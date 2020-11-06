import json
from flask import Flask, request, abort
from api.models.model_dto import BestTrack
from api.models.model_dao import LogisticMap
from api.extensions.database import db


def init_app(app: Flask):
    
    @app.route("/find-map/<string:map_name>/", methods=["GET"])
    def find_logistic_map(map_name):
        result = LogisticMap.query.filter_by(name=map_name).first() or abort(
            404,
            description=f"Logistic Map {map_name} not found. Please try a valid option.",
        )
        result.network = json.loads(result.network)
        return json.dumps(result.to_dict())

    @app.route("/add-map/", methods=["POST"])
    def add_logistic_map():
        data = request.get_json()
        request_map_name = data["map_name"]
        request_map_file = data["map_file"]
        if LogisticMap.query.filter_by(name=request_map_name).first():
            abort(
                409,
                description=f"Logistic Network {request_map_name} already exists, inclusion canceled.",
            )
        else:
            new_map = LogisticMap(
                name=request_map_name, network=json.dumps(request_map_file)
            )
            db.session.add(new_map)
            db.session.commit()
        return f"Malha {new_map.name} inserida na base."

    @app.route("/delete-map/<string:map_name>/", methods=["DELETE"])
    def del_logistic_map(map_name):
        result = LogisticMap.query.filter_by(name=map_name).first() or abort(
            409, description=f"Network {network_name} does not exist, removal canceled."
        )
        if result:
            db.session.delete(result)
            db.session.commit()
            return f"Malha {result.name} excluida da base."

    @app.route("/find-best-track/<string:map_name>/", methods=["GET"])
    def find_best_track(map_name):
        reference_map = LogisticMap.query.filter_by(name=map_name).first() or abort(
            404,
            description=f"Logistic Map {map_name} not found. Calculate best track aborted.",
        )
        data = request.get_json()
        start_point = data["start_point"]
        destination_point = data["destination_point"]
        vehicle_performance = float(data["vehicle_performance"])
        fuel_cost = float(data["fuel_cost"])
        resultado_best_track = BestTrack(
            map_name, start_point, destination_point, vehicle_performance, fuel_cost
        )
        resultado_best_track._find_best_track(json.loads(reference_map.network))
        return json.dumps(resultado_best_track.__dict__)
