# import time
# import threading


# def get_data(data, value):
#     for _ in range(value):
#         print(f"{threading.current_thread().name} - {data}")
#         time.sleep(1)
#
# thr_list = []
#
# for i in range(3):
#     thr = threading.Thread(target=get_data, name=f"thr-{i}", args=(str(time.time()), i, ))
#     thr_list.append(thr)
#     thr.start()
#
# for i in thr_list:
#     i.join()
# print("finish")


# for i in range(100):
#     print(f"current: {i}")
#     time.sleep(1)
#
#     if i % 10 == 0:
#         print("active thread: ", threading.active_count())
#         print("enumerate: ", threading.enumerate())
#         print("thr is alive: ", thr.is_alive())

# value = 0
# locker = threading.Lock()

# def inc_value():
#     global value
#     while True:
#         locker.acquire()
#         value += 1
#         print(value)
#         time.sleep(1)
#         locker.release()

# for _ in range(5):
#     threading.Thread(target=inc_value().start)
