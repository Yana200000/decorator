from datetime import datetime


def write_data_and_time(old_function):
    def new_function(*args):
        file = open('new_file.txt', 'w+')
        func_name = old_function.__name__
        file.write(f'Дата и время вызова функции: {datetime.today().strftime("%Y-%m-%d-%H.%M.%S")}\n'
                   f'Имя функции: {func_name}\n'
                   f'Аргументы функции: {args}\n'
                   f'Значение: {old_function}')

        return f'Информация добавлена'
    return new_function

