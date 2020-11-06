import click
from api.extensions.database import db


def create_db():
    db.create_all()


def drop_db():
    db.drop_all()


# def populate_db():
#     data = [
#         Product(
#             id=1, name="Ciabatta", price="10", description="Italian Bread"
#         ),
#         Product(id=2, name="Baguete", price="15", description="French Bread"),
#         Product(id=3, name="Pretzel", price="20", description="German Bread"),
#     ]
#     db.session.bulk_save_objects(data)
#     db.session.commit()
#     return Product.query.all()


def init_app(app):
    # add multiple commands in a bulk
    # for command in [create_db, drop_db, populate_db]:
    for command in [create_db, drop_db]:
        app.cli.add_command(app.cli.command()(command))

