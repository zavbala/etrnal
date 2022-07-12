# import os
import random
import re
import uuid

import httpx
from bs4 import BeautifulSoup
from furl import furl
from glom import GlomError, glom
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
# from instagram_scraper import InstagramScraper
from parsel import Selector

from . import strings
from .settings import Config

# credentials = {
#     "login_user": os.environ.get("IG_USER"),
#     "login_pass": os.environ.get("IG_PASS"),
# }

# instagram = InstagramScraper(**credentials)
# instagram.authenticate_with_login()


# def get_lastest_posts_from_user():
#     """Get shots from instagram"""

#     user = get_random_instagram_user()
#     shared_data = instagram.get_shared_data_userinfo(username=user)

#     for item in instagram.query_media_gen(shared_data):
#         print(item)

#     return ""


def clean_image_source(link: str):
    """Remove default resizer"""

    return re.sub("[?](.*)", "", link)


def format_schema(values: tuple):
    """Define main schema"""

    return dict(zip(strings.BASIC_SCHEMA, values))


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


def get_records_from_gql(schema: str, next_page: str) -> tuple[str, dict]:
    """Get shots from graphql endpoints"""

    try:
        with open(
            Config.APP_DIR / f"schemas/{schema}.gql", "r", encoding="utf-8"
        ) as file:
            my_schema = file.read()
    except FileNotFoundError:
        pass

    try:
        source = strings.GRAPHQL_SOURCES[schema]
    except KeyError:
        pass

    headers = {**strings.JSON_CONTENT, **strings.USER_AGENT, **source["headers"]}
    transport = RequestsHTTPTransport(url=source["url"], headers=headers, retries=3)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    with client as session:
        # assert client.schema is not None
        query = gql(my_schema)
        args = {**source["variables"], **({"after": next_page} if next_page else {})}
        result = session.execute(query, variable_values=args)

    entry = result.get("search")
    schema = format_schema(source["schema"])
    nodes = []

    for node in entry["nodes"]:
        node = get_schema_from_json(node, schema)
        node["_id"] = str(uuid.uuid4())

        nodes.append(node)

    return entry["pageInfo"]["endCursor"], nodes


def get_records_from_html(page: int, **kwargs):
    """Get daily shots"""

    f = furl(kwargs["base_url"])

    headers = {
        **strings.USER_AGENT,
        **strings.LANGUAGE,
    }

    with httpx.Client(base_url=f.url, headers=headers) as session:
        response = session.get(kwargs["path"], params={"page": page})

    soup = BeautifulSoup(response.text, "lxml")
    schema = format_schema(kwargs["schema"])
    entry = kwargs["content"]

    for item in soup.select(entry["children"]):
        shot = get_schema_from_soup(schema, item)

        try:
            if kwargs["relative"]:
                shot["owner"] = f.url + shot["owner"]
                shot["source"] = f.url + shot["source"]
        except KeyError:
            pass

        shot["cover"] = clean_image_source(shot["cover"])

        yield {"_id": str(uuid.uuid4()), **shot}
