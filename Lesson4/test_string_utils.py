import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

class TestStringUtils:
    """Тесты для класса StringUtils"""

    def test_capitalize_positive(self, utils):
        assert utils.capitalize("skypro") == "Skypro"
        assert utils.capitalize("hello") == "Hello"
        assert utils.capitalize("123abc") == "123abc"

    def test_capitalize_edge_cases(self, utils):
        assert utils.capitalize("") == ""
        assert utils.capitalize(" skypro") == " skypro"

    def test_trim_positive(self, utils):
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("skypro") == "skypro"
        assert utils.trim("  hello  world  ") == "hello  world  "

    def test_trim_special_spaces(self, utils):
        assert utils.trim("\tskypro") == "\tskypro"
        assert utils.trim("\nskypro") == "\nskypro"

    def test_contains_positive(self, utils):
        assert utils.contains("SkyPro", "S") is True
        assert utils.contains("SkyPro", "Pro") is True
        assert utils.contains("SkyPro", "y") is True

    def test_contains_negative(self, utils):
        assert utils.contains("SkyPro", "U") is False
        assert utils.contains("", "a") is False
        assert utils.contains("SkyPro", "sky") is False

    def test_delete_symbol_positive(self, utils):
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert utils.delete_symbol("ababab", "a") == "bbb"

    def test_delete_symbol_edge_cases(self, utils):
        assert utils.delete_symbol("SkyPro", "X") == "SkyPro"
        assert utils.delete_symbol("", "a") == ""
        assert utils.delete_symbol("aaa", "a") == ""