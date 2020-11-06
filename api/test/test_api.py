def test_app_created(app):
    assert app.name == "api.app"

def test_find_logistic_map(client):
    assert client.get("/find-map/Koper MOCK network/").status_code == 404 
