from flask import Blueprint, render_template, request, session, url_for, redirect
from const import *

def get_byid(username):
    return User.query.filter_by(username=username).first() if username else None

user_bp = Blueprint(
    name='user_bp', import_name=__name__,
    static_folder=STATIC_FOLDER,
    template_folder=USER_FOLDER,
    url_prefix='/user'
)

@user_bp.route('/', methods=['GET'])
def user_me():
    isExist = session.get('username', None)
    isExist = get_byid(isExist) if isExist else None
    summRating = 0

    if request.method == "GET":
        r = request.args.get
        if r('act', None):
            act = r('act').split('!')
            if act[0] == 'add_wishlist':
                if len(Wishlist.query.filter_by(user_id=isExist.id, product_id=int(act[1])).all()) < 1:
                    wishlist = Wishlist(
                        user_id=isExist.id,
                        product_id=int(act[1])
                    )
                
                    db.session.add(wishlist)
                    db.session.commit()

                    return redirect(url_for('user_bp.user_me'))
            elif act[0] == 'remove_product':
                    db.session.query(Wishlist).filter_by(product_id=int(act[1])).delete()
                    db.session.query(Reviews).filter_by(product_id=int(act[1])).delete()
                    db.session.query(Product).filter_by(owner_id=isExist.id, id=int(act[1])).delete()

                    db.session.commit()
    if isExist:
        summRating = (
            db.session.query(db.func.sum(Product.rating)).filter_by(owner_id=isExist.id).scalar() or 0
        )



    return render_template('user_iam.html', isExist=isExist, 
                                            production=Product.query.filter_by(owner_id=isExist.id).all() if isExist else None,
                                            summRating=summRating
                           )

@user_bp.route('/<int:uid>/user')
def user_user(uid):
    isExist = session.get('username', None)
    isExist = get_byid(isExist) if isExist else None

    summRating = 0

    if request.method == "GET":
        r = request.args.get
        if r('act', None):
            act = r('act').split('!')
            if act[0] == 'add_wishlist':
                if len(Wishlist.query.filter_by(user_id=isExist.id, product_id=int(act[1])).all()) < 1:
                    wishlist = Wishlist(
                        user_id=isExist.id,
                        product_id=int(act[1])
                    )
                
                    db.session.add(wishlist)
                    db.session.commit()

                    return redirect(url_for('user_bp.user_user', uid=uid))

    summRating = (
        db.session.query(db.func.sum(Product.rating)).filter_by(owner_id=uid).scalar() or 0
    )

    return render_template('user_user.html', isExist=isExist,
                                            user=User.query.filter_by(id=uid).first(),
                                            production=Product.query.filter_by(owner_id=uid).all(),
                                            summRating=summRating
                          )