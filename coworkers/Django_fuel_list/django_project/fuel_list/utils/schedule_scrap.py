import schedule
import time
from django_project.fuel_list.fuel_parser.fuel_parser.spiders.prices import main as parser
from multiprocessing import Process


def worker(pars):
    print('Worker starting')
    pr = Process(target=parser)
    pr.start()
    pr.join()


def main():
    schedule.every().day.at("15:00").do(worker, parser)
    # schedule.every().day.at("20:21").do(worker, parser)
    # schedule.every().day.at("20:23").do(worker, parser)
    # schedule.every(1).minutes.do(worker, parser)
    print('Spider working now')
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()


