from flask.ext import restful
from flask.ext.restful import fields, marshal_with
from flask import Blueprint, jsonify
from atlas_core.models import Cat

main_app = Blueprint("main_app", __name__)

cat_fields = {
    'id': fields.String,
    'born_at': fields.Integer,
    'name': fields.String,
}


class CatAPI(restful.Resource):

    @marshal_with(cat_fields)
    def get(self, cat_id):
        """Get a :py:class:`~atlas_core.models.Cat` with the given cat ID.

        :param id: unique ID of the cat
        :type id: int
        :code 404: cat doesn't exist

        """

        q = Cat.query.get_or_404(cat_id)

        return q
