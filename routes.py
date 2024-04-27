from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user
from app import app, db, login_manager
from models import User
from forms import LoginForm, RegisterForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/a')
def a():
    return render_template('a.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_page'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('main_page'))
        else:
            error = 'Неверные учетные данные. Пожалуйста, попробуйте еще раз или зарегистрируйтесь.'
    return render_template('login.html', form=form, error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        name=form.name.data,
                        surname=form.surname.data,
                        birthday = form.birthday.data,
                        phone = form.phone.data,
                        password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/order')
def order():
    return render_template('order.html')


@app.route('/cart')
@login_required
def cart():
    return render_template('cart.html')

if __name__ == "__main__":
    app.run(debug=True)
