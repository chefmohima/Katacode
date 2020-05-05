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




