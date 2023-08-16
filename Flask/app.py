from flask import Flask, request
from flask_smorest import abort
from flask_sqlalchemy import SQLAlchemy
from models import StoreModel, ItemModel
from db import db, stores, items
import uuid


def create_app():
    app = Flask(__name__)

    # Configure the database URI. Here's an example for SQLite
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


app = create_app()


# Methods for retrieving stores and posting stores
@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")


@app.post("/store")
def post_store():
    store_data = request.get_json()

    # Validating required arguments
    if "name" not in store_data:
        abort(
            400,
            message="Bad request. Make sure 'name' is included in the JSON payload.",
        )

    # Checking if store already exist
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message="Store already exist.")

    # Adding new store
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201


@app.put("/store/<string:store_id>")
def update_store(store_id):
    store_data = request.get_json()
    try:
        store = stores[store_id]
        store |= store_data

        return store
    except KeyError:
        abort(404, message="Item not found")


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted"}
    except KeyError:
        abort(404, message="Store not found")


# Methods for retrieving items and posting items
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")


@app.post("/item")
def post_item_to_store():
    item_data = request.get_json()

    # Validating required arguments
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(
            400,
            message="Bad request. Make sure 'price', 'store_id', and 'name' are included in the JSON payload.",
        )

    # Checking if item already exist
    for item in items.values():
        if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(400, message="Bad request. Item already exists.")

    # Adding new item
    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item
    return new_item, 201


@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    try:
        item = items[item_id]
        item |= item_data

        return item
    except KeyError:
        abort(404, message="Item not found")


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted"}
    except KeyError:
        abort(404, message="Item not found")
