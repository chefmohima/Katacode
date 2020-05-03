# Recipe 1: split strings on multiple delimeters. 
We know that we can split a string with the string.split(delimeter) method but we can use only 1 delimiting character.
If we need to split a string on multiple delimters then use the re.split() method

```python
line = 'asdf fjdk; afed, fjek,asdf,      foo'
import re
re.split(r'[;,\s]\s*', line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
```
