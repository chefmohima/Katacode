### Recipe 1: split strings on multiple delimeters. 
We know that we can split a string with the string.split(delimeter) method but we can use only 1 delimiting character.
If we need to split a string on multiple delimters then use the re.split() method

```python
line = 'asdf fjdk; afed, fjek,asdf,      foo'
import re
# re.split(delimeter(s), string_to_split)
re.split(r'[;,\s]\s*', line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# OR compile the pattern and then split
pattern = re.compile(r'[;,\s]\s*')
pattern.split(line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
```
