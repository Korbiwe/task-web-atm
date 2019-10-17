from numbers import Number

from flask import request

from atm.money import money
from atm.money.atm import Atm
from atm.core.utils import json_response
from atm.core.exceptions import AtmUserError


@money.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()

    try:
        currency = data['currency']
        value = data['value']
        quantity = data['quantity']
    except KeyError:
        raise AtmUserError('tbd', 'Please provide the following keys in your json: currency, value, quantity')

    if not isinstance(currency, str) or not isinstance(value, Number) or not isinstance(quantity, int):
        raise AtmUserError('tbd', 'Currency must be a string, value must be a number, quantity must be an integer.')

    if quantity <= 0:
        raise AtmUserError('tbd', 'You cannot deposit non-positive quantities of banknotes.')

    Atm.deposit(currency, value, quantity)
    return json_response()


@money.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()

    try:
        currency = data['currency']
        amount = data['amount']
    except KeyError:
        raise AtmUserError('tbd', 'Please provide the following keys in your json: currency, quantity')

    if not isinstance(currency, str) or not isinstance(amount, Number):
        raise AtmUserError('tbd', 'Currency must be a string, amount must be a number.')

    if amount <= 0:
        raise AtmUserError('tbd', 'You can\'t withdraw non-positive amounts of money.')

    result = Atm.withdraw(currency, amount)
    return json_response(result=result)
