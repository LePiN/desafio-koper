def validate_logistic_json(json_map):    
    if len(json_map) != 2:
        return "Map has the wrong number of arguments."
    elif not "map_name" in json_map or not "map_file" in json_map:
        return "Map does not contain the expected keys."
    elif not isinstance(json_map["map_file"], list):
        return "Map file argument is not a list."
    else: 
        for item in json_map["map_file"]:
            if not isinstance(item, list):
                return "Map file item is not a list."
            elif len(item) != 3:
                return "Map item oversized."
            elif not isinstance(item[2], float):
                return "Distance on the map item is not a decimal number."
    return "Validated"

def validate_best_track_json(json_map):
    if len(json_map) != 5:
        return "Map has the wrong number of arguments."
    elif (not "map_name" in json_map or not "start_point" in json_map or not "destination_point" in json_map or 
    not "vehicle_performance" in json_map or not "fuel_cost" in json_map):
        return "Map does not contain the expected keys."
    elif not isinstance(json_map["vehicle_performance"], float) or not isinstance(json_map["fuel_cost"], float):
        return "Vehicle perfomance ou fuel cost is not a decimal number."
    return "Validated"
