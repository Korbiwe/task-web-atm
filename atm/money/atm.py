from atm.money.models import BanknoteStore
from atm.core.models import db
from atm.core.exceptions import AtmUserError, AtmUnprocessableError


class Atm:
    @staticmethod
    def withdraw(currency, amount):
        stores = BanknoteStore.query\
            .filter_by(currency=currency)\
            .filter(BanknoteStore.banknote_quantity != 0)\
            .order_by(BanknoteStore.banknote_value.desc())\
            .all()

        if len(stores) == 0:
            raise AtmUserError('tbd', f'This ATM does not provide {currency} at the moment.')

        result = []

        for store in stores:
            quantity_taken = store.withdraw_banknotes(amount)

            if quantity_taken != 0:
                amount -= quantity_taken * store.banknote_value
                result.append({'value': store.banknote_value, 'quantity': quantity_taken})

        if amount != 0:
            db.session.rollback()
            available_banknotes = [{'value': store.banknote_value, 'quantity': store.banknote_quantity}
                                   for store in stores]
            raise AtmUnprocessableError('tbd',
                                        f'Sorry, we cannot fulfill your request. '
                                        f'Please refer to the \'params\' key for available banknotes for {currency}.',
                                        available_banknotes=available_banknotes)

        db.session.commit()
        return result

    @staticmethod
    def deposit(currency, value, quantity):
        store = BanknoteStore.query.filter_by(currency=currency, banknote_value=value).first()

        if store is None:
            raise AtmUserError('tbd', f'This ATM does not accept banknotes of currency {currency} with value {value}.')

        store.add(quantity)

        db.session.commit()
