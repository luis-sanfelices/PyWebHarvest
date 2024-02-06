import requests
from bs4 import BeautifulSoup


def _get_element_content(el, from_attr = None):
    if el is not None:
        return el.get(from_attr) if from_attr else el.get_text(strip=True)
    return None

class SoupExtractor(object):

    def __init__(self, urls, content_extractor):
        self.urls = urls
        self.content_extractor = content_extractor

    def extract(self):
        items = []
        for url in self.urls:
            page = requests.get(url, timeout=120)
            soup = BeautifulSoup(page.text, 'html.parser')

            for extractor in self.content_extractor:
                
                elements = soup.find_all(
                    extractor["tag"], extractor["selector"]
                )
                for element in elements:
                    item = {}
                    item[extractor["key"]] = _get_element_content(
                        element, extractor.get("content_from_attr"))

                    children_extractors = extractor.get("children")

                    if children_extractors is not None:
                        for child_extractor in children_extractors:
                            finded_element = element.find(
                                    child_extractor["tag"], child_extractor["selector"]
                                )
                            item[child_extractor["key"]] = _get_element_content(
                                finded_element, child_extractor.get("content_from_attr"))

                    items.append(item)

        return items
