from flask import Flask, redirect
from const import *
from bp import main_bp, shop_bp, user_bp

app = Flask(
    import_name=__name__,
    static_folder=STATIC_FOLDER,
)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{pasw}@{host}/{dbname}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

db.init_app(app)
with app.app_context():
    #db.drop_all()
    db.create_all()

app.register_blueprint(main_bp)
app.register_blueprint(shop_bp)
app.register_blueprint(user_bp)

@app.route('/')
def index():
    return redirect(location='/main/')

@app.errorhandler(404)
def err404(er):
    return f"Не існує",404

if __name__ == "__main__":
    app.run(
        host='localhost',
        port=8000,
        debug=True
    )
