from database import Card, List
from . import celery


@celery.task
def export_list_as_csv(listID):
    export_list = List.query.get(listID)
    file = open("static/export-list-{}.csv".format(listID), "w")
    file.write("cardID,cardName,content,deadline,creationDate,isComplete,completionDate,lastEdited \n")
    for card in export_list.listCards:
        file.write("{},{},{},{},{},{},{},{} \n".format(card.cardID, card.cardName, card.content, card.deadline,
                                                       card.creationTime, card.isComplete, card.completionDate,
                                                       card.lastEdited))
    file.close()
    return "done"
l

@celery.task
def export_card_as_csv(cardID):
    card = Card.query.get(cardID)
    file = open("static/export-card-{}.csv".format(cardID), "w")
    file.write("cardID,cardName,content,deadline,creationDate,isComplete,completionDate,lastEdited \n")
    file.write(
        "{},{},{},{},{},{},{},{} \n".format(card.cardID, card.cardName, card.content, card.deadline, card.creationTime,
                                            card.isComplete, card.completionDate, card.lastEdited))
    file.close()
    return "done"
