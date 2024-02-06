import re

HOST = "http://localhost:9000"
PAGE_HOME = "Sleep%20Aid.html"

product_content_extractor =  [
    {
        "key": "id",
        "tag": "div",
        "selector": {"class": "oct-listers-hits__item"},
        "content_from_attr": "data-insights-object-id",
        "children": [
            {
                "key": "link",
                "tag": "a",
                "selector": {"class": "oct-teaser__title-link"},
                "content_from_attr": "href"
            },
            {
                "key": "title",
                "tag": "h3",
                "selector": {"class": "oct-teaser__title"}
            },
            {
                "key": "price",
                "tag": "p",
                "selector": {"class": "oct-teaser__productPrice"}
            },
            {
                "key": "price_detail",
                "tag": "p",
                "selector": {"class": "oct-teaser__productPriceDetail"}
            },
            {
                "key": "rating",
                "tag": "a",
                "selector": {"class": "oct-reviews__count"},
                "content_from_attr": "aria-label"
            }
        ]
    }
]

short_desc_extractor = [
    {
        "key": "Short_Desc",
        "tag": "p",
        "selector": {"id": re.compile("^product_shortdescription")}
    }
]
