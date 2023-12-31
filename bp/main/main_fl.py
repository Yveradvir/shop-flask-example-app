from flask import Blueprint, render_template, request, session, url_for, redirect
from const import *


main_bp = Blueprint(
    name='main_bp', import_name=__name__,
    static_folder=STATIC_FOLDER,
    template_folder=MAIN_FOLDER,
    url_prefix='/main'
)


@main_bp.route('/', methods=['GET'])
def index():
    username = session.get('username', None)

    if username and request.method == 'GET':
        if request.args.get('act') == 'delete':
            session.pop('username')

    return render_template('index.html', username=username)

@main_bp.route('/auth', methods=["GET", "POST"])
def auth():
    isExist = ['none', '']

    if request.method == "POST":
        r = request.form
        if r['act']:
            _user = User.query.filter_by(username=r['username']).first()
            if   r['act'] == 'l':
                if not _user: isExist = ['block', 'User does\'nt exist']
                else:
                    if _user.password == r['password']:
                        session['username'] = r['username']
                        return redirect(url_for('shop_bp.shop_index'))

            elif r['act'] == 's':
                if _user: isExist = ['block', 'User arleady exist']
                else:
                    user = User(
                        username=r['username'],
                        password=r['password']
                    )

                    db.session.add(user)
                    db.session.commit()

                    session['username'] = r['username']
                    return redirect(url_for('shop_bp.shop_index'))

    return render_template('auth.html', isExist=isExist)