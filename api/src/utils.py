import random
import re
import uuid

import httpx
from bs4 import BeautifulSoup
from furl import furl
from glom import GlomError, glom
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from parsel import Selector

from . import strings
from .settings import Config


def clean_image_source(link: str):
    """Remove default resizer"""

    return re.sub("[?](.*)", "", link)


def get_schema_from_json(item: dict, schema: dict) -> dict:
    """Return a schema with their values on base to selectors"""

    _dict = {}

    for key, value in schema.items():
        try:
            _dict[key] = glom(item, value)
        except (GlomError):
            pass

    return _dict


def get_random_instagram_user():
    """Get random instagram user from the list data/users.txt"""

    with open(Config.APP_DIR / "data/users.txt", "r", encoding="UTF-8") as file:
        users = file.readlines()

    return random.choice(users)


def get_schema_from_soup(selectors: dict, html: str) -> dict:
    """Return schema from html doc on base to selectors"""

    schema = {}
    selector = Selector(f""""<html><body>{html}</body></html>""")

    for key, value in selectors.items():
        schema[key] = selector.css(value).get("")

    return schema


def get_records_from_gql(props: dict, source: dict) -> tuple[str, dict]:
    """Get records from graphql endpoints"""

    provider, kind = props.values()

    url = source["url"]
    entry = source["entry"]
    schema = source["schema"]
    variables = source["variables"]

    try:
        with open(
            Config.APP_DIR / f"schemas/{provider}/{kind}.gql", "r", encoding="utf-8"
        ) as file:
            query = file.read()
    except FileNotFoundError:
        return "", {}

    headers = {**strings.JSON_CONTENT, **strings.USER_AGENT, **source["headers"]}
    transport = RequestsHTTPTransport(url=url, headers=headers, retries=3)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    with client as session:
        query = gql(query)
        result = session.execute(query, variable_values={**variables})

    data = glom(result, entry)

    for index, node in enumerate(data["nodes"]):
        node = get_schema_from_json(node, schema)
        node["_id"] = str(uuid.uuid4())
        data["nodes"][index] = node

    return data.values()


def get_records_from_html(**kwargs):
    """Get records from html endpoints"""

    entity = furl(kwargs["url"])

    headers = {
        **strings.LANGUAGE,
        **strings.USER_AGENT,
    }

    try:
        params = kwargs["params"]
    except KeyError:
        params = {}

    with httpx.Client(headers=headers) as session:
        response = session.get(url=kwargs["url"], params=params)

    soup = BeautifulSoup(response.text, "lxml")

    schema = kwargs["schema"]
    entry = kwargs["content"]

    for item in soup.select(entry["children"]):
        record = get_schema_from_soup(schema, item)

        try:
            if kwargs["relative"]:
                record["owner"] = entity.origin + record["owner"]
                record["source"] = entity.origin + record["source"]
        except KeyError:
            pass

        temp_id = str(uuid.uuid4())
        record["cover"] = clean_image_source(record["cover"])

        yield {"_id": temp_id, **record}
