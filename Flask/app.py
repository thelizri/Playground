from flask import Flask, request
from flask_smorest import abort
from flask_sqlalchemy import SQLAlchemy
from models import StoreModel, ItemModel
from db import db


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
    # Query all stores from the database
    store_objects = StoreModel.query.all()

    # Convert the list of StoreModel objects to a list of dictionaries
    stores_list = [store.get_dict() for store in store_objects]

    return {"stores": stores_list}


@app.get("/store/<int:store_id>")
def get_store(store_id):
    store = StoreModel.query.get(store_id)
    if store:
        return store.get_dict()
    else:
        abort(404, message="Store not found")


@app.post("/store")
def post_store():
    store_data = request.get_json()

    # Validating required arguments
    if "name" not in store_data or "address" not in store_data:
        abort(
            400,
            message="Bad request. Make sure 'name' and 'address' is included in the JSON payload.",
        )

    if StoreModel.query.filter_by(name=store_data["name"]).first():
        abort(400, message="Store already exists.")

    new_store = StoreModel(name=store_data["name"], address=store_data["address"])
    db.session.add(new_store)
    db.session.commit()

    return new_store.get_dict(), 201


@app.put("/store/<int:store_id>")
def update_store(store_id):
    store_data = request.get_json()

    existing_store = StoreModel.query.get(store_id)
    if existing_store is None:
        abort(404, message="Store not found")

    if "name" in store_data:
        existing_store.name = store_data["name"]
    if "address" in store_data:
        existing_store.address = store_data["address"]

    db.session.commit()
    return existing_store.get_dict()


@app.delete("/store/<int:store_id>")
def delete_store(store_id):
    existing_store = StoreModel.query.get(store_id)
    if existing_store is None:
        abort(404, message="Store not found")

    db.session.delete(existing_store)
    db.session.commit()

    return {"message": f"Store with ID {store_id} has been deleted"}


# Methods for retrieving items and posting items
@app.get("/item")
def get_all_items():
    items = ItemModel.query.all()
    items_list = [item.get_dict() for item in items]
    return {"items": items_list}


@app.get("/item/<int:item_id>")
def get_item(item_id):
    item = ItemModel.query.get(item_id)
    if item:
        return item.get_dict()
    else:
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

    if ItemModel.query.filter_by(name=item_data["name"]).first():
        abort(400, "Item already exists.")

    new_item = ItemModel(
        name=item_data["name"], price=item_data["price"], store_id=item_data["store_id"]
    )
    db.session.add(new_item)
    db.session.commit()
    return new_item.get_dict(), 201


@app.put("/item/<int:item_id>")
def update_item(item_id):
    existing_item = ItemModel.query.get(item_id)
    if existing_item is None:
        abort(404, message="Item not found")

    item_data = request.get_json()
    if "name" in item_data:
        existing_item.name = item_data["name"]
    if "price" in item_data:
        existing_item.price = item_data["price"]
    if "store_id" in item_data:
        existing_item.store_id = item_data["store_id"]

    db.session.commit()
    return existing_item.get_dict()


@app.delete("/item/<int:item_id>")
def delete_item(item_id):
    existing_item = ItemModel.query.get(item_id)
    if existing_item is None:
        abort(404, message="Item not found")

    db.session.delete(existing_item)
    db.session.commit()
    return {"message": f"Item with ID {item_id} has been deleted"}
