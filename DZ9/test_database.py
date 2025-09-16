from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'users'


def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM company"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['id'] == 1
    assert row1['name'] == "QA Студия 'ТестировщикЪ'"

    connection.close()


def test_select_1_row_with_two_filters():
    connection = db.connect()
    sql_statement = text(
        'SELECT * FROM company WHERE "is_active" = :is_active AND id >= :id')
    result = connection.execute(sql_statement, {"id": 12, "is_active": True})
    rows = result.mappings().all()

    assert len(rows) == 15
    connection.close()


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("""INSERT INTO company ("name", "is_active",
            "create_timestamp", "change_timestamp"
            VALUES (:new_name, TRUE, NOW(), NOW())""")
    connection.execute(sql, {"new_name": "Skypro"})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE company SET description = :descr WHERE id = :id")
    connection.execute(sql, {"descr": 'New descr', "id": 31})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM company WHERE id = :id")
    connection.execute(sql, {"id": 33})

    transaction.commit()
    connection.close()
