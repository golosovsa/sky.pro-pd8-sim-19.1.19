# Просто: Напишите функцию `easy` которая 
# получает пароль в открытом виде и 
# возвращает хеш с использованием алгоритма md5
#
# Сложно: Напишите функцию `hard` которая 
# получает пароль в открытом виде и соль 
# и возвращает хеш с использованием алгоритма sha256
import base64
import hashlib


def easy(password: str):
    # TODO напишите Ваше решение здесь
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def hard(password: str, salt):
    # TODO Или напишите Ваше решение здесь.
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        1000
    )
