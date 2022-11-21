import flask
from flask import Flask
from controllers.github import app as github_controller
from models.models import db
import config

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gitusers.sqlite3'

app.register_blueprint(github_controller, url_prefix="/")

if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True, port=config.PORT)