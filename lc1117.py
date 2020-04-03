from timer import timer
from threading import Lock, Semaphore
from queue import Queue

class H2O:
    def __init__(self):
        self.h = Queue()
        self.o = Queue()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.h.put(releaseHydrogen)
        self.pop()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o.put(releaseOxygen)
        self.pop()
    
    def pop(self) -> None:
        if self.h.qsize() >= 2 and self.o.qsize() >= 1:
            self.h.get()()
            self.h.get()()
            self.o.get()()


def releaseHydrogen():
    print('H', end='')


def releaseOxygen():
    print('O', end='')


@timer
def main():
    from concurrent.futures import ThreadPoolExecutor
    h2o = H2O()
    with ThreadPoolExecutor() as pool:
        for c in 'OHOHOOHHOHHOOHHHHOOHOOHHOHHOOHHHOOHOHHOHHOHHHHHOHHHHHHHHHHHH':
            if c == 'O':
                pool.submit(h2o.oxygen, releaseOxygen)
            else:
                pool.submit(h2o.hydrogen, releaseHydrogen)


if __name__ == "__main__":
    main()
