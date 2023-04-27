import json
import random

from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args

from src import settings, utils

config = settings.Config()
blueprint = Blueprint("items", __name__)


@blueprint.route("/api/items")
@use_args(
    {"page": fields.Int(), "page_id": fields.Str(), "providers": fields.Str()},
    location="query",
)
def get_items(args):
    """Get feed / popular items"""

    data = []
    page = args["page"]
    page_id = args["page_id"]

    try:
        providers = args["providers"].split(",")
    except KeyError:
        providers = "all"

    with open(config.APP_DIR / "data/Sources.json", "r", encoding="UTF-8") as file:
        plain = file.read()
        sources = json.loads(plain)

    for key, source in sources.items():
        records = []

        if source["type"] == "html":

            url = source["base_url"] + source["feed"]
            records = utils.get_records_from_html(
                url=url, params={"page": page * 1}, **source
            )

        if source["type"] == "gql":

            source["variables"]["after"] = page_id
            next_page, records = utils.get_records_from_gql(
                {"provider": key, "kind": "feed"}, source
            )

        data.extend(records)

    random.shuffle(data)

    return jsonify(page_id=next_page, records=data)
