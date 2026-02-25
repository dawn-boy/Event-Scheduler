from flask import Flask
from config import Config
from extensions import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from models import Event
        db.create_all()

    from routes import main
    app.register_blueprint(main)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=False)