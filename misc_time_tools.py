import time

class Timer:
    def __init__(self, time):
        self._time = time
        self.start = time.time()

    @property
    def time_left(self):
        return self._time - (time.time() - self.start)

    @property
    def times_up(self):
        return self.time_left <= 0

class Stopwatch:
    def __init__(self, *, auto_start=True):
        """Class name seems self explanatory
        Acess time with Stopwatch.elapsed
        If you want to quickly acess the value just print it directly
        It has `start()`, `pause()`, `reset()` and `restart()`
        Example:
        ```
        from misc_time_tools import Stopwatch
        t = Stopwatch()
        print(t) # around 0.0
        time.sleep(1)
        print(t) # around 1.0
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
        self._total_elapsed += time.time() - self._last_start if self._last_start else 0.0
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
    time.sleep(0.67)
    print(t)
    t.pause()
    time.sleep(1)
    print(t)
    t.start()
    t.restart()
    time.sleep(0.67)
    print(t)

if __name__ == '__main__':
    main()