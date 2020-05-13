### Ternary operator equivalent
Syntax: result1 if condition is True else result2
```python
>>> def test_ternary(x):
...     return x*x if x <= 5 else x*3
... 
>>> test_ternary(5)
25
>>> test_ternary(6)
18
```

### check if a file exists
```python
>>> import os.path
>>> os.path.isfile('/home/cloud_user/.config')
False
>>> os.path.isdir('/home/cloud_user/.config')
True
```

### reading a file
testfile
---------
Random Content
Line 1 this is line1
Line 2 this is line2
Line 3 this is line3
Line 4 this is line4

#### read all contents in file buffer till EOF
```python
>>> with open("testfile") as f:
...     content = f.read()
...
>>> print(content)
```
Random Content
Line 1 this is line1
Line 2 this is line2
Line 3 this is line3
Line 4 this is line4


#### read n characters only
```python
# read() method accepts an argument to limit the number of characters read, 
# by default it will read till EOF if this argument is not provided
>>> with open("testfile") as f:
...     first_ten_chars = f.read(10)
... 
>>> print(first_ten_chars)
Random Con
```
#### read the whole file line by line
```python
# Method 1: iterate over the file handle, this will read one line at a time and is recommended
>>> with open("testfile") as f:
...     for line in f:
...         print(line)
... 
```
Random Content

Line 1 this is line1

Line 2 this is line2

Line 3 this is line3

Line 4 this is line4


```python
# Method 2: use readline(), readline() reads each line till newline:\n
>>> with open("testfile") as f:
...     line = f.readline()
...     while line:
...         print(line)
...         line = f.readline()
... 

```
Random Content

Line 1 this is line1

Line 2 this is line2

Line 3 this is line3

Line 4 this is line4

```python
# same as Method2 - different looping
>>> with open("testfile") as f:
...     while True:
...         line = f.readline()
...         if not line:
...             break
...         print(line)
... 
```
Random Content

Line 1 this is line1

Line 2 this is line2

Line 3 this is line3

Line 4 this is line4

#### make a list of all lines in the file
```python
# readlines() returns a list where each item is a line in the file
>>> lines = []
>>> with open("testfile") as f:
...     lines = f.readlines()
... 
>>> print(lines)
```
['Random Content\n', 'Line 1 this is line1\n', 'Line 2 this is line2\n', 'Line 3 this is line3\n', 'Line 4 this is line4\n', '\n']


### return first line from a file that has n characters, None if there is no such line
```python
    def get_line(file, char_count):
    # return first line from file that has n characters
    with open(file) as f:
        for line in f:
            line = line.strip()
            if len(line) == char_count:
                return line
    return None


l = get_line("testfile", 20)
print(l)
```










