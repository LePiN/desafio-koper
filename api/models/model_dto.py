import networkx as nx


class BestTrack:
    def __init__(
        self, map_name, start_point, destination_point, vehicle_perfomance, fuel_cost
    ):
        self.map_name = map_name
        self.start_point = start_point
        self.destination_point = destination_point
        self.vehicle_perfomance = vehicle_perfomance
        self.fuel_cost = fuel_cost
        self.best_track = None

    def _find_best_track(self, map_content):
        reference_graph = nx.Graph()
        reference_graph.add_weighted_edges_from(map_content)
        best_track_info = nx.single_source_dijkstra(
            reference_graph, self.start_point, self.destination_point
        )
        if best_track_info:
            self.best_track = best_track_info[1]
            self.best_track_distance = float(best_track_info[0])
            self.best_track_cost = (
                self.best_track_distance / self.vehicle_perfomance
            ) * self.fuel_cost

    def __str__(self):
        return (
            f'"map_name": "{self.map_name}", '
            f'"best_track": {self.best_track},'
            f'"best_track_distance": {self.best_track_distance}, '
            f'"best_track_cost": {self.best_track_cost}.'
        )
