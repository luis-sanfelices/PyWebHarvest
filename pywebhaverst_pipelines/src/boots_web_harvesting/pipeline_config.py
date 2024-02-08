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
                "key": "Link",
                "tag": "a",
                "selector": {"class": "oct-teaser__title-link"},
                "content_from_attr": "href"
            },
            {
                "key": "Title",
                "tag": "h3",
                "selector": {"class": "oct-teaser__title"}
            },
            {
                "key": "Price_Str",
                "tag": "p",
                "selector": {"class": "oct-teaser__productPrice"}
            },
            {
                "key": "Rating",
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

output_columns = ["Title", "Price", "Price_Unit", "Short_Desc", "Rating", "Page_Size"]

output_path = "output"
output_file_name = "products.json"