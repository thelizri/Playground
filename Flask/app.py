from flask import Flask, request

app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "Chair"}, {"name": "Soffa"}]}]


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def post_stores():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201
