import threading
import time


def eat():
    time.sleep(3)
    print("You ate")


def drink():
    time.sleep(4)
    print("You drank")


def study():
    time.sleep(5)
    print("You studied")


x = threading.Thread(target=eat, args=())
x.start()

y = threading.Thread(target=drink, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
