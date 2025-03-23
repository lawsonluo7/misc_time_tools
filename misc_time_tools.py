import time

class Stopwatch:
    def __init__(self, auto_start=True):
        if auto_start:
            self.restart()
        else:
            self.reset()

    def start(self):
        '''Start stopwatch'''
        self.start_time = time.time()

    def stop(self):
        '''Stop the stopwatch, can't be resumed'''
        self.end_time = time.time()

    def reset(self):
        '''Reset the stopwatch'''
        self.start_time = time.time()
        self.end_time = None

    def restart(self):
        '''Reset and start the stopwatch'''
        self.reset()
        self.start()

    @property
    def elapsed(self):
        return (
            self.end_time
            if self.end_time
            else time.time()
            - self.start_time)

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

print(Stopwatch().elapsed)