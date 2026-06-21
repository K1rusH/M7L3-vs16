import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""
def test_password_length():
    length = 6
    password = generate_password(length)

# Важно убедиться, что функция reverse_string корректно обрабатывает пустую строку, не вызывая ошибок.
def test_password():
    password1 = generate_password(6)
    password2 = generate_password(6)
    password3 = generate_password(6)
    password4 = generate_password(6)
    password5 = generate_password(6)
    password6 = generate_password(6)
