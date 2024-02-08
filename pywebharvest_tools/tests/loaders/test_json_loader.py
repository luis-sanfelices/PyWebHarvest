import os
import json
from unittest.mock import mock_open, patch
import pytest
from pywebharvest.loaders import JsonLoader

@pytest.fixture
def json_data():
    return {"key": "value"}

def test_load_data(tmpdir, json_data):
    # Mocked data and file path
    path = tmpdir.mkdir("test_dir")
    file_name = "test.json"

    # Call the JsonLoader
    loader = JsonLoader(path=str(path), file_name=file_name)
    loaded_file = loader.load(json_data)

    # Assertions
    assert os.path.isfile(loaded_file)
    with open(loaded_file, "r") as f:
        loaded_data = json.load(f)
        assert loaded_data == json_data

def test_load_data_permissions(tmpdir, json_data):
    # Mocked data and file path
    path = tmpdir.mkdir("test_dir")
    file_name = "test.json"

    # Patching open to raise PermissionError
    with patch("builtins.open", side_effect=PermissionError):
        # Call the JsonLoader and expect PermissionError
        loader = JsonLoader(path=str(path), file_name=file_name)
        with pytest.raises(PermissionError):
            loader.load(json_data)

def test_load_data_file_not_found(tmpdir, json_data):
    # Mocked data and file path
    path = tmpdir.mkdir("test_dir")
    file_name = "test.json"

    # Call the JsonLoader with a non-existing directory and expect FileNotFoundError
    loader = JsonLoader(path=str(path), file_name="non_existing_dir/test.json")
    with pytest.raises(FileNotFoundError):
        loader.load(json_data)

def test_load_data_other_error(tmpdir, json_data):
    # Mocked data and file path
    path = tmpdir.mkdir("test_dir")
    file_name = "test.json"

    # Patching open to raise an exception
    with patch("builtins.open", side_effect=Exception):
        # Call the JsonLoader and expect Exception
        loader = JsonLoader(path=str(path), file_name=file_name)
        with pytest.raises(Exception):
            loader.load(json_data)
