from flask import Flask
from app.routes import cleaner_bp
from common.config import Config
from app.models import db

app = Flask(__name__)


app.config.from_object(Config)


db.init_app(app)


app.register_blueprint(cleaner_bp, url_prefix='/database')


with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
    app.run(debug=True)