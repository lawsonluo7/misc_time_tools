# Misc Time Tools

This repository contains miscellanious Python tools for working with time and dates.

## Usage

Behaves a lot like a `float`, but each time you do math operations on it, or print it, it dynamically changes the time.
It has `start()`, `pause()`, `reset()` and `restart()`

###### `restart()` vs `reset()`
`restart()` runs `reset()` and `start()` together

Here are some examples of how to use the tools in this repository:

### Example 1

```python
from misc_time_tools import Stopwatch

t = Stopwatch()
print(t*100)
```