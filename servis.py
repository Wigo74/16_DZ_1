from models import *
from config import db
import json


def insert_data_user(input_data):
    for row in input_data:
        db.session.add(
            User(
                id=row.get("id"),
                first_name=row.get("first_name"),
                last_name=row.get("last_name"),
                age=row.get("age"),
                email=row.get("email"),
                role=row.get("role"),
                phone=row.get("phone"),
            )
        )

        db.session.commit()


def insert_data_order(input_data):
    for row in input_data:
        db.session.add(
            Order(
                id=row.get("id"),
                name=row.get("name"),
                description=row.get("description"),
                start_date=row.get("start_date"),
                end_date=row.get("end_date"),
                address=row.get("address"),
                price=row.get("price"),
                customer_id=row.get("customer_id"),
                executor_id=row.get("executor_id"),
            )
        )

    db.session.commit()


def insert_data_offer(input_data):
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get("id"),
                order_id=row.get("order_id"),
                executor_id=row.get("executor_id"),
            )
        )

    db.session.commit()


db.drop_all()
db.create_all()


def get_all_users():
    result = []
    for row in User.query.all():
        result.append((row.get_user()))
    return result


def get_all_orders():
    result = []
    for row in Order.query.all():
        result.append((row.get_order()))
    return result


def get_all_offers():
    result = []
    for row in Offer.query.all():
        result.append((row.get_offer()))
    return result


def update_method(model, user_id, values):
    try:
        db.session.query(model).filter(model.id == user_id).update(values)
        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def delete_method(model, user_id):
    try:
        db.session.query(model).filter(model.id == user_id).delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def init_db():
    db.drop_all()
    db.create_all()

    with open("data/user.json") as file:
        insert_data_user(json.load(file))

    with open("data/orders.json") as file:
        insert_data_order(json.load(file))

    with open("data/offer.json") as file:
        insert_data_offer(json.load(file))


def update_user(model, user_id, values):
    try:
        data = db.session.query(model).get(user_id)
        data.id = values.get('id')
        data.first_name = values.get('irst_name')
        data.last_name = values.get('last_name')
        data.age = values.get('age')
        data.email = values.get('email')
        data.role = values.get('role')
        data.phone = values.get('phone')
        db.session.commit()
    except Exception as e:
        print(e)
        return {}
