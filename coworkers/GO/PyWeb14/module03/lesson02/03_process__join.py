import sys
from multiprocessing import Process, Pool
from time import sleep


def example_work(params):
    sleep(0.5)
    print(params)
    sys.exit(0)


if __name__ == '__main__':
    prs = []
    for i in range(5):
        pr = Process(target=example_work, args=(f"Count process - {i}",))  # daemon=True
        pr.start()
        prs.append(pr)

    [el.join() for el in prs]

    print('End program')
