import time

class Stopwatch:
    def __init__(self, *, auto_start=True):
        """Behaves a lot like a `float`,
        but each time you print it or perform math operations on it,
        it gives a dynamically updated time.
        It has `start()`, `pause()`, `reset()` and `restart()`
        Example:
        ```
        from misc_time_tools import Stopwatch
        t = Stopwatch()
        time.sleep(1)
        print(t) # around 1.0
        print(t + 1) # around 2.0
        t.pause()
        time.sleep(1)
        print(t) # still 1.0
        ```
        """
        if auto_start:
            self.restart()
        else:
            self.reset()

    def start(self):
        '''Start stopwatch, if paused, resume'''
        self.paused: bool = False
        self.total_paused_time += time.time() - self.last_paused_time

    def pause(self):
        '''Temporarily pause the stopwatch'''
        self.last_paused_time: float = time.time()
        self.paused: bool = True

    def reset(self):
        '''Reset the stopwatch, doesn't start it'''
        self.start_time: float = time.time()
        self.total_paused_time: float = 0.0
        self.pause()

    def restart(self):
        '''Reset and start the stopwatch'''
        self.reset()
        self.start()

    @property
    def elapsed(self):
        return (time.time() - self.start_time) - self.total_paused_time

    def __str__(self):
        return str(self.elapsed)

    def __int__(self):
        return int(self.elapsed)

    def __float__(self):
        return self.elapsed

    def __add__(self, other):
        return float(self) + other

    def __radd__(self, other):
        return other + float(self)

    def __sub__(self, other):
        return float(self) - other

    def __rsub__(self, other):
        return other - float(self)

    def __mul__(self, other):
        return float(self) * other

    def __rmul__(self, other):
        return other * float(self)

    def __truediv__(self, other):
        return float(self) / other

    def __rtruediv__(self, other):
        return other / float(self)

    def __floordiv__(self, other):
        return float(self) // other

    def __rfloordiv__(self, other):
        return other // float(self)

    def __mod__(self, other):
        return float(self) % other

    def __rmod__(self, other):
        return other % float(self)

    def __pow__(self, other, modulo=None):
        return pow(float(self), other, modulo)

    def __rpow__(self, other):
        return pow(other, float(self))

    def __neg__(self):
        return -float(self)

    def __pos__(self):
        return +float(self)

    def __abs__(self):
        return abs(float(self))

    def __round__(self, ndigits=None):
        return round(float(self), ndigits)

    def __eq__(self, other):
        return float(self) == other

    def __ne__(self, other):
        return float(self) != other

    def __lt__(self, other):
        return float(self) < other

    def __le__(self, other):
        return float(self) <= other

    def __gt__(self, other):
        return float(self) > other

    def __ge__(self, other):
        return float(self) >= other

def main():
    t = Stopwatch()
    for _ in range(2):
        time.sleep(1)
        print(t)
        t.pause()
        time.sleep(1)
        print(t)
    t.restart()
    time.sleep(1)
    print(t)
    t2 = Stopwatch()
    time.sleep(1)
    print("\n\nt1", t)
    print("t2", t2)
    print("avrg", ((t + t2)/2))

if __name__ == '__main__':
    main()
