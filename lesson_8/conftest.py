import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_requests():
    return Mock()


@pytest.fixture
def base_url():
    return "https://yougile.com/api-v2"


@pytest.fixture
def auth_token():
    return "test-auth-token"


@pytest.fixture
def yougile_api(base_url, auth_token, mock_requests):
    class YougileAPI:
        def __init__(self):
            self.base_url = base_url
            self.headers = {
                "Authorization": f"Bearer {auth_token}",
                "Content-Type": "application/json"
            }
            self.session = mock_requests

        def create_project(self, data):
            url = f"{self.base_url}/projects"
            return self.session.post(url, json=data, headers=self.headers)

        def get_project(self, project_id):
            url = f"{self.base_url}/projects/{project_id}"
            return self.session.get(url, headers=self.headers)

        def update_project(self, project_id, data):
            url = f"{self.base_url}/projects/{project_id}"
            return self.session.put(url, json=data, headers=self.headers)

    return YougileAPI()
