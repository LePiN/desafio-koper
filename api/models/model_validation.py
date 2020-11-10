from math import inf


def validate_logistic_json(json_map):
    if len(json_map) != 2:
        return "Map has the wrong number of arguments."
    elif "map_name" not in json_map or "map_file" not in json_map:
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
    elif (
        ("map_name" not in json_map)
        or ("start_point" not in json_map)
        or ("destination_point" not in json_map)
        or ("vehicle_performance" not in json_map)
        or ("fuel_cost" not in json_map)
    ):
        return "Map does not contain the expected keys."
    elif not isinstance(json_map["vehicle_performance"], float) or not isinstance(
        json_map["fuel_cost"], float
    ):
        return "Vehicle perfomance ou fuel cost is not a decimal number."
    return "Validated"


def create_graph(map):
    map_points = set()
    for item in map:
        map_points.add(item[0])
        map_points.add(item[1])
    graph = {}
    for point in map_points:
        combination = {}
        for item in map:
            if point == item[0]:
                combination[item[1]] = item[2]
        graph[point] = combination
    return graph


def calculate_best_route(map, start, goal, vehicle_perfomance, fuel_cost):
    graph = create_graph(map)
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = inf
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        for edge, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[edge]:
                shortest_distance[edge] = weight + shortest_distance[minNode]
                predecessor[edge] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        best_track_cost = (shortest_distance[goal] / vehicle_perfomance) * fuel_cost
        return shortest_distance[goal], str(path), best_track_cost
