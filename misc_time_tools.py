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
        self._total_elapsed = 0.0
        self._last_start = time.time() if auto_start else None

    def start(self):
        '''Start stopwatch, if paused, resume'''
        self._last_start = time.time()

    def pause(self):
        '''Temporarily pause the stopwatch'''
        self._total_elapsed += time.time() - self._last_start
        self._last_start = None

    def reset(self):
        '''Reset the stopwatch, doesn't start it'''
        self._total_elapsed = 0.0
        self._last_start = None

    def restart(self):
        '''Reset and start the stopwatch'''
        self.reset()
        self.start()

    @property
    def elapsed(self):
        return self._total_elapsed + (time.time() - self._last_start if self._last_start else 0.0)

    def __str__(self):
        return str(self.elapsed)

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
    print("avrg", ((t.elapsed + t2.elapsed)/2))

if __name__ == '__main__':
    main()