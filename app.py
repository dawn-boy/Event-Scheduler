from flask import Flask
from config import Config
from extensions import db


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

app.run(debug=True)