import pytest
from unittest.mock import Mock, patch
from pywebharvest.extractors import SoupExtractor

@pytest.fixture
def mock_requests_get():
    with patch("requests.get") as mock_get:
        yield mock_get

def test_extract(mock_requests_get):
    # Mocked data
    urls = ["http://example.com"]
    content_extractor = [{
        "tag": "div",
        "selector": {"class": "content"},
        "key": "content",
        "content_from_attr": "id",
        "children": [
            {"tag": "h1", "selector": {"class": "title"}, "key": "title", "content_from_attr": None},
            {"tag": "p", "selector": {"class": "description"}, "key": "description", "content_from_attr": None}
        ]
    }]

    mocked_response = Mock()
    mocked_response.text = """
        <html>
            <body>
                <div class="content" id="1">
                    <h1 class="title">Title</h1>
                    <p class="description">Description</p>
                </div>
            </body>
        </html>
    """
    mock_requests_get.return_value = mocked_response

    # Call the SoupExtractor
    extractor = SoupExtractor(urls=urls, content_extractor=content_extractor)
    extracted_data = extractor.extract()

    # Assertions
    assert len(extracted_data) == 1
    assert extracted_data[0]["content"] == "1"
    assert extracted_data[0]["title"] == "Title"
    assert extracted_data[0]["description"] == "Description"
    mock_requests_get.assert_called_once_with("http://example.com", timeout=120)