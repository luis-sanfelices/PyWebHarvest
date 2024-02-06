import re
import pd
import requests
from config import config
from pywebharvest.runners import Pipeline
from pywebharvest.extractors import SoupExtractor


def _extract():
    extractor = SoupExtractor(
        urls=[f"{config.HOST}/{config.PAGE_HOME}"],
        content_extractor=config.product_content_extractor
    )
    products = extractor.extract()

    for product in products:
        product_url = f"{config.HOST}{product['link'][1:]}"
        product_page = requests.head(product_url, timeout=60)
        product["page_size"] = product_page.headers["Content-Length"]
        product_extractor = SoupExtractor(
            urls=[product_url],
            content_extractor= config.short_desc_extractor
        )
        val = product_extractor.extract()
        product["Short_Desc"] = val[0]["Short_Desc"] if val else None

    return pd.Dataframe(products)


def _transform(df):
    return df


def _load(df):
    return df


def etl_main_function():


    df = _extract()

    df = _transform(df)

    df = _load(df)

    return "COMPLETED"


# pipeline runner
pipeline = Pipeline(
    name="Boots_web_harvesting",
    etl_main_function=etl_main_function,
)

pipeline.start()