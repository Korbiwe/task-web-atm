from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.ext.declarative import declared_attr

from atm.core.utils import random_uuid4_as_hex

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    id = db.Column(db.String, primary_key=True, default=random_uuid4_as_hex,
                   unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def as_dict(self):
        return {
            c.name: getattr(self, c.name)
            for c in self.__table__.columns
        }
