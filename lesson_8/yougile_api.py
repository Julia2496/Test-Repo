import requests


class YougileAPI:
    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"
        }
        self.session = requests.Session()

    def create_project(self, project_data):
        url = f"{self.base_url}/projects"
        return self.session.post(url, json=project_data, headers=self.headers)

    def get_project(self, project_id):
        url = f"{self.base_url}/projects/{project_id}"
        return self.session.get(url, headers=self.headers)

    def update_project(self, project_id, update_data):
        url = f"{self.base_url}/projects/{project_id}"
        return self.session.put(url, json=update_data, headers=self.headers)
