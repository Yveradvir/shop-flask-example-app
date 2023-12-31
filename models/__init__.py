from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()


from .wishlist import Wishlist
from .product  import Product
from .user     import User
from .reviews  import Reviews