# PyWebHarvest

This package contains a data extraction pipeline designed to extract information from web pages using BeautifulSoup, perform transformations, and load the data into JSON files. It is organized into three main components: loaders, extractors, and runners. 

## Loaders

The loaders module contains classes responsible for loading data into various formats. Currently, it includes a `JsonLoader` class for saving data into JSON files.

### JsonLoader

The `JsonLoader` class provides methods for loading data into a JSON file. It allows customization of the file path, file name, and serialization options.

## Extractors

The extractors module contains classes for extracting content from web pages. Currently, it includes a `SoupExtractor` class that utilizes BeautifulSoup for content extraction.

### SoupExtractor

The `SoupExtractor` class extracts content from web pages based on specified extraction rules. It supports configurable content extraction rules, including tag selectors and attribute extraction.

## Runners

The runners module contains classes for orchestrating the execution of the data extraction pipeline. Currently, it includes a `Pipeline` class for setting up logging and executing the pipeline.

### Pipeline

The `Pipeline` class wraps the data extraction pipeline and sets up logging configurations. It provides a method to start the pipeline execution, which includes extraction, transformation, and loading steps.

## Usage

To use the data extraction pipeline:

1. Instantiate the necessary loader, extractor, and runner classes.
2. Configure the extraction rules and pipeline parameters as needed.
3. Start the pipeline execution using the `start` method of the `Pipeline` class.

Example usage:

```python
from loaders import JsonLoader
from extractors import SoupExtractor
from runners import Pipeline

# Configure extraction rules
urls = ["https://example.com"]
content_extractor = [{"tag": "div", "selector": ".content", "key": "content"}]

# Instantiate classes
def etl_main_function():
    soup_extractor = SoupExtractor(urls=urls, content_extractor=content_extractor)
    json_loader = JsonLoader(path="data", file_name="output.json")
    data = soup_extractor.extract()
    result = json_loader.load(data)



# Start pipeline execution
pipeline = Pipeline(name="WebDataPipeline", etl_main_function=etl_main_function)
pipeline.start()
```