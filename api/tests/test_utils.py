import pytest

from src import strings, utils
from src.settings import Config


def test_pick_random_user():
    my_user = utils.get_random_instagram_user()

    with open(Config.APP_DIR / "data/users.txt", "r", encoding="UTF-8") as file:
        users = file.readlines()

    assert users.count(my_user)


def test_get_shots_from_html():
    dribbble = strings.HTML_SOURCES["dribbble"]
    shots = list(utils.get_records_from_html(page=1, **dribbble))

    assert len(shots) == 24


# def test_posts_from_instagram():
#     posts = utils.get_lastest_posts_from_user()
#     print(posts)

#     assert True


def test_get_shots_from_graphql():
    next_page, nodes = utils.get_records_from_gql("behance", "")
    assert len(nodes) == 48


docs = [
    (
        {
            "username": "h1::text",
        },
        """
        <h1>John Doe</h1>
        """,
        {"username": "John Doe"},
    ),
    (
        {"source": "img::attr(src)", "author": "span::text"},
        """
        <img alt="ALT TEXT" src="https://dummy.source.io/file/my_image.png" />
        <span>John Doe</span>
        """,
        {"source": "https://dummy.source.io/file/my_image.png", "author": "John Doe"},
    ),
]


@pytest.mark.parametrize("selectors, tag, expected", docs)
def test_get_schema_from_soup(selectors, tag, expected):
    assert expected == utils.get_schema_from_soup(selectors, tag)


schemas = [
    (
        {"user": {"name": "John Doe"}},
        {"username": "user.name"},
        {"username": "John Doe"},
    ),
]


@pytest.mark.parametrize("item, schema, expected", schemas)
def test_get_schema_from_json(item, schema, expected):
    assert expected == utils.get_schema_from_json(item, schema)


images = [
    (
        "https://cdn.dribbble.com/media/dummy.png?compress=1&resize=400x300",
        "https://cdn.dribbble.com/media/dummy.png",
    ),
]


@pytest.mark.parametrize("link, expected", images)
def test_cleaning_image_sources(link, expected):
    assert expected == utils.clean_image_source(link)
