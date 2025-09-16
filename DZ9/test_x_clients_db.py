from CompanyApi import CompanyApi
from CompanyTable import CompanyTable


api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")


# Получить компании
def test_get_companies():
    # Шаг1: получить список компаний через API:
    api_result = api.get_company_list()

    # Шаг2: получить список компаний из БД:
    db_result = db.get_companies()

    # Шаг2: проверить, что списки равны
    assert len(api_result) == len(db_result)


# Получение активных компаний
def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    db_list = db.get_active_companies()

    assert len(filtered_list) == len(db_list)


# Добавить новую компанию
def test_add_new():
    # Получить количество компаний до
    body_before = api.get_company_list()
    len_before = len(body_before)

    # Создать новую компанию
    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Получить количество компаний после
    body_after = api.get_company_list()
    len_after = len(body_after)

    # Удалить компанию (после проверок)
    db.delete(new_id)

    # Проверить, что размер списка увеличен на 1
    assert len_after - len_before == 1

    # Проверить данные через прямой запрос по ID
    created_company = api.get_company(new_id)
    assert created_company["name"] == name
    assert created_company["description"] == descr


# Получить компанию по ID
def test_get_one_company():
    # Подготовка
    name = "Skypro"
    description = "descr"
    db.create(name, description)
    max_id = db.get_max_id()

    # Получение компании
    new_company = api.get_company(max_id)

    # Удаление
    db.delete(max_id)

    # Проверим название, описание и статус новой компании:
    assert new_company["name"] == name
    assert new_company["description"] == description
    assert new_company["is_active"] is True


# Изменение компании
def test_edit():
    # Добавляем в базу компанию с названием Skypro:
    name = "Skypro"
    description = "Курсы"
    db.create(name, description)
    max_id = db.get_max_id()

    # Меняем описание компании в поле description:
    new_name = "Updated"
    new_descr = "_upd_"
    edited = api.edit_company(max_id, new_name, new_descr)

    # Удаляем компанию:
    db.delete(max_id)

    # Проверяем, что название компании поменялось
    assert edited["name"] == new_name
    # Проверяем, что описание компании поменялось
    assert edited["description"] == new_descr


# Удаление компании
def test_delete():
    # Добавили компанию через базу:
    name = "Skypro"
    description = "Курсы"
    db.create(name, description)
    max_id = db.get_max_id()

    # Удалили компанию:
    deleted = api.delete_company(max_id)

    assert deleted["company_id"] == max_id
    assert deleted["detail"] == "Компания успешно удалена"

    # Проверили по ID, что компании нет в базе:
    rows = db.get_company_by_id(max_id)
    assert len(rows) == 0


# Дективация компании
def test_deactivate():
    # Создаем компанию
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]
    # Деактивируем компанию
    body = api.set_active_state(new_id, False)

    # Проверяем, что у компании статус «неактивная»
    assert body["is_active"] is False


# Деактивация и активация компании
def test_deactivate_and_activate_back():
    # Создаем компанию:
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]

    # Деактивируем компанию с помощью параметра False
    body_d = api.set_active_state(new_id, False)

    # Проверяем, что компания не активная
    assert body_d["is_active"] is False

    # Активируем компанию с помощью параметра True
    body_a = api.set_active_state(new_id, True)

    # Проверяем, что компания активная
    assert body_a["is_active"] is True
