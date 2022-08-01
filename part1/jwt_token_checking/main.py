# Напишите функцию `check_token`, которая проверяет токен. 
# Внимание, функция должна принимать 3 позиционных агрумента:
# токен, алгоритм и секрет.
# Функция должна возвращать:
# Декодированную информацию если токен удалось декодировать.
# И возвращайть False, если токен декодировать не удалось.

# В тестах мы проверим функцию,отправив ей верный и неверный токен.
import jwt


def check_token(token, secret, algorithms):
    # TODO напишите ваше решение здесь
    try:
        return jwt.decode(token, secret, algorithms=algorithms)

    except jwt.exceptions.PyJWTError:
        return False
