from sqlalchemy import create_engine, text
from textwrap import dedent


class CompanyTable:

    __scripts = {
        "select": text("SELECT * FROM company WHERE deleted_at IS NULL"),

        "select_only_active": text(
            "SELECT * FROM company "
            "WHERE is_active = TRUE AND deleted_at IS NULL"
        ),

        "delete_by_id": text("DELETE FROM company WHERE id = :id"),

        "insert_new": text(dedent("""
        INSERT INTO company (
            name, description, is_active,
            create_timestamp, change_timestamp
        ) VALUES (
            :name, :description, TRUE, NOW(), NOW()
        )
    """)),

        "get_max_id": text(
            "SELECT MAX(id) FROM company "
            "WHERE deleted_at IS NULL"
        ),

        "select_by_id": text(
            "SELECT * FROM company "
            "WHERE id = :select_id AND deleted_at IS NULL"
        )
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_companies(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_active_companies(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_only_active"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete(self, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete_by_id"], {"id": id})
        conn.close()

    def create(self, name, description):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert_new"], {
                     "name": name, "description": description})
        conn.commit()
        conn.close()

    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        conn.close()
        return max_id

    def get_company_by_id(self, id):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["select_by_id"],
            {"select_id": id}
        )
        company = result.mappings().all()
        conn.close()
        return company
