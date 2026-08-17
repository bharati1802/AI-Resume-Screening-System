from flask import Flask

from app.database import create_table
from app.routes import main


def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    create_table()

    app.register_blueprint(main)

    return app