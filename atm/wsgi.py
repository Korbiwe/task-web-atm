from flask import Flask

from atm.config import Config
from atm.core.models import db

from atm.core import core as core_blueprint
from atm.money import money as money_blueprint
from atm.money.seed import seed as seed_atm

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(money_blueprint)
app.register_blueprint(core_blueprint)


@app.before_first_request
def seed():
    seed_atm()

db.init_app(app)
