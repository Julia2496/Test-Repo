import requests
import json
company_json = """
{
    "id": 111,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Барбершоп 'Цирюльникъ'",
    "description": "Крутые стрижки для крутых шишек"
    }
"""


def test_parse_json():
    company = json.loads(company_json)
    assert company["id"] == 111


company_list_json = """
[
    {
        "id": 111,
        "isActive": true,
        "createDateTime": "2022-12-23T14:43:26.713Z",
        "lastChangedDateTime": "2022-12-23T14:43:26.713Z",
        "name": "Барбершоп 'Цирюльникъ'",
        "description": "Крутые стрижки для крутых шишек"
    },
    {
        "id": 112,
        "isActive": true,
        "createDateTime": "2022-12-23T14:43:27.113Z",
        "lastChangedDateTime": "2022-12-23T14:43:27.113Z",
        "name": "Кондитерская Профи-тролли",
        "description": "Сладко и точка"
    },
    {
        "id": 114,
        "isActive": false,
        "createDateTime": "2022-12-23T14:43:27.213Z",
        "lastChangedDateTime": "2022-12-23T14:43:27.213Z",
        "name": "Муж на час",
        "description": "Ремонт вообще всего"
    },
    {
        "id": 113,
        "isActive": true,
        "createDateTime": "2022-12-23T14:43:27.213Z",
        "lastChangedDateTime": "2022-12-23T14:43:27.213Z",
        "name": "Клининг-центр 'Клинг-кинг'",
        "description": "Куда по помытому??"
    },
    {
        "id": 115,
        "isActive": true,
        "createDateTime": "2022-12-23T14:43:27.313Z",
        "lastChangedDateTime": "2022-12-23T14:43:27.313Z",
        "name": "Шиномонтаж на Ленинском",
        "description": "Пятое колесо - это хорошо"
    }
]
"""


def test_parse_array_json():
    company_list = json.loads(company_list_json)
    first_company = company_list[0]
    assert first_company["name"] == "Барбершоп 'Цирюльникъ'"
    # assert company_list[1]["id"] == 112


r = requests.get('https://httpbin.org/basic-auth/user/pass',
                 auth=('user', 'pass'))
r.status_code


base_url = "http://5.101.50.27:8000"


# Получить список компаний
def test_simple_req():
    resp = requests.get(base_url + '/company/list')
    response_body = resp.json()
    first_company = response_body[0]
    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"


def test_auth():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    assert resp.status_code == 200


# Авторизация
def test_auth():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    assert resp.json()["user_token"] is not None
    assert resp.status_code == 200


# Создание компании
def test_create_company():
    company = {
        "name": "python",
        "description": "requests"
    }
    resp = requests.post(base_url + '/company/create',
                         json=company)
    assert resp.status_code == 201
