import string
import traceback
from datetime import datetime

# Импорт функции генерации
try:
    from password.new_password import generate_password
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    raise SystemExit(1)


# --- Исходные тесты (с минимальными обязательными исправлениями, чтобы они запускались) ---

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)
    for char in password:
        assert char in valid_characters, f"Недопустимый символ: {char!r}"


def test_password_lenght():
    """Тест: длина пароля соответствует заданной (минимальная 8)"""
    length = 12
    password = generate_password(length)
    assert len(password) >= 8, f"Пароль короче 8 символов: {len(password)}"


def test_password_correct():
    """
    Тест: пароль не равен одной из тривиальных последовательностей.
    Проверяем один сгенерированный пароль (как в исходной идее).
    """
    trivial_patterns = [
        "11111111", "22222222", "33333333", "44444444", "55555555",
        "66666666", "77777777", "88888888", "99999999",
        "12345678", "23456789", "34567891", "45678912", "56789123",
        "67891234", "78912345", "89123456", "91234567"
    ]
    password = generate_password(8)
    assert password not in trivial_patterns, f"Сгенерирован тривиальный пароль: {password}"


# Дополнительный тест (по твоему запросу: два подряд пароля различаются)
def test_passwords_are_different():
    """Тест: два сгенерированных подряд пароля различаются"""
    p1 = generate_password(16)
    p2 = generate_password(16)
    assert p1 != p2, "Два сгенерированных подряд пароля оказались одинаковыми"
