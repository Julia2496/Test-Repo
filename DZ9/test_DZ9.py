import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import get_db
from typing import Generator

# Тестовые данные
TEST_DATA = {
    "subject": {
        "id": 9999,
        "title": "Advanced Python Programming"
    },
    "user": {
        "id": 9999,
        "email": "john.doe@university.edu",
        "subject_id": 9999  # Связь с тестовым предметом
    },
    "student": {
        "user_id": 9999,
        "level": "Intermediate",
        "education_form": "Evening classes",
        "subject_id": 9999  # Связь с тестовым предметом
    }
}


@pytest.fixture
def db_session() -> Generator[Session, None, None]:
    """Фикстура для работы с БД"""
    with get_db() as db:
        # Очистка тестовых данных перед тестом
        cleanup_test_data(db)
        yield db
        # Откат изменений после теста
        cleanup_test_data(db)


def cleanup_test_data(db: Session):
    """Очистка тестовых данных"""
    db.execute(text("DELETE FROM group_student WHERE user_id = :user_id"),
               {"user_id": TEST_DATA["user"]["id"]})
    db.execute(text("DELETE FROM student WHERE user_id = :user_id"),
               {"user_id": TEST_DATA["user"]["id"]})
    db.execute(text("DELETE FROM users WHERE user_id = :user_id"),
               {"user_id": TEST_DATA["user"]["id"]})
    db.execute(text("DELETE FROM subject WHERE subject_id = :id"),
               {"id": TEST_DATA["subject"]["id"]})
    db.commit()


def setup_test_data(db: Session):
    """Создание тестовых данных"""
    try:
        # Добавляем предмет
        db.execute(text("""
            INSERT INTO subject (subject_id, subject_title)
            VALUES (:id, :title)
        """), TEST_DATA["subject"])

        # Добавляем пользователя
        db.execute(text("""
            INSERT INTO users (user_id, user_email, subject_id)
            VALUES (:id, :email, :subject_id)
        """), TEST_DATA["user"])

        # Добавляем студента
        db.execute(text("""
            INSERT INTO student (user_id, level, education_form, subject_id)
            VALUES (:user_id, :level, :education_form, :subject_id)
        """), TEST_DATA["student"])

        db.commit()
    except Exception as e:
        db.rollback()
        pytest.fail(f"Ошибка подготовки данных: {str(e)}")


def test_db_connection(db_session: Session):
    """Тест подключения к БД"""
    result = db_session.execute(text("SELECT 1")).scalar()
    assert result == 1


def test_add_subject(db_session: Session):
    """Тест добавления предмета"""
    new_subject = {
        "id": 8888,
        "title": "Database Design Fundamentals"
    }

    db_session.execute(text("""
        INSERT INTO subject (subject_id, subject_title)
        VALUES (:id, :title)
    """), new_subject)
    db_session.commit()

    result = db_session.execute(text("""
        SELECT subject_title FROM subject WHERE subject_id = :id
    """), {"id": new_subject["id"]}).fetchone()

    assert result is not None
    assert result[0] == new_subject["title"]

    # Очистка
    db_session.execute(text("DELETE FROM subject WHERE subject_id = :id"),
                       {"id": new_subject["id"]})
    db_session.commit()


def test_update_student_level(db_session: Session):
    """Тест обновления уровня студента"""
    setup_test_data(db_session)

    new_level = "Advanced"
    db_session.execute(text("""
        UPDATE student SET level = :level
        WHERE user_id = :user_id
    """), {
        "level": new_level,
        "user_id": TEST_DATA["user"]["id"]
    })
    db_session.commit()

    result = db_session.execute(text("""
        SELECT level FROM student WHERE user_id = :user_id
    """), {"user_id": TEST_DATA["user"]["id"]}).fetchone()

    assert result[0] == new_level


def test_delete_user(db_session: Session):
    """Тест удаления пользователя"""
    setup_test_data(db_session)

    db_session.execute(text("""
        DELETE FROM users WHERE user_id = :user_id
    """), {"user_id": TEST_DATA["user"]["id"]})
    db_session.commit()

    result = db_session.execute(text("""
        SELECT 1 FROM users WHERE user_id = :user_id
    """), {"user_id": TEST_DATA["user"]["id"]}).fetchone()

    assert result is None
