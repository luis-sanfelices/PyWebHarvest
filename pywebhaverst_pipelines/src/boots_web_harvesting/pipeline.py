import os
import logging
import numpy as np
import pandas as pd
import requests as req
import pipeline_config as cfg
from pywebharvest.runners import Pipeline
from pywebharvest.extractors import SoupExtractor
from pywebharvest.loaders import JsonLoader

TIMEOUT = 60
KB_TO_BYTES = 1024


def extract_data():
    """Extract product data from URLs"""
    extractor = SoupExtractor(
        urls=[f"{cfg.HOST}/{cfg.PAGE_HOME}"],
        content_extractor=cfg.product_content_extractor
    )
    products = extractor.extract()
    for product in products:
        product_url = f"{cfg.HOST}{product['Link'][1:]}"
        try:
            product_page = req.head(product_url, timeout=TIMEOUT)
            product["Page_Size"] = product_page.headers.get("Content-Length")
            product_extractor = SoupExtractor(
                urls=[product_url],
                content_extractor=cfg.short_desc_extractor
            )
            val = product_extractor.extract()
            product["Short_Desc"] = val[0]["Short_Desc"] if val else None
        except (req.ConnectionError, req.Timeout, req.HTTPError) as e:
            logging.error(f"Error occurred while extracting data: {e}")
    return products


def transform_data(products):
    """Transform extracted data"""
    try:
        # Clean and build dataset
        df = pd.DataFrame(products)
        df["Price"] = df["Price_Str"].str.replace(r"[^\d\.]", "", regex=True).astype(float)
        df["Price_Unit"] = df["Price_Str"].str.replace(r"[\Â\d\.]", "", regex=True)
        df["Page_Size"] = (pd.to_numeric(df["Page_Size"], errors="coerce") / KB_TO_BYTES).astype(int)
        df["Rating"] = pd.to_numeric(df["Rating"].str.split().str.get(0), errors='coerce')
        df.replace({np.nan: None}, inplace=True)
        output_df = df[cfg.output_columns]
        median = output_df["Price"].median()
        # Transform to expected dict
        output_dict = {
            "Products": output_df.to_dict('records'),
            "Median": median
        }

    except Exception as e:
        raise Exception(f"Data is malformed, transformation failed with error: {e}") from e
    
    return output_dict


def load_data(data) -> None:
    """Save transformed data to a JSON file"""
    file_path = os.path.join(os.getcwd(), cfg.output_path)
    load_options = {
        "file_options": { 
            "encoding": "utf8"
        },
        "json_options": {
            "ensure_ascii": False
        }
    }
    json_loader = JsonLoader(
        file_path,
        file_name=cfg.output_file_name,
        **load_options
    )
    return json_loader.load(data)


def etl_main_function() -> str:
    """ ETL main function """
    products = extract_data()

    transformed_products = transform_data(products)

    file = load_data(transformed_products)

    return f"Data extracted succesfully and stored into the next file: '{file}'"


if __name__ == "__main__":
    pipeline = Pipeline(
        name="Boots_web_harvesting",
        etl_main_function=etl_main_function,
    )

    pipeline.start()
