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

def test_password_lenght():         
    assert (password_length(12)) >= 8

def test_password_correct():
    assert generate_password != 11111111 or 22222222 or 33333333 or 44444444 or 55555555 or 66666666 or 77777777 or 88888888 or 99999999 or 12345678 or 23456789 or 34567891 or 45678912 or 56789123 or 67891234 or 78912345 or 89123456 or 91234567