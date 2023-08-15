from flask import Flask, request
from flask_smorest import abort
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
        abort(404, message="Store not found")


@app.post("/store")
def post_store():
    store_data = request.get_json()

    # Validating required arguments
    if "name" not in store_data:
        abort(400, "Bad request. Make sure 'name' is included in the JSON payload.")

    # Checking if store already exist
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, "Store already exist.")

    # Adding new store
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
            "Bad request. Make sure 'price', 'store_id', and 'name' are included in the JSON payload.",
        )

    # Checking if item already exist
    for item in items.values():
        if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(
                400,
                "Item already exists",
            )

    # Adding new item
    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item
    return new_item, 201


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted"}
    except KeyError:
        abort(404, message="Item not found")
