from flask import Flask

from routes.tuor import tuor_route
from models.tuor import Tuor
from models.base import create_db


app = Flask(__name__)
app.register_blueprint(tuor_route)


if __name__ == "__main__":
    create_db()
    app.run(debug=True)