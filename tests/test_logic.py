# Pytest-based tests for logic
import pytest
from unittest.mock import patch
from client import main

@patch("client.main.requests.post")
def test_borrow_book_fail(mock_post):
    mock_post.return_value.json.return_value = {"error": "Book not available"}
    mock_post.return_value.status_code = 400
    response = main.borrow_book()
    assert "error" in response


