import json
import pickle
import sqlalchemy_utils
import networkx as nx
from flask import Flask, abort, jsonify, request
from blueprint import mock_database
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


app = Flask(__name__)
#sqlalchemy_utils.functions.drop_database('sqlite:////teste.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class LogisticNetwork(db.Model, SerializerMixin):
    __tablename__ = 'logistic_network'
    network_name = db.Column(db.String(100), primary_key=True)
    network_file = db.Column(db.Text, nullable=False)

    def __init__(self, network_name, network_file):
        self.network_name = network_name
        self.network_file = network_file
#db.create_all()

@app.route('/')
def entry_point():
    return 'Hello World!'

@app.route('/find-map/<string:network_name>/', methods=['GET'])
def find_logistic_network(network_name):
    network_result = LogisticNetwork.query.filter_by(network_name=network_name).first() or abort(
        404, description=f'Logistic Network {network_name} not found. Please try a valid option.') 
    network_result.network_file = json.loads(network_result.network_file)
    print(network_result.network_file)
    print(json.dumps(network_result.to_dict()))
    #return jsonify(network_result.to_dict())
    return json.dumps(network_result.to_dict())

@app.route('/add-map/', methods=['POST'])
def add_logistic_network():
    data = request.get_json()
    request_network_name = data['network_name']
    request_network_file = data['network_file'] 
    if LogisticNetwork.query.filter_by(network_name=request_network_name).first():
        abort(409, description=f'Logistic Network {request_network_name} already exists, inclusion canceled.')
    else:        
        new_network = LogisticNetwork(network_name=request_network_name, network_file=json.dumps(request_network_file))
        db.session.add(new_network)
        db.session.commit()
    return f'Malha {new_network.network_name} inserida na base.'

@app.route('/delete-map/<string:network_name>/', methods=['DELETE'])
def del_logistic_network(network_name):
    network_result = LogisticNetwork.query.filter_by(network_name=network_name).first() or abort(409, description=f'Network {network_name} does not exist, removal canceled.')
    if network_result:
        db.session.delete(network_result)
        db.session.commit()
        return f'Malha {network_result.network_name} excluida da base.'

@app.route('/find/<string:logistic_network_name>/<string:start_point>/<string:destination_point>/<vehicle_performance>/<fuel_cost>/')
def get_best_track(logistic_network_name, start_point, destination_point, vehicle_performance, fuel_cost):
    logistic_network = get_logistic_network(logistic_network_name)
    best_track = calculate_best_track(logistic_network, start_point, destination_point)
    best_track_cost = calculate_track_cost(best_track, float(vehicle_performance), float(fuel_cost))
    return prepare_best_track_infos(logistic_network_name, start_point, destination_point, vehicle_performance, fuel_cost, best_track, best_track_cost)

def get_logistic_network(logistic_network_name):
    return  mock_database.malha_lojistica[logistic_network_name]

def calculate_best_track(logistic_network, start_point, destination_point):
    tracks_graph = nx.Graph()    
    tracks_graph.add_weighted_edges_from(logistic_network)    
    return nx.single_source_dijkstra(tracks_graph, "A", "D")

def calculate_track_cost(best_track, vehicle_performance, fuel_cost):
    return (best_track[0] / vehicle_performance) * fuel_cost

def prepare_best_track_infos(logistic_network_name, start_point, destination_point, vehicle_performance, fuel_cost, best_track, best_track_cost):  

    return jsonify({
        'Logistic network name': logistic_network_name,
        'Start point': start_point,
        'Destination point': destination_point,
        'Vehicle performance': vehicle_performance,
        'Fuel cost': fuel_cost,
        'Best track': best_track[1],
        'Best track cost': best_track_cost
    })   

if __name__ == '__main__':
    #db.create_all()
    app.run(use_reloader=True)
    #db.drop_all()
    
    