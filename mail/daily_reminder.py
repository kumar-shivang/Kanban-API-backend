from jobs import celery
from . import mail
from flask_mail import Message
from celery.schedules import crontab
from database import User
from datetime import datetime, timedelta


@celery.task(name="mail.daily_reminder")
def reminder():
    user_list = User.query.all()
    for user in user_list:
        cards_pending = list(filter(lambda x: x.isComplete == False, user.userCards))
        cards_upcoming_tomorrow = list(filter(lambda x: x.deadline.date() == (
            datetime.now() + timedelta(days=1)).date(), cards_pending))
        cards_deadline_today = list(
            filter(lambda x: x.deadline.date() == datetime.now().date(), cards_pending))
        if cards_pending:
            msg = Message('Daily Reminder from Kanban',
                          sender="reminder@kanban.com", recipients=[user.email])
            msg.body = "Hello {},\n\n You have {} cards pending.".format(user.username,len(cards_pending))
            if cards_deadline_today:
                msg.body += "You have the following tasks due today:\n"
                for card in cards_deadline_today:
                    msg.body += card.cardName + "\n"
                msg.body += "\n"
            if cards_upcoming_tomorrow:
                msg.body += "You have the following tasks due tomorrow:\n"
                for card in cards_upcoming_tomorrow:
                    msg.body += card.cardName + "\n"
                msg.body += "\n"
            msg.body += "Thank you for using Kanban!\n\n"
            mail.send(msg)
            return "ok"
    return "not ok"


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(
        hour=20, minute=0, day_of_week="*"), reminder.s(), name="mail.daily_reminder")
    # test mail in every 10 seconds
    # sender.add_periodic_task(10.0, reminder.s(), name="mail.daily_reminder")  
