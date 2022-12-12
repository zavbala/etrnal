import json
import random

from flask import Blueprint, jsonify
from src import settings, utils
from webargs import fields
from webargs.flaskparser import use_args

config = settings.Config()
blueprint = Blueprint("search", __name__)


@blueprint.route("/api/search")
@use_args(
    {"query": fields.Str(), "category": fields.Str(), "providers": fields.Str()},
    location="query",
)
def search(args):
    """Search"""

    query = args["query"]

    try:
        providers = args["providers"].split(",")
    except KeyError:
        providers = "all"

    try:
        category = args["category"]
    except KeyError:
        category = None

    with open(config.APP_DIR / "data/Sources.json", "r", encoding="UTF-8") as file:
        plain = file.read()
        sources = json.loads(plain)

    dribbble = sources["dribbble"]

    dribbble_shots = utils.get_records_from_html(
        url=dribbble["base_url"] + f"/search/{query}", **dribbble
    )

    data = list(dribbble_shots)

    return jsonify(data)
