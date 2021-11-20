import datetime
import requests as rq
from main import write_data_and_time


@write_data_and_time
def func(*args):
    return f'{args}'


if __name__ == '__main__':
    print(func(1, 2, 8))
