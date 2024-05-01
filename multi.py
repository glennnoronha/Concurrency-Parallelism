from multiprocessing import Process, cpu_count
from time import time


def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter, args=(2000000,))
    b = Process(target=counter, args=(2000000,))
    c = Process(target=counter, args=(1000000,))
    d = Process(target=counter, args=(1000000,))

    start = time()
    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()

    end = time()
    print("finished in: ", end - start)


if __name__ == '__main__':
    main()
