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

### Recipe 2: check start/end of string for a specific pattern
use the str.startswith() or str.endswith()
Example: given a directory with the following files, print the files that are either txt or xml
['f1.txt', 'f2.txt', 'f4.xml', 'f3.html']

```python
for f in os.listdir("."):
    if f.endswith(('txt', 'xml')): # notice for multiple matches, startswith/endswith will take a tuple as input
        print(f)
# output
f1.txt
f2.txt
f4.xml
```

### Alternatively use the regex with anchor tags ^ for start and $ for end , | for multiple matching
```python
>>> import re
>>> for f in os.listdir("."):
...     if re.search(r'txt|xml$', f):
...         print(f)
... 
f1.txt
f2.txt
f4.xml
```


