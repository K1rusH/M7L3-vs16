import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters


def test_len_password():
    password = generate_password(42)
    assert len(password) == 42, "Длина не соответсвует заданной"

def test_two_passwords():
    password_1 = generate_password(12)
    password_2 = generate_password(12)
    assert password_1 != password_2, "Пароли одинаковые"
    """
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""