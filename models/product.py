from . import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, nullable=False)

    currency = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    rating = db.Column(db.Float, nullable=False)


    def __init__(self, owner_id, currency, price, quantity, name, rating=0, description=None):
        self.owner_id = owner_id
        self.currency = currency
        self.price = price
        self.quantity = quantity
        self.name = name
        self.description = description

        self.rating = rating

    def __repr__(self):
        return f"Product(id={self.id}, owner_id={self.owner_id}, currency={self.currency}, price={self.price}, name={self.name})"
