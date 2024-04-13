from flask import render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from forms import LoginForm, RegisterForm
from models import User, Product, User2, db

def configure_routes(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.password == form.password.data:
                login_user(user)
                return redirect(url_for('addb'))
        return render_template('login.html', form=form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            new_user = User(username=form.username.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        return render_template('register.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('home'))

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/shop')
    def shop():
        products = Product.query.all()
        return render_template('shop.html', products=products)

    @app.route('/addb', methods=['GET', 'POST'])
    @login_required
    def add():
        form = ProductForm()
        if form.validate_on_submit():
            new_product = Product(name=form.name.data,
                                  description=form.description.data,
                                  price=form.price.data)
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for('shop'))
        return render_template('addb.html', form=form)

    @app.route('/about', methods=['GET', 'POST'])
    def add_user():
        form = LoginForm2()
        if form.validate_on_submit():
            new_user2 = User2(name1=form.name.data,
                              surname=form.surname.data,
                              login=form.login.data)
            db.session.add(new_user2)
            db.session.commit()
            return redirect(url_for('shop'))
        return render_template('about.html', form=form)

    @app.route('/delete/<id>', methods=['POST'])
    def delete(id):
        product_delete = Product.query.get_or_404(id)
        db.session.delete(product_delete)
        db.session.commit()
        return redirect(url_for('shop'))
