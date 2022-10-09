import os
from datetime import datetime

def loger(path):
    def _loger(function):
        def new_func(*args, **kwargs):
            with open(path, 'a', encoding='UTF-8') as file:
                file.write(f'***Вызов функции {function} - {datetime.now()}, параметры {args} - {kwargs} \n')
                result = function(*args, **kwargs)
                file.write(f'Результат +++++++++++++++++++'+'\n')
                for item in result:
                    file.write(item+'\n')
                file.write(f'Результат -------------------'+'\n')
                file.write(f'***Конец функции {function} - {datetime.now()}')
            return result
        return new_func
    return _loger