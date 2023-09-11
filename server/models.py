from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db
import bcrypt

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class CPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    core_count = db.Column(db.Integer)
    performance_core_clock = db.Column(db.Float)
    price = db.Column(db.Float)

    def __init__(self, name, core_count, performance_core_clock, price):
        self.name = name
        self.core_count = core_count
        self.performance_core_clock = performance_core_clock
        self.price = price
