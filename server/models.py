from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    selected_price_range = db.Column(db.Integer, db.ForeignKey('price_ranges.id'))

class PriceRanges(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    min_price = db.Column(db.Integer, nullable=False)
    max_price = db.Column(db.Integer, nullable=False)

class Ratings(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    build_id = db.Column(db.Integer, db.ForeignKey('builds.id'))
    rating = db.Column(db.Integer, nullable=False)

class BuildType(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(100), nullable=False)

class Builds(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    price_range_id = db.Column(db.Integer, db.ForeignKey('price_ranges.id'))
    build_type_id = db.Column(db.Integer, db.ForeignKey('build_type.id'))

    components = db.relationship("BuildComponents", uselist=False, back_populates="build")

# Component models
# # GPU Model
class GPU(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    Speed = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

# CPU Model
class CPU(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String, nullable=False)
    Speed = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

# Memory Model
class Memory(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    Speed = db.Column(db.Integer, nullable=False)
    Size = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

# MotherBoard Model
class MotherBoard(db.Model, SerializerMixin):
    __tablename__ = 'motherboard'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    Type = db.Column(db.String(50), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

# Storage Model
class Storage(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    Size = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

# PSU Model
class PSU(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    Wattage = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

# Case Model
class Case(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    Type = db.Column(db.String(50), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

class BuildComponents(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)  
    build_id = db.Column(db.Integer, db.ForeignKey('builds.id'))
    gpu_id = db.Column(db.Integer, db.ForeignKey('gpu.id'))
    cpu_id = db.Column(db.Integer, db.ForeignKey('cpu.id'))
    memory_id = db.Column(db.Integer, db.ForeignKey('memory.id'))
    motherboard_id = db.Column(db.Integer, db.ForeignKey('motherboard.id'))
    storage_id = db.Column(db.Integer, db.ForeignKey('storage.id'))
    psu_id = db.Column(db.Integer, db.ForeignKey('psu.id'))
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'))

    build = db.relationship("Builds", back_populates="components")

    