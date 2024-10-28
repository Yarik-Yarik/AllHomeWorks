import pytest # noqa: F401
from StringUtils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

string_utils = StringUtils()

@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),  # обычное слово
        ("hello world", "Hello world"),  # строка с маленькими буквами
    ],
)
def test_capitilize(input_str, expected):
    # Позитивные тесты
    assert string_utils.capitilize(input_str) == expected

    # Негативные тесты
    assert string_utils.capitilize("") == ""
    assert string_utils.capitilize("123abc") == "123abc"


def test_trim():
    # Позитивные тесты
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("hello   ") == "hello"

    # Негативные тесты
    assert string_utils.trim("") == ""
    assert string_utils.trim("   ") == ""


def test_to_list():
    # Позитивные тесты
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]

    # Негативные тесты
    assert string_utils.to_list("") == []
    assert string_utils.to_list(None) == []


def test_contains():
    # Позитивные тесты
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "U") is False

    # Негативные тесты
    assert string_utils.contains("", "S") is False
    assert string_utils.contains("SkyPro", "") is True


def test_delete_symbol():
    # Позитивные тесты
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"

    # Негативные тесты
    assert string_utils.delete_symbol("", "k") == ""
    assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"


def test_starts_with():
    # Позитивные тесты
    assert string_utils.starts_with("SkyPro", "S") is True
    assert string_utils.starts_with("SkyPro", "P") is False

    # Негативные тесты
    assert string_utils.starts_with("", "S") is False
    assert string_utils.starts_with("SkyPro", "") is True


def test_end_with():
    # Позитивные тесты
    assert string_utils.end_with("SkyPro", "o") is True
    assert string_utils.end_with("SkyPro", "y") is False

    # Негативные тесты
    assert string_utils.end_with("", "o") is False
    assert string_utils.end_with("SkyPro", "") is True


def test_is_empty():
    # Позитивные тесты
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty(" ") is True

    # Негативные тесты
    assert string_utils.is_empty("SkyPro") is False


def test_list_to_string():
    # Позитивные тесты
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"

    # Негативные тесты
    assert string_utils.list_to_string([]) == ""