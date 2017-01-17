from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from common.config import CONF

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONF.connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Dns(db.Model):
    __tablename__ = CONF.table_name
    id = db.Column(db.Integer, primary_key=True)
    zone = db.Column(db.String(255), nullable=False)
    host = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum('MX', 'CNAME', 'NS', 'SOA', 'A', 'PTR', 'TXT', 'AAAA'), nullable=False)
    data = db.Column(db.String(255), default=None)
    ttl = db.Column(db.Integer, default='800')
    view = db.Column(db.String(255), default='any')
    mx_priority = db.Column(db.String(255), default=None)
    refresh = db.Column(db.Integer, default=3600)
    retry = db.Column(db.Integer, default=3600)
    expire = db.Column(db.Integer, default=86400)
    minimum = db.Column(db.Integer, default=3600)
    serial = db.Column(db.Integer, default=0)
    resp_person = db.Column(db.String(64), default=CONF.resp_person)
    primary_ns = db.Column(db.String(64), default=CONF.primary_ns)

    def to_dict(self):
        return {'zone': self.zone, 'host': self.host, 'type': self.type, 'data': self.data, 'view': self.view}

    def __str__(self):
        return '{zone: %s, host: %s, type: %s, data: %s, view: %s}'\
               % (self.zone, self.host, self.type, self.data, self.view)

    __repr__ = __str__
