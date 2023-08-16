from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=False, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")

    def __init__(self, name, address):
        self.name = name
        self.address = address
