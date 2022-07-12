import random

from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args

from src import strings, utils

blueprint = Blueprint("items", __name__)


@blueprint.route("/api/items")
@use_args({"page": fields.Int(), "page_id": fields.Str()}, location="query")
def get_items(args):
    """Mix"""

    data = []
    dribbble = strings.HTML_SOURCES["dribbble"]

    n_page = args["page"] * dribbble["payload"]
    shots = list(utils.get_records_from_html(n_page, **dribbble))
    data.extend(shots)

    next_page, nodes = utils.get_records_from_gql("behance", args["page_id"])
    data.extend(nodes)

    random.shuffle(data)

    return jsonify(page_id=next_page, records=data)
