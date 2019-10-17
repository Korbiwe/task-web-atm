from atm.core.models import db
from atm.money.models import BanknoteStore
from atm.money.currencies import allowed_banknotes


def seed():
    db.create_all()

    for currency, values in allowed_banknotes.items():
        for value in values:
            if BanknoteStore.query.filter_by(currency=currency, banknote_value=value).first() is None:
                new_store = BanknoteStore(currency=currency, banknote_value=value)
                db.session.add(new_store)
                db.session.commit()
