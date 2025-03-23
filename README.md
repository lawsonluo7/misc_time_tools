# Misc Time Tools

This repository contains miscellanious Python tools for working with time and dates.

## Usage

Here are some examples of how to use the tools in this repository:

### Example 1

```python
from misc_time_tools import Stopwatch

t = Stopwatch()
print(t*100)
```
Behaves a lot like a `float`, but each time you acess it, it dynamically changes the time.
It has `start()`, `stop()`, `reset()` and `restart()`
Keep in mind that after calling `stop()` you can't resume.

###### `restart()` vs `reset()`
`restart()` runs `reset()` and `start()` together