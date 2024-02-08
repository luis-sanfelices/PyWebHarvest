import sys
sys.path.append("src/boots_web_harvesting")
import pytest
from mock import patch
from pipeline import extract_data, transform_data, load_data


@pytest.fixture
def sample_extracted_data():
    return [
        {"Link": "/product/1", "Title": "Product 1", "Price_Str": "$10", "Rating": "4.5 stars", "Short_Desc": "product 1"},
        {"Link": "/product/2", "Title": "Product 2", "Price_Str": "$20", "Rating": "null stars", "Short_Desc": "product 2"}
    ]

@pytest.fixture
def sample_data_to_transform():
    return [
        {"Link": "/product/1", "Title": "Product 1", "Price_Str": "$10", "Rating": "4.5 stars", "Short_Desc": "product 1", "Page_Size":"1024"},
        {"Link": "/product/2", "Title": "Product 2", "Price_Str": "$20", "Rating": "null stars", "Short_Desc": "product 2", "Page_Size":"1024"},
        {"Link": "/product/3", "Title": "Product 3", "Price_Str": "$19", "Rating": "null stars", "Short_Desc": "product 3", "Page_Size":"1024"}
    ]

@patch("requests.head")
@patch("pywebharvest.extractors.SoupExtractor.extract")
def test_extract_data(mock_soup_extractor, mock_head, sample_extracted_data):
    mock_head.return_value.headers = {"Content-Length": "1024"}
    mock_soup_extractor.return_value = sample_extracted_data

    extracted_data = extract_data()

    assert extracted_data == sample_extracted_data
    assert len(extracted_data) == 2
    assert extracted_data[0]["Page_Size"] == "1024"


def test_transform_data(sample_data_to_transform):
    transformed_data = transform_data(sample_data_to_transform)

    assert len(transformed_data["Products"]) == 3
    assert transformed_data["Median"] == 19.0


@patch("pywebharvest.loaders.JsonLoader.load")
def test_load_data(mock_json_loader):
    data = {"key": "value"}
    mock_json_loader.return_value = "output/products.json"
    value = load_data(data)

    mock_json_loader.assert_called_once_with(data)
    assert mock_json_loader.return_value == value
