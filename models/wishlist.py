from . import db

class Wishlist(db.Model):
    __tablename__ = 'wishlist'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

    user = db.relationship('User', backref='wishlist')
    product = db.relationship('Product', backref='wishlist')

    def __repr__(self):
        return f"Wishlist(id={self.id}, user_id={self.user_id}, product_id={self.product_id})"
