from mail import mail
from jobs import celery
from celery.schedules import crontab
from flask_mail import Message
from database import User
from datetime import datetime, timedelta

@celery.task(name="mail.monthly_summary")
def summary():
    user_list = User.query.all()
    for user in user_list:
        cards_pending = list(filter(lambda x : x.isComplete==False,user.userCards))
        all_completed_cards = list(filter(lambda x : x.isComplete==True,user.userCards))
        cards_completed_last_month = list(filter(lambda x: x.completionDate.date() >= (
            datetime.now() - timedelta(days=30)).date(), all_completed_cards))
        if cards_pending or cards_completed_last_month:
            msg = Message('Monthly Summary from Kanban',
                          sender="summary@kanban.com", recipients=[user.email])
            msg.body = "Hello {},\n\n You have completed {} cards this month.\n".format(user.username,len(cards_completed_last_month))
            if cards_pending:
                msg.body += "You have the following tasks pending:\n"
                for card in cards_pending:
                    msg.body += card.cardName + "\n"
                msg.body += "\n"
            msg.body += "Thank you for using Kanban!\n\n"
            mail.send(msg)
            return "ok"
    return "not ok"


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(day_of_month=1, hour=20, minute=0), summary.s(), name="mail.monthly_summary")
    #test mail in every 10 seconds
    # sender.add_periodic_task(10.0, summary.s(), name="mail.monthly_summary")