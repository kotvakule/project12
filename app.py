from flask import Flask
from routes import configure_routes
from models import db, login_manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\user\\PycharmProjects\\Final_html_project\\test.db'
app.config['SECRET_KEY'] = 'mysecretkey'
db.init_app(app)
login_manager.init_app(app)
configure_routes(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
