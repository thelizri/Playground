from flask import Flask, request
from db import items, stores
import uuid

app = Flask(__name__)


# Methods for retrieving stores and posting stores
@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404


@app.post("/store")
def post_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201


# Methods for retrieving items and posting items
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message": "Item not found"}, 404


@app.post("/item")
def post_item_to_store():
    item_data = request.get_json()
    try:
        if item_data["store_id"] not in stores:
            return {"message": "Store not found"}, 404
    except KeyError:
        return {"message": "Item needs store id"}, 400
    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item
    return new_item, 201
