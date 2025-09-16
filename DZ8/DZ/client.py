import requests
from config import URL, LOGIN, PASSWORD


class YouGileClient:
    def __init__(self):
        self.base_url = URL
        # Создаем сессию для всех запросов
        self.session = requests.Session()
        # Устанавливаем общие заголовки для всех запросов сессии
        self.session.headers.update({"Content-Type": "application/json"})
        # Внутренние переменные для хранения ключа
        self._api_key = None
        self._company_id = None

    def get_companies(self):
        """Получить список компаний и вернуть ID первой компании."""
        data = {
            "login": LOGIN,
            "password": PASSWORD,
            "name": "Test"
        }
        response = self.session.post(
            f"{self.base_url}auth/companies",
            json=data
        )
        # Проверяем, что статус 200-299
        response.raise_for_status()
        # Возвращаем весь JSON-ответ
        return response.json()

    def get_api_key(self, company_id):
        """Запрос API-ключа для компании."""
        data = {
            "login": LOGIN,
            "password": PASSWORD,
            "companyId": company_id
        }
        response = self.session.post(
            f"{self.base_url}auth/keys",
            json=data
        )
        response.raise_for_status()
        return response.json()["key"]

    def delete_api_key(self, api_key):
        """Удаление API ключа."""
        response = self.session.delete(
            f"{self.base_url}auth/keys/{api_key}"
        )
        return response.status_code

    def create_project(self, title: str) -> str:
        """Создать проект и вернуть его ID."""
        headers = {"Authorization": f"Bearer {self._api_key}"}
        response = self.session.post(
            f"{self.base_url}projects",
            json={"title": title},
            headers=headers
        )
        response.raise_for_status()
        return response.json()["id"]

    def update_project(self, project_id: str, new_title: str):
        """Обновить проект."""
        headers = {"Authorization": f"Bearer {self._api_key}"}
        response = self.session.put(
            f"{self.base_url}projects/{project_id}",
            json={"title": new_title},
            headers=headers
        )
        response.raise_for_status()
        return response.json()

    def get_project(self, project_id: str):
        """Получить проект по ID."""
        headers = {"Authorization": f"Bearer {self._api_key}"}
        response = self.session.get(
            f"{self.base_url}projects/{project_id}",
            headers=headers
        )
        response.raise_for_status()
        return response.json()

    def set_api_key(self, api_key):
        """Установить API ключ для клиента."""
        self._api_key = api_key
        self.session.headers.update({"Authorization": f"Bearer {api_key}"})
