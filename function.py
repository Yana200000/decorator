import datetime

from main import write_data_and_time


@write_data_and_time
def func(*args):
    return args


print(func(1, 2, 3))
