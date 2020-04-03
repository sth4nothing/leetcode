from concurrent.futures import ThreadPoolExecutor
import time
import functools


class FooBar:
    def __init__(self, n):
        self.n = n
        self.stat = 0

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            while self.stat != 0:
                time.sleep(0.0005)
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.stat = 1

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            while self.stat != 1:
                time.sleep(0.0005)
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.stat = 0


def pf():
    print('foo', end='')


def pb():
    print('bar', end='')


def timecost(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        cost = (time.time() - start) * 1000
        print(f'time cost: {cost:.3f} ms')
        return res
    return wrapper


@timecost
def main():
    fb = FooBar(100)
    with ThreadPoolExecutor(2) as e:
        e.submit(fb.foo, pf)
        e.submit(fb.bar, pb)


if __name__ == "__main__":
    main()
