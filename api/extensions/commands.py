import click
from api.extensions.database import db
from api.models.model_dao import LogisticMap


def create_db():
    db.create_all()


def drop_db():
    db.drop_all()


def populate_db():
    data = [        
        LogisticMap(name="Koper MOCK network",
                    network= str([
                        ["A", "B", 10], 
                        ["B", "C", 25],
                        ["C", "D", 30],
                        ["D", "E", 30],
                        ["A", "C", 50],
                        ["B", "D", 15],
                        ["C", "E", 45],
                        ["B", "E", 50],
                        ["A", "D", 90]
                    ])
        ),
        LogisticMap(name="Koper Second Map",
                    network= str([
                        ["Red", "Blue", 20], 
                        ["Green", "Yellow", 50],
                        ["Brown", "Blue", 40],
                        ["Orange", "Red", 25],
                        ["Pink", "Green", 50]
                    ])
        )
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return LogisticMap.query.all()


def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

