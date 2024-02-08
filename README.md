


## Prerequisites:
- Python >=3.6
- Docker

## Setup:
Due to limitations with the size of the provided zip file and the Google Drive API, it is not possible to directly build the Docker image for serving a web app on localhost using the provided Google Drive link. Instead, please follow these steps:

1. Download the zip file from the provided Google Drive link.
2. Unzip the contents of the zip file.
3. Copy the extracted content into the `pywebharvest_ops/Sleep_aid_clone` folder.


docker run -it --rm -d -p 9000:80 --name web-clone web-clone-server

docker build -f .\pywebharvest_ops\Dockerfile . -t web-clone-server 

pip install .\pywebharvest_tools\

pytest .\tests\