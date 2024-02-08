import logging
import os
import pytest
from datetime import datetime
from unittest.mock import Mock, patch
from pywebharvest.runners import Pipeline

@pytest.fixture
def mock_etl_main_function():
    return Mock()

@pytest.fixture
def pipeline(mock_etl_main_function):
    return Pipeline(name="test_pipeline", etl_main_function=mock_etl_main_function)


def test_start_success(mock_etl_main_function, capsys, pipeline):
    # Mock etl_main_function
    mock_etl_main_function.return_value = "SUCCESS"

    # Call start method
    result = pipeline.start()

    # Assertions
    captured = capsys.readouterr()
    assert result == "SUCCESS"
    assert "Pipeline 'test_pipeline' started..." in captured.out
    assert "Pipeline 'test_pipeline' completed successfully with resul:\n SUCCESS\n" in captured.out
    assert not captured.err

def test_start_failure(mock_etl_main_function, capsys, pipeline):
    # Mock etl_main_function to raise an exception
    mock_etl_main_function.side_effect = Exception("Some error")

    # Call start method and expect exception to be raised
    with pytest.raises(Exception):
        pipeline.start()

    # Assertions
    captured = capsys.readouterr()
    assert "Error occurred in pipeline 'test_pipeline': Some error\n" in captured.out
