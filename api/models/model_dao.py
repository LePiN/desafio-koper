from sqlalchemy_serializer import SerializerMixin

from api.extensions.database import db


class LogisticMap(db.Model, SerializerMixin):
    __tablename__ = 'logistic_map'
    name = db.Column(db.String(100), primary_key=True)
    network = db.Column(db.Text, nullable=False)

    def __init__(self, name, network):
        self.name = name
        self.network = network
    
    def __str__(self):
        return '{"map_name": %, "map_file": %}' % (self.name, self.network.replace("'", '"'))
