from . import db


class Reviews(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    rating = db.Column(db.Integer) 

    user = db.relationship('User', backref='reviews')
    product = db.relationship('Product', backref='reviews')

    def __repr__(self):
        return f"Reviews(id={self.id}, user_id={self.user_id}, product_id={self.product_id})"
