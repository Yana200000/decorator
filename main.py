from datetime import datetime


def write_data_and_time(old_function):
    def new_function(*args):
        file = open('new_file.txt', 'w+')
        file.write(f'Дата и время вызова функции: {datetime.today().strftime("%Y-%m-%d-%H.%M.%S")}; имя функции: {old_function}; аргументы функции: {args}; значение: {old_function()}')

        return f'Информация добавлена'
    return new_function

