> I used the [font awesome icons](https://fontawesome.com/) in NON COMERCIAL GOALS

>I used flask, flask_sqlalchemy and nothing other.
```
pip install flask
pip install Flask-SQLAlchemy
```

You should create a .env file in the cwd, content of .env:
```
db    = ""
pasw  = ""
user  = ""
host  = ""
port  = numbers
key   = ""
```

You should have a postgress, otherwise change `SQLALCHEMY_DATABASE_URI` in app.setting.
