import json


def test_app_created(app):
    assert app.name == "api.app"


def test_find_logistic_map_sucess(client):
    response = client.get("/find-map/Koper MOCK network/")
    assert response.status_code == 200


def test_find_logistic_map_fail(client):
    response = client.get("/find-map/wrong MOCK/")
    assert response.status_code == 404


def test_find_all_logistic_maps(client):
    assert client.get("/find-all-map-names/").status_code == 200 


def test_add_logistic_map_sucess(client):    
    mock_request_data = {
        "map_name": "MOCK Teste 3",
        "map_file": [
            ["Carrot", "Apple", 25], 
            ["Orange", "Pinaple", 50],
            ["Apple", "Peach", 75]
        ]
    }
    response = client.post("/add-map/", data=json.dumps(mock_request_data), content_type='application/json') 
    assert response.status_code == 200 


def test_add_logistic_map_fail(client):    
    mock_request_data = {
        "map_name": "Koper MOCK network",
        "map_file": [
            ["Carrot", "Apple", 25], 
            ["Orange", "Pinaple", 50],
            ["Apple", "Peach", 75]
        ]
    }
    response = client.post("/add-map/", data=json.dumps(mock_request_data), content_type='application/json') 
    assert response.status_code == 409


def test_del_logistic_map_sucess(client):
    assert client.delete("/delete-map/MOCK Teste 3/").status_code == 200 


def test_del_logistic_map_fail(client):
    assert client.delete("/delete-map/wrong MOCK/").status_code == 409 


def test_find_best_track(client):
    mock_request_data = {
    "map_name":"Koper MOCK network",
    "start_point":"A",
    "destination_point":"D",
    "vehicle_performance":10.0,
    "fuel_cost":2.5 
    }
    response = client.get("/find-best-track/Koper MOCK network/", data=json.dumps(mock_request_data), content_type='application/json') 
    assert response.status_code == 200 


def test_find_best_track(client):
    mock_request_data = {
    "map_name":"Koper MOCK network",
    "start_point":"A",
    "destination_point":"D",
    "vehicle_performance":10.0,
    "fuel_cost":2.5 
    }
    response = client.get("/find-best-track/wrong MOCK/", data=json.dumps(mock_request_data), content_type='application/json') 
    assert response.status_code == 404
