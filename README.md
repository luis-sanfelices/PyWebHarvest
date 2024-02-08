# Data engineering task

## Project structure

Project Structure
This project is structured into three main folders, each serving a distinct purpose. While segregating these folders into separate repositories might offer better organization, for the ease of review, they have been consolidated within this repository.

### pywebharvest_ops

This folder contains all the things needed for setting up the environment. Currently, it contains a dockerfile for serving a web clone on localhost using nginx.

### pywebharvest_tools

This folder contains tools designed to extract information from web pages, enhancing code reusability and efficiency.

### pywebharvest_pipelines

This folder contains the data extraction pipelines.


## Seting up the environment

**_NOTE:_** The following commands have been designed for use in PowerShell. Some adjustments may be necessary for Unix systems.

### Prerequisites:
- Python >=3.6
- Docker

### Setup:
Due to limitations with the size of the provided zip file and the Google Drive API, it is not possible to directly build the Docker image for serving a web app on localhost using the provided Google Drive link. Instead, please follow these steps:

1. Download the zip file from the provided Google Drive link.
2. Unzip the contents of the zip file.
3. Copy the extracted content into the `pywebharvest_ops/Sleep_aid_clone` folder.

Once the zip file has been copied into the ops folder, execute the following commands to build the image and deploy the web clone locally:

```docker build -f .\pywebharvest_ops\Dockerfile . -t web-clone-server ```
```docker run -it --rm -d -p 9000:80 --name web-clone web-clone-server```

As the pywebharvest_tools have been developed as a package, execute the installation command:

```pip install .\pywebharvest_tools\```

Feel free to reach out if you encounter any issues during the setup process.

## Running pipeline and tests

### Pipeline 

For running the pipeline, preferably move to the pipeline folder and use the python command:

```cd  .\pywebhaverst_pipelines\src\boots_web_harvesting\```

```python pipeline.py``

You can still run the pipeline from the root, but the output file will be stored there.

### Tests

Since pywebharvest_pipelines and pywebharvest_tools have been developed as separate modules, tests have to be run inside their respective folders to ensure correct Python imports.

#### Pipeline tests
From the root:
```cd  .\pywebhaverst_pipelines\```
```pytest .\tests\```

#### Package tests
From the root:
```cd  .\pywebhaverst_tools\```
```pytest .\tests\```


### Stop Web clone container

```docker stop web-clone```
```docker rmi $(docker images --format "{{.Repository}}:{{.Tag}}"|findstr "web-clone-server")```


