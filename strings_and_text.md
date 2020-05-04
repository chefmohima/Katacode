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

### Recipe 3: find match at start or anywhere in text
-> to match at start use re.match()
-> to match anywhere in text use re.search()
-> to match a pattern mutiple times first compile the pattern with re.compile()

```python
# match date that is in the form of mm/dd/yyyy
text1 = '11/27/2012'        # this should match
text2 = 'Nov 27, 2012'.     # this should not match

# re.match(pattern, text_to_match), returns a match object if match is found otherwise None
>>> re.match(r'\d+/\d+/\d+', text1)
<re.Match object; span=(0, 10), match='11/27/2012'>
>>> re.match(r'\d+/\d+/\d+', text2)

# to get the matched text, use the matched_object.group() method
>>> mo = re.match(r'\d+/\d+/\d+', text1)
>>> mo.group()
'11/27/2012'

# capture groups : to capture different parts of the matched text use capture groups
>>> mo = re.match(r'(\d+)/(\d+)/(\d+)', text1)>>> mo.groups()
('11', '27', '2012')
>>> month, day, year = mo.groups()

# if we are going to use the same pattern multiple times, against mutiple texts then
# compile the pattern into a pattern object that can be reused
>>> pattern = re.compile(r'\d+/\d+/\d+')

# search vs match
>>> text = 'Today is 11/27/2012'
>>> pattern.match(text)                                 # no match found as pattern is not matched at the start of the text
>>> pattern.search(text)
<re.Match object; span=(9, 19), match='11/27/2012'>     # search will find a match anywhere in text
```

### Recipe 4: search and replace
use string.replace or the re.sub() method for more complex replacements

```python
# In the text below replace 'be' with 'go'
>>> text = "To be or not to be"
>>> text.replace('be', 'go')
'To go or not to go'

# In the text below, change the date format from mm/dd/yyyy to yyyy-mm-dd
# use re.sub(pattern_to_replace, replace_with, text)
>>> text = "Today is 05/05/2020"
>>> import re
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2020-05-05'                               # see how the order of the matched groups is altered in the substitution                                                     # pattern
```

### Recipe 5: case-insensitive search and replace/matching
use the re.IGNORECASE flag when using regexes for case insensitive matching

```python
>>> text = 'Uppercase HARRY Lowercase harry Mixedcase Harry'
>>> re.findall('harry', text, flags=re.IGNORECASE)
['HARRY', 'harry', 'Harry']
>>> re.sub('harry', 'Harry', text, flags=re.IGNORECASE)
'Uppercase Harry Lowercase Harry Mixedcase Harry'
```

### Recipe 6: stripping unwanted characters from strings
strip(): removes leading and trailing spaces
rstrip(: removes trailing spaces
lstrip(): removes leading spaces
```python
>>> text = "    hello    "
>>> text.lstrip()
'hello    '
>>> text.rstrip()
'    hello'
>>> text.strip()
'hello'

# can also use a character parameter for strip methods, instead of spaces it will remove the leading or trailing chars
>>> text = "****hello****"
>>> text.strip("*")

# to replace spaces from the middle of the string use str.replace()
>>> text = '   he   llo   '
>>> text.replace(" ", "")
'hello'

# to sanitize file contents when reading
>>> with open("f1.txt", 'r') as f1:
...     for line in f1:
...         l = line.strip()                # remove leading and trailing space from each line
...         print(l, len(l)
```

### Recipe 7: join strings -> array to string. split strings - > string to list
```python
# join : syntax - > delimeter.join(list_to_join) : returns a string joined with the given delimeter between each list 
#element
>>> str1 = 'Harry Potter'
>>> str2 = 'And The Prisoner of Azakaban'
>>> str3 = 'And the Goblet of Fire'
>>> str4 = 'And the Chamber of Secrets'

>>> ' '.join([str1, str2])
'Harry Potter And The Prisoner of Azakaban'
>>> ' '.join([str1, str3])
'Harry Potter And the Goblet of Fire'
>>> ' '.join([str1, str4])
'Harry Potter And the Chamber of Secrets'

# joining using a custom delimeter
>>> '***'.join([str1, str4])
'Harry Potter***And the Chamber of Secrets'

# split string: syntax - > str.split(delimeter). default delimeter is  spcae character
>>> str1
'Harry Potter'
>>> str1.split()
['Harry', 'Potter']

# to get all characters in a string use the list function
>>> str1
'Harry Potter'
>>> list(str1)
['H', 'a', 'r', 'r', 'y', ' ', 'P', 'o', 't', 't', 'e', 'r']ˇ

# using split to get values from a string
>>> url  = "https://www.google.com//search"
>>> protocol, link, resource = url.split("//")
>>> protocol
'https:'
>>> link
'www.google.com'
>>> resource
'search'







