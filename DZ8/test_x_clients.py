from CompanyApi import CompanyApi


api = CompanyApi("http://5.101.50.27:8000")


def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0


# Проверка получения активных компаний
def test_get_active_companies():
    # Получить список всех компаний
    full_list = api.get_company_list()
    # Получить список активных компаний
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    # Проверить, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)


# # Получить список активных компаний
# my_params = {'active': 'true'}
# resp = requests.get(base_url+'/company/list', params=my_params)
# filtered_list = resp.json()

# # Получить список активных компаний
# resp = requests.get(base_url+'/company/list', params={'active': 'true'})
# filtered_list = resp.json()


# Проверка добавления новой компании
def test_add_new():
    # Получить количество компаний до
    body = api.get_company_list()
    # Находим длину переменной
    len_before = len(body)
    # Создать новую компанию
    name = "Autotest"
    descr = "Descr"
    api.create_company(name, descr)
    # Получить количество компаний после
    body = api.get_company_list()
    # Находим длину переменной
    len_after = len(body)
    # Проверить, что размер списка увеличен на +1
    assert len_after - len_before == 1
    # Проверить название и описание
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr


# Изменение компании
def test_get_one_company():
    # Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)

    # Проверим название, описание и статус новой компании:
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True


# Удаление компании
def test_edit():
    name = "Company to be edited"
    descr = "Edit me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_name = "Updated"
    new_descr = "_upd_"

    edited = api.edit_company(new_id, new_name, new_descr)

    # Проверяем, что название компании поменялось
    assert edited["name"] == new_name
    # Проверяем, что описание компании поменялось
    assert edited["description"] == new_descr
