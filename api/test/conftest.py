import pytest
from api.app import create_app
from api.extensions.commands import populate_db
from api.extensions.database import db

@pytest.fixture(scope="module")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        db.create_all(app=app)
        populate_db()
        yield app
        db.drop_all(app=app)
