import pytest
import requests
from faker import Faker
from client import YouGileClient
import time


fake = Faker()


# Подготовка клиента для тестов
@pytest.fixture(scope="session")
def api_client():
    time.sleep(2)
    # Инициализация клиента
    client = YouGileClient()

    # Получаем company_id
    companies_data = client.get_companies()
    client._company_id = companies_data["content"][0]["id"]

    # Получаем API-ключ один раз для всех тестов
    client._api_key = client.get_api_key(client._company_id)
    client.session.headers.update(
        {"Authorization": f"Bearer {client._api_key}"})

    # Возврат клиента тестам
    yield client

    # Удаляем API ключ после всех тестов
    if hasattr(client, '_api_key') and client._api_key:
        client.delete_api_key(client._api_key)


# Cоздание временного проекта
@pytest.fixture
def project_id(api_client):
    # Создаем временный проект для тестов
    project_id = api_client.create_project("Тестовый проект")
    yield project_id


# Получить список компаний
def test_get_companies(api_client):
    response_data = api_client.get_companies()

    # Проверяем что поле paging является словарём
    assert isinstance(response_data["paging"], dict)
    # Проверяем что поле content является списком
    assert isinstance(response_data["content"], list)
    # Проверяем что в списке content есть хотя бы одна компания
    assert len(response_data["content"]) > 0


# Создание ключа
def test_get_api_key(api_client):
    """Проверяем, что ключ был получен в фикстуре"""
    # Проверяем что у объекта api_client существует атрибут с именем _api_key
    assert hasattr(api_client, '_api_key')
    # Проверяем что API-ключ является строкой
    assert isinstance(api_client._api_key, str)
    # Проверяем что длина строки с ключом больше 0
    assert len(api_client._api_key) > 0


# Cоздать новый проект
@pytest.mark.positive
def test_create_project_positive(api_client):
    project_title = "Новый проект " + fake.word()
    project_id = api_client.create_project(project_title)

    assert isinstance(project_id, str)
    assert len(project_id) > 0


@pytest.mark.negative
def test_create_project_negative(api_client):
    with pytest.raises(requests.exceptions.HTTPError):
        # Пытаемся создать проект без заголовка
        api_client.create_project("")


# Изменить проект
@pytest.mark.positive
def test_update_project_positive(api_client, project_id):
    new_title = "Обновленный проект " + fake.word()
    response = api_client.update_project(project_id, new_title)

    # Проверяем, что в ответе есть поле "id"
    assert "id" in response
    # Проверяем, что ID в ответе совпадает с ID обновляемого проекта
    assert response["id"] == project_id
    # Проверяем, что проект действительно обновился
    project = api_client.get_project(project_id)
    assert project["title"] == new_title


@pytest.mark.negative
def test_update_project_negative(api_client, project_id):
    with pytest.raises(requests.exceptions.HTTPError):
        # Пытаемся обновить несуществующий проект
        api_client.update_project("invalid_project_id", "Название")

    # Пустое название
    with pytest.raises(requests.exceptions.HTTPError):
        api_client.update_project(project_id, "")

    # Невалидный формат ID
    with pytest.raises(requests.exceptions.HTTPError):
        api_client.update_project("123", "Название")


# Получить проект по ID
@pytest.mark.positive
def test_get_project_positive(api_client, project_id):
    project = api_client.get_project(project_id)

    # Убеждаемся, что сервер вернул тот же ID, который запрашивали
    assert project["id"] == project_id
    # Проект должен иметь название
    assert "title" in project
    # Проверяем наличие метки времени
    assert "timestamp" in project
    # Проверка, что название не пустое
    assert len(project["title"]) > 0


@pytest.mark.negative
def test_get_project_negative(api_client):
    with pytest.raises(requests.exceptions.HTTPError):

        # Пытаемся получить несуществующий проект
        api_client.get_project("invalid_project_id")
    with pytest.raises(requests.exceptions.HTTPError) as exc_info:
        api_client.get_project("invalid_project_id")

        # Проверка точного статус-кода
    assert exc_info.value.response.status_code == 404

    # Спецсимволы
    with pytest.raises(requests.exceptions.HTTPError):
        api_client.get_project("project_id'; DROP TABLE projects; --")
