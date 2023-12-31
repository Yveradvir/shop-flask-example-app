from flask import Blueprint, render_template, request, session, url_for, redirect
from const import *

def get_byid(username):
    return User.query.filter_by(username=username).first() if username else None

shop_bp = Blueprint(
    name='shop_bp', import_name=__name__,
    static_folder=STATIC_FOLDER,
    template_folder=SHOP_FOLDER,
    url_prefix='/shop'
)


@shop_bp.route('/', methods=["GET"])
def shop_index():
    isExist = session.get('username', None)
    isExist = get_byid(isExist) if isExist else None

    if request.method == "GET":
        r = request.args.get
        if r('act', None):
            act = r('act').split('!')
            if act[0] == 'add_wishlist':
                if len(Wishlist.query.filter_by(
                    user_id=isExist.id,
                    product_id=int(act[1])
                ).all()) < 1:
                    
                    wishlist = Wishlist(
                        user_id=isExist.id,
                        product_id=int(act[1])
                    )
                
                    db.session.add(wishlist)
                    db.session.commit()

                    return redirect(url_for('shop_bp.shop_index'))

    return render_template('shop_index.html', isExist=isExist, products=Product.query.all())


@shop_bp.route('/new', methods=['GET', 'POST'])
def shop_new():
    isExist = session.get('username', None)
    isExist = get_byid(isExist) if isExist else None

    if request.method == 'POST':
        r = request.form
        if r['act']:
            owner_id = get_byid(session.get('username', None)).id

            production = Product(
                owner_id=owner_id,
                name=r['name'], description=r['description'],
                currency=r['currency'], price=r['price'], quantity=r['quantity'],
                rating=0
            )

            db.session.add(production)
            db.session.commit()

            return redirect(url_for('shop_bp.shop_product', id=production.id))

    return render_template('shop_new.html', isExist=isExist)

@shop_bp.route('/<int:id>/product', methods=['GET', 'POST'])
def shop_product(id):
    isExist = session.get('username', None)
    isExist = get_byid(isExist) if isExist else None
    doReviewed = Reviews.query.filter_by(product_id=id, user_id=isExist.id).all() if isExist else None
    product = Product.query.filter_by(id=id).first()

    if request.method == 'POST' and request.form.get('act', None):
        r = request.form
        print(r)
        review = Reviews(
            user_id=isExist.id, product_id=id,
            title=r['title'], description=r['description'],
            rating=r['rating']
        )

        product.rating += float(r['rating'])

        db.session.add(review)
        db.session.commit()
        return redirect(url_for('shop_bp.shop_product', id=id))
    
    if request.method == "GET":
        r = request.args.get
        if r('act', None):
            act = r('act').split('!')
            if act[0] == 'add_wishlist':
                if len(Wishlist.query.filter_by(
                    user_id=isExist.id,
                    product_id=int(act[1])
                ).all()) < 1:
                    
                    wishlist = Wishlist(
                        user_id=isExist.id,
                        product_id=int(act[1])
                    )
                
                    db.session.add(wishlist)
                    db.session.commit()

                    return redirect(url_for('shop_bp.shop_product', id=id))



    return render_template('shop_product.html', 
                           isExist=isExist if isExist else None, doReviewed=doReviewed,
                           product=product, reviews=Reviews.query.filter_by(product_id=id).all())


@shop_bp.route('/<int:uid>/wishlist', methods=['GET'])
def shop_wishlist(uid):
    isExist = session.get('username', None)
    isExist = get_byid(isExist) if isExist else None

    wishlist = None
    if isExist: wishlist = Wishlist.query.filter_by(user_id=isExist.id).all()

    if request.method == "GET":
        r = request.args.get
        if r('act', None):
            act = r('act').split('!')
            if act[0] == 'remove_wishlist':
                Wishlist.query.filter_by(
                    user_id=isExist.id,
                    product_id=int(act[1])
                ).delete()

                db.session.commit()
                return redirect(url_for('shop_bp.shop_wishlist', uid=uid))

    return render_template('shop_wishlist.html', isExist=isExist,
                           isthisme=int(isExist.id) == int(uid) if isExist else None,
                           wishlist=wishlist)