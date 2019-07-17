from flask import Blueprint, request

from model.serializer import RevendaSchema

bp_revenda = Blueprint('revenda', __name__, url_prefix="/revenda")


@bp_revenda.route("/register", methods=['POST'])
def register():
    revenda = RevendaSchema()
    teste, error = revenda.load(request.json)
    if error:
        print(error)
        return error, 404
    return revenda.jsonify(teste), 201


@bp_revenda.route("/", methods=['GET'])
def getall():
    ...
