from os import path, PathLike, getenv, getcwd
from dotenv import load_dotenv
from models import *

load_dotenv(
    path.join(
        getcwd(), '.env'
    )
)

g = getenv

SECRET_KEY = g('key')
dbname, user, pasw, host = g('db'), g('user'), g('pasw'), g('host')

def templates(bpname: str) -> PathLike:
    return path.join(
        path.dirname(__file__), 
        'bp', bpname, 'templates'
    )

STATIC_FOLDER = path.join(
    path.dirname(__file__),
    'static'
)

MAIN_FOLDER   = templates('main')
SHOP_FOLDER   = templates('shop')
USER_FOLDER   = templates('user')