from api.extensions.database import db
from api.models.model_dao import LogisticMap


def create_db():
    db.create_all()


def drop_db():
    db.drop_all()


def populate_db():
    data = [
        LogisticMap(
            name="Koper MOCK network",
            network=str(
                [
                    ["A", "B", 10.0],
                    ["B", "C", 25.0],
                    ["C", "D", 30.0],
                    ["D", "E", 30.0],
                    ["A", "C", 50.0],
                    ["B", "D", 15.0],
                    ["C", "E", 45.0],
                    ["B", "E", 50.0],
                    ["A", "D", 90.0],
                ]
            ),
        ),
        LogisticMap(
            name="Koper Second Map",
            network=str(
                [
                    ["Red", "Blue", 20.0],
                    ["Green", "Yellow", 50.0],
                    ["Brown", "Blue", 40.0],
                    ["Orange", "Red", 25.0],
                    ["Pink", "Green", 50.0],
                ]
            ),
        ),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return LogisticMap.query.all()


def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
