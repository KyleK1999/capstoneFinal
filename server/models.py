from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    selected_price_range = db.Column(db.Integer, db.ForeignKey('price_ranges.id'))

    saved_builds = relationship('Builds', backref='user')

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'selected_price_range': self.selected_price_range
        }

class PriceRanges(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    min_price = db.Column(db.Integer, nullable=False)
    max_price = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'min_price': self.min_price,
            'max_price': self.max_price,
        }

class Ratings(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    build_id = db.Column(db.Integer, db.ForeignKey('builds.id'))
    rating = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'build_id': self.build_id,
            'rating': self.rating,
        }

class BuildType(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'type_name': self.type_name,
        }


class Builds(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    price_range_id = db.Column(db.Integer, db.ForeignKey('price_ranges.id'))
    build_type_id = db.Column(db.Integer, db.ForeignKey('build_type.id'))
    components = db.relationship("BuildComponents", uselist=False, back_populates="build")
    build_type = db.relationship("BuildType")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def serialize(self):
        return {
            'id': self.id,
            'price_range_id': self.price_range_id,
            'build_type_id': self.build_type_id,
        }

# Component models
# GPU Model
class GPU(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    Speed = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'Speed': self.Speed,
            'Price': self.Price,
            'ProductImage': self.ProductImage,
            'purchase_link': self.purchase_link
        }

# CPU Model
class CPU(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String, nullable=False)
    Speed = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'Speed': self.Speed,
            'Price': self.Price,
            'ProductImage': self.ProductImage,
            'purchase_link': self.purchase_link
        }

# Memory Model
class Memory(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    Speed = db.Column(db.Integer, nullable=False)
    Size = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'Speed': self.Speed,
            'Size': self.Size,
            'Price': self.Price,
            'ProductImage': self.ProductImage,
            'purchase_link': self.purchase_link
        }

# MotherBoard Model
class MotherBoard(db.Model, SerializerMixin):
    __tablename__ = 'motherboard'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    Type = db.Column(db.String(50), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'Type': self.Type,
            'Price': self.Price,
            'ProductImage': self.ProductImage,
            'purchase_link': self.purchase_link,
        }

# Storage Model
class Storage(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    Size = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'Size': self.Size,
            'Price': self.Price,
            'ProductImage': self.ProductImage,
            'purchase_link': self.purchase_link,
        }

# PSU Model
class PSU(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    Wattage = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'Wattage': self.Wattage,
            'Price': self.Price,
            'ProductImage': self.ProductImage,
            'purchase_link': self.purchase_link,
        }

# Case Model
class Case(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    Type = db.Column(db.String(50), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    ProductImage = db.Column(db.String(255))
    purchase_link = db.Column(db.String(500))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'Type': self.Type,
            'Price': self.Price,
            'ProductImage': self.ProductImage,
            'purchase_link': self.purchase_link,
        }

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

    def serialize(self):
        return {
            'id': self.id,
            'build_id': self.build_id,
            'gpu_id': self.gpu_id,
            'cpu_id': self.cpu_id,
            'memory_id': self.memory_id,
            'motherboard_id': self.motherboard_id,
            'storage_id': self.storage_id,
            'psu_id': self.psu_id,
            'case_id': self.case_id,
        }

    