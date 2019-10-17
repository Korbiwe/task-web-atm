from sqlalchemy import UniqueConstraint

from atm.core.models import db, BaseModel
from atm.money.currencies import allowed_banknotes, Currencies


class BanknoteStore(BaseModel):
    currency = db.Column(db.Enum(Currencies))
    banknote_value = db.Column(db.Integer)
    banknote_quantity = db.Column(db.Integer, default=0)

    __tableargs__ = (UniqueConstraint('currency', 'banknote_value'), )

    def __init__(self, *, banknote_value, currency, **kwargs):
        if banknote_value not in allowed_banknotes[currency]:
            raise ValueError(f'Banknote with value {banknote_value} does not exist in currency {currency}!')

        super(BanknoteStore, self).__init__(banknote_value=banknote_value, currency=currency, **kwargs)

    def add(self, quantity):
        self.banknote_quantity += quantity
        db.session.commit()

    def quantity(self, amount):
        return int(amount / self.banknote_value)

    def withdraw_banknotes(self, amount):
        quantity = self.quantity(amount)
        if self.banknote_quantity - quantity < 0:
            # Give out all we have left in this store despite not being able to provide the full quantity
            quantity_given = self.banknote_quantity
            self.banknote_quantity = 0
            return quantity_given

        self.banknote_quantity -= quantity

        return quantity
