from flask import Flask
from app.routes import cleaner_bp

app = Flask(__name__)

app.register_blueprint(cleaner_bp, url_prefix='/cleaner')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
