import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def check_password(password):
        """Проверка пароля: длина >= 8 и есть буквы, цифры, спецсимволы."""
        if len(password) < 8:
            return False
        
        
        has_letter = any(c.isalpha() for c in password)      
        has_digit = any(c.isdigit() for c in password)       
        has_special = any(c in string.punctuation for c in password)  
        
        
        return has_letter and has_digit and has_special

def test_generate_password_length():
    """Тест: проверяем, что пароль генерируется правильной длины."""
    assert len(generate_password(8)) == 8
    assert len(generate_password(12)) == 12
    assert len(generate_password(20)) == 20
    assert len(generate_password(1)) == 1
    assert len(generate_password(0)) == 0