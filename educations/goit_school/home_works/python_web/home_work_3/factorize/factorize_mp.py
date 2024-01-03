from multiprocessing import Pool, current_process, cpu_count
from datetime import datetime


def main_func(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def factorize_mp(*num):
    result = []
    time_start = datetime.now()
    with Pool(processes=4) as pool:
        for i in pool.map(main_func, num):
            result.append(i)
    print(f'time factorize_mp: {datetime.now() - time_start}')
    return result


if __name__ == '__main__':
    a, b, c, d = factorize_mp(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    print(cpu_count())