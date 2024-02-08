from setuptools import setup, find_packages

setup_options = dict(
    name="pywebharvest",
    version="0.0.1" ,
    author="Luis Sanfelices",
    author_email="",
    description="package for running web scrapping pipelines",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent", 
    ],
    python_requires= ">=3.6",
    install_requires = [
        "requests>=2.31.0,<3",
        "beautifulsoup4>=4.12.3,<5"
    ],
    packages=find_packages()
)

setup(**setup_options)