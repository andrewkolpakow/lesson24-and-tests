# Напишите декоратор @logger, который после выполнения
# функции напишет название функции и статус выполнения
# (если произошло исключение нужно вывести
# сообщение “exc_has_appeared”, иначе вывести только название функции.
from functools import wraps


def logger(func):
    # TODO напишите функцию-декоратор здесь
    @wraps(func)
    def _wrapper(*args, **kwargs):
        exc_has_appeared = False
        try:
            func(*args, **kwargs)
        except:
            exc_has_appeared = True
        finally:
            print(func.__name__)
            if exc_has_appeared:
                print('exc_has_appeared')
    return _wrapper()


# Код для самопроверки
@logger
def function_with_error():
    var = 1/0


@logger
def working_function():
    pass


# Запустите этот файл для проверки
if __name__ == "__main__":
    # Вызов функции ниже должен вывести в терминал название функции
    # и сообщить, что произошла ошибка
    function_with_error()
    # Вызов функции ниже должен вывести только ее название
    working_function()
