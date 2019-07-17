from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()


class RevendaSchema(ma.Schema):
    id = fields.Str(load_only=True)
    number = fields.Integer(required=True, error_messages={"required": "number is required."})
    name = fields.Str(required=True, error_messages={"required": "number is required."})


class PostgresSchema(ma.Schema):
    id = fields.Str(load_only=True)
    url = fields.Str()
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    database = fields.Str(required=True)


class ActiveMQSchema(ma.Schema):
    id = fields.Str(load_only=True)
    port = fields.Int(required=True)
    username = fields.Str()
    password = fields.Str()


class PortalWebSchema(ma.Schema):
    id = fields.Str(load_only=True)
    api = fields.Str(required=True)
    host = fields.Str(required=True)
    port = fields.Int(required=True)
    revenda = fields.Nested(RevendaSchema)


class PortalApiSchema(ma.Schema):
    id = fields.Str(load_only=True)
    port = fields.Integer(required=True)
    postgres = fields.Nested(PostgresSchema)
    revenda = fields.Nested(RevendaSchema)


def configure(app):
    ma.init_app(app)
