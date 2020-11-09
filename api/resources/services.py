import json
from flask import Flask, request, abort, jsonify
from api.models.model_dto import BestTrack
from api.models.model_dao import LogisticMap
from api.extensions.database import db
from api.models.model_validation import validate_logistic_json, validate_best_track_json


def init_app(app: Flask):
    
    @app.route("/find-map/<string:map_name>/", methods=["GET"])
    def find_logistic_map(map_name):
        result = LogisticMap.query.filter_by(name=map_name).first() or abort(404, 
        description=f"Logistic Map {map_name} not found or url incorrect format. Please try a valid entry.")
        return jsonify(result.to_dict())

    
    @app.route("/find-all-map-names/", methods=["GET"])
    def find_all_logistic_map_names():
        result = LogisticMap.query.all() or abort(404, 
        description=f"No maps found in the repository.")              
        result_names = {"map-list": [item.name for item in result]}
        return jsonify(result_names)


    @app.route("/add-map/", methods=["POST"])
    def add_logistic_map():
        data = request.get_json() or abort(409, description=f"{request_map_name}' is not a valid json.")
        status_data = validate_logistic_json(data)
        if status_data == "Validated":
            request_map_name = data["map_name"]
            request_map_file = data["map_file"]
            if LogisticMap.query.filter_by(name=request_map_name).first():
                abort(409, description=f"Logistic Network '{request_map_name}' already exists, add map canceled.")
            else:
                new_map = LogisticMap(name=request_map_name, network=str(request_map_file))
                db.session.add(new_map)
                db.session.commit()
            return f"Logistic Network '{new_map.name}' successfully add."
        else:
            abort(400, description= status_data)

    @app.route("/delete-map/<string:map_name>/", methods=["DELETE"])
    def del_logistic_map(map_name):
        result = LogisticMap.query.filter_by(name=map_name).first() or abort(
            409, description=f"Logistic Network '{map_name}' does not exist, removal canceled.")
        if result:
            db.session.delete(result)
            db.session.commit()
            return f"Logistic Network '{result.name}' successfully removed."

    @app.route("/find-best-track/<string:map_name>/", methods=["GET"])
    def find_best_track(map_name):
        reference_map = LogisticMap.query.filter_by(name=map_name).first() or abort(
            404, description=f"Logistic Map {map_name} not found. Calculate best track aborted.")
        data = request.get_json() or abort(409, description=f"{request_map_name}' is not a valid json.")
        status_data = validate_best_track_json(data)
        if status_data == "Validated":
            start_point = data["start_point"]
            destination_point = data["destination_point"]
            vehicle_performance = data["vehicle_performance"]
            fuel_cost = data["fuel_cost"]
            best_track_result = BestTrack(map_name, start_point, destination_point, vehicle_performance, fuel_cost)
            best_track_result._find_best_track(json.loads(reference_map.network.replace("'", '"')))
            return (jsonify(best_track_result.__dict__))
        else:
            abort(400, description= status_data)
