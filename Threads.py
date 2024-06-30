from threading import *


class Alphabets(Thread):
    def run(self):
        for i in range(65, 91):
            print(chr(i))


if __name__ == '__main__':
    t = Alphabets()
    t.start()
    for i in range(65, 91):
        print(i)
    t.join()
# two threads are running simultaneously so the results will be mixed
