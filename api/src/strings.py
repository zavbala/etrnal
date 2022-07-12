DRIBBBLE_CATEGORIES = (
    "animation",
    "branding",
    "illustration",
    "mobile",
    "print",
    "product-design",
    "typography",
    "web-design",
)


BEHANCE_CATEGORIES = ("projects", "images", "prototypes")

HTML_SOURCES = {
    "dribbble": {
        "payload": 1,
        "base_url": "https://dribbble.com",
        "path": "/shots/popular",
        "categories": DRIBBBLE_CATEGORIES,
        "relative": True,
        "schema": (
            "img::attr(src)",
            "a.shot-thumbnail-link::attr(href)",
            "a.hoverable::attr(href)",
        ),
        "content": {
            "layout": "ol.shots-grid",
            "children": "li.shot-thumbnail-container",
        },
    },
}

GRAPHQL_SOURCES = {
    "behance": {
        "url": "https://www.behance.net/v3/graphql",
        "categories": BEHANCE_CATEGORIES,
        "headers": {
            "Cookie": "bcp=6f065de4-c22f-4d92-ab08-d04f462472dd",
            "X-BCP": "6f065de4-c22f-4d92-ab08-d04f462472dd",
            "X-Requested-With": "XMLHttpRequest",
        },
        "variables": {"filter": {}, "first": 48, "after": "NDk="},
        "schema": ("covers.size_original.url", "url", "owners.0.url"),
    },
}

BASIC_SCHEMA = {"cover": "", "source": "", "owner": ""}

JSON_CONTENT = {"Content-Type": "application/json"}

USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
}

BASIC_ACCEPT = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

LANGUAGE = {"Accept-Language": "en"}
