import json
from flask import request
from config import app, db
from models import User, Order, Offer
from servis import init_db, get_all_users, get_all_orders, get_all_offers, insert_data_user, update_user, update_method


@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    """Выводим всех users"""
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all_users(), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json")
    elif request.method == 'POST':
        insert_data_user(request.json)
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json")


@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_user_id(user_id):
    """Выводим одного users по id"""
    if request.method == 'GET':
        data = get_all_users()
        for row in data:
            if row.get("id") == user_id:
                return app.response_class(
                        response=json.dumps(row, indent=4, ensure_ascii=False),
                        status=200,
                        mimetype="application/json"
                    )
    elif request.method == 'PUT':
        update_method(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json")
    elif request.method == 'DELETE':
        update_method(User, user_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json")

@app.route("/orders/")
def get_orders():
    """Выводим всех заказы"""
    return app.response_class(
        response=json.dumps(get_all_orders(), indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json")


@app.route("/orders/<int:order_id>", methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(order_id):
    """Выводим заказ по id"""
    if request.method == 'GET':
        data = get_all_orders()
        for row in data:
            if row.get("id") == order_id:
                return app.response_class(
                    response=json.dumps(row, indent=4, ensure_ascii=False),
                    status=200,
                    mimetype="application/json")
    elif request.method == 'PUT':
        update_method(Order, order_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json")
    elif request.method == 'DELETE':
        update_method(Order, order_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json")


@app.route("/offers/")
def get_offers():
    """Выводим всех предложения"""
    return app.response_class(
        response=json.dumps(get_all_offers(), indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json")


@app.route("/offers/<int:offer_id>", methods=['GET', 'PUT', 'DELETE'])
def get_offers_by_id(offer_id):
    """Выводим предложения по id"""
    if request.method == 'GET':
        data = get_all_offers()
        for row in data:
            if row.get("id") == offer_id:
                return app.response_class(
                    response=json.dumps(row, indent=4, ensure_ascii=False),
                    status=200,
                    mimetype="application/json")
    elif request.method == 'PUT':
        update_method(Offer, offer_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json")
    elif request.method == 'DELETE':
        update_method(Offer, offer_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json")

if __name__ == "__main__":
    init_db()
    app.run(port=8000, debug=True)
