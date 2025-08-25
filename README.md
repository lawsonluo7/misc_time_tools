# Misc Time Tools

This repository contains miscellanious Python tools for working with time and dates.

## StopWatch

### Description
Keeps track of the amount of time that has elapsed since you started it

### Usage
Acess time with `Stopwatch.elapsed` (you will get a `float`).
See Methods section below.

#### Methods
##### `start()`
starts counting the time

##### `pause()`
pause the time, it remains resumable

##### `reset()`
elapsed time will be turned to 0, pauses the timer

##### `restart()`
elapsed time will be turned to 0, starts it for you

#### Example
Here is a example of how to use the `Stopwatch` tool:

```python
from misc_time_tools import Stopwatch

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
```

## Timer
### Description
A class that helps check wether a certain amount of time has passed since the instance was created

### Usage
`Timer.time_is_up` will return a `bool` that indicates whether the timer is done
`Timer.time_left` will return a `float` of the amount of time left until the timer is done

#### Example
Here is an example of using `Timer` class

```python
from misc_time_tools import Timer
t = Timer(h=0, m=0, s=5)
while not t.time_is_up:
    print(t.time_left)
    time.sleep(1)
print("Timer finished!")
```