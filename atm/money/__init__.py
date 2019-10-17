__all__ = ['money']
from flask import Blueprint

money = Blueprint('money', __name__)

from atm.money.logging import logger
from atm.money.views import *
