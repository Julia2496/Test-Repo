import pytest
from unittest.mock import Mock


@pytest.mark.positive
def test_create_project_success(yougile_api, mock_requests):
    test_data = {"name": "Test Project", "description": "Test"}
    mock_response = Mock()
    mock_response.status_code = 201
    mock_response.json.return_value = {"id": "123", **test_data}
    mock_requests.post.return_value = mock_response

    response = yougile_api.create_project(test_data)

    assert response.status_code == 201
    assert response.json()["name"] == "Test Project"
    mock_requests.post.assert_called_once()


@pytest.mark.negative
def test_create_project_failure(yougile_api, mock_requests):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_requests.post.return_value = mock_response

    response = yougile_api.create_project({"invalid": "data"})
    assert response.status_code == 400


@pytest.mark.positive
def test_get_project_success(yougile_api, mock_requests):
    project_id = "123"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": project_id,
        "name": "Test Project"
    }
    mock_requests.get.return_value = mock_response

    response = yougile_api.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["id"] == project_id
    mock_requests.get.assert_called_once()


@pytest.mark.negative
def test_get_project_not_found(yougile_api, mock_requests):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_requests.get.return_value = mock_response

    response = yougile_api.get_project("non-existent-id")
    assert response.status_code == 404


@pytest.mark.positive
def test_update_project_success(yougile_api, mock_requests):
    project_id = "123"
    update_data = {
        "name": "Updated Name",
        "description": "Updated"
    }
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": project_id,
        **update_data
    }
    mock_requests.put.return_value = mock_response

    response = yougile_api.update_project(project_id, update_data)

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Name"
    mock_requests.put.assert_called_once()


@pytest.mark.negative
def test_update_project_invalid_data(yougile_api, mock_requests):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_requests.put.return_value = mock_response

    response = yougile_api.update_project("123", {"name": ""})
    assert response.status_code == 400
