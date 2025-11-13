from flask import Flask
from .db import db
from .routes.items import items_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(items_bp)

    @app.get("/")
    def home():
        return {"message": "App running!"}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)