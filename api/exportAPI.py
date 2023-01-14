from os import remove
from flask import jsonify, send_file, request, after_this_request
from database import List, Card
from jobs.export import export_list_as_csv, export_card_as_csv
from . import API


@API.route("/export/card/<int:cardID>", methods=["GET"])
def export_card(cardID):
    card = Card.query.get(cardID)
    if card is None:
        return jsonify({'message': 'Card not found'}), 404
    task = export_card_as_csv.delay(cardID)
    return jsonify({'message': 'Exporting card as CSV',"taskID":task.id}), 200


@API.route('/export/list/<int:listID>', methods=['GET'])
def export_list(listID):
    print("Exporting list as CSV")
    print(listID)
    export_list = List.query.get(listID)
    if export_list is None:
        return jsonify({'message': 'List not found'}), 404
    task = export_list_as_csv.delay(listID)
    return jsonify({'message': 'Exporting list as CSV', 'taskID': task.id}), 200

@API.route('/export/status', methods=['POST'])
def export_status():
    req = request.get_json()
    print(req)
    taskID = req['taskID']
    task = export_list_as_csv.AsyncResult(taskID)
    return jsonify({'taskID': task.id, 'status': task.status}), 200


@API.route("/export/download/card/<int:cardID>", methods=["GET"])
def download_card_as_csv(cardID):
    card = Card.query.filter_by(cardID=cardID).first()
    if card is None:
        return jsonify({'message': 'Card not found'}), 404

    @after_this_request
    def remove_file(response):
        try:
            remove("static/export-card-{}.csv".format(cardID))
        except Exception as error:
            print(error)
        return response
    return send_file("static/export-card-{}.csv".format(cardID), as_attachment=True)


@API.route('/export/download/list/<int:listID>', methods=['GET'])
def download_list_as_csv(listID):
    export_list = List.query.get(listID)
    if export_list is None:
        return jsonify({'message': 'List not found'}), 404
    @after_this_request
    def remove_file(response):
        try:
            remove("static/export-list-{}.csv".format(listID))
        except Exception as error:
            print(error)
        return response
    return send_file("static/export-list-{}.csv".format(listID), as_attachment=True)
