# Misc Time Tools

This repository contains miscellanious Python tools for working with time and dates.

## StopWatch
### Usage

Class name seems self explanatory
Acess time with Stopwatch.elapsed
If you want to quickly acess the value just print it directly
It has `start()`, `pause()`, `reset()` and `restart()`

#### restart vs reset
`restart()` runs `reset()` and `start()` together

Here are some examples of how to use the tools in this class:

#### Example 1

```python
from misc_time_tools import Stopwatch

t = Stopwatch()
print(t)
print(type(t))
print(type(t.elapsed))
```