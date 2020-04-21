# Python data structures

# Recipe1 : Unpacking sequences into variables
# number and order should match when unpacking

>>> data
['ACME', 50, 91.1, (2012, 12, 21)]
>>> name, share, price, date = data
>>> print('Name: {}, Share: {}, Price: {}, Date: {}'.format(name, share, price, date))
Name: ACME, Share: 50, Price: 91.1, Date: (2012, 12, 21)

# If we want to split the date further:
>>> name, share, price, (year, month, day) = data
>>> print('Date: {}/{}/{}'.format(year, month, day))
Date: 2012/12/21

# Throwaway variable: when unpacking if there are certain values we dont need replace them with
# _. Example if we dont want the date value from data replace with _ when unpacking
>>> data
['ACME', 50, 91.1, (2012, 12, 21)]
>>> name, share, price, _ = data
>>> print(name, share, price)
ACME 50 91.1

# Any iterable can be unpacked including strings
# get the first and last characters from the string 'hello'
>>> c1, _, _, _, c2 = 'hello'
>>> print(c1, c2)
h o

# Recipe 2 : using * for unpacking
# Unpack iterables of ARBITRARY lengths with *
# Suppose we have this record of an employee with multiple contact numbers
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# fetch all the contact numbers with *
name, email, *phone_numbers = record
print(phone_numbers)
['773-555-1212', '847-555-1212']

# * will eat up N number of variables into a list
# using the * unpacking with split to fetch data
# Suppose we have this line of data
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# Fetch the username, directory and shell name from the line
>>> username, *middle_fields, dir, shell = line.split(':')
>>> print(username,  dir,  shell)
nobody /var/empty /usr/bin/false


# throwaway multiple values with _*
# In the data below fetch just the name and year
>>> record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
>>> name
'ACME'
>>> year
2012

# Recipe 3: find N largest/ N smallest items in a sequence with heapq
import heapq
>>> nums = [100,10,30,90,40,60,1]
>>> heapq.nlargest(2, nums)
[100, 90]
>>> heapq.nsmallest(2, nums)

# using heapq nlargest/nsmallest with key
>>> num = [-1,3,2,1,4,2,-3,-5,-10]
>>> heapq.nlargest(2, num)
[4, 3]
# notice how the result changes when we use a key
# In the below example, when we use key 
# we are using list of squares to compute the values
>>> heapq.nlargest(2, num, key=lambda s:s**2)


# Recipe 4: Map keys to multiple values in a dictionary
# we can either use a normal dictionary and initialize every key value to an empty list
# or use defaultdict(list) where key values will be list by default and do not need to be initialized

# normal dicts
>>> map1 = {}
>>> map1['key1'] = []       # this initialization is required
>>> map1['key1'].append('a')
>>> map1['key1'].append('b')
>>> map1
{'key1': ['a', 'b']}

# dafultdict(list)
>>> from collections import defaultdict
>>> map2 = defaultdict(list)
>>> map2['key1'].append('a')    # no initialization needed
>>> map2['key1'].append('b')
>>> map2
defaultdict(<class 'list'>, {'key1': ['a', 'b']})
[-10, -5]

# Recipe 5: ordering dictionary entries with OrderedDict
# using an OrderedDict will preserve the order of insertion of items into the dictionary
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
    
# Recipe 6: perform calculations on dict VALUES and do reverse lookup
# usually we use dicts to look up using keys, however sometimes
# we may need to do a reverse lookup or find values with ceratin key
# to do this we can invert the dict with zip() function
# this converts key: value pair to value:key pair

# Normal function of zip is to pair up values one by one from N iterables
>>> list(zip(['a', 'b', 'c'],[1,2,3],['x','y','z']))
[('a', 1, 'x'), ('b', 2, 'y'), ('c', 3, 'z')]

# invert key value pairs with zip
>>> prices = {
...    'ACME': 45.23,
...    'AAPL': 612.78,
...    'IBM': 205.55,
...    'HPQ': 37.20,
...    'FB': 10.75
... }

>>> list(zip(prices.values(), prices.keys()))
[(45.23, 'ACME'), (612.78, 'AAPL'), (205.55, 'IBM'), (37.2, 'HPQ'), (10.75, 'FB')]

# find product with minimum price
>>> min(zip(prices.values(), prices.keys()))
(10.75, 'FB')

# sort dictionary by value
>>> sorted(zip(prices.values(), prices.keys()))
[(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

# Computing on dict values without using zip
# can use the key value to calculate min/max values in a dict
>>> prices = {
...    'ACME': 45.23,
...    'AAPL': 612.78,
...    'IBM': 205.55,
...    'HPQ': 37.20,
...    'FB': 10.75
... }

>>> min(prices)       # this computes the minimum value among the dict keys and not value
'AAPL'

# to change this behavior use the key parameter
min(prices, key = lamda k: prices[k])
'FB'                                 # this finds the key with minimum value

# to find the correspnding value:
prices[min(prices, key = lamda k: prices[k])]
10.75

# Recipe 7: find common elements in dictionaries
>>> a = {
...    'x' : 1,
...    'y' : 2,
...    'z' : 3
... }
>>>
>>> b = {
...    'w' : 10,
...    'x' : 11,
...    'y' : 2
... }
>>> a.keys() & b.keys()     # find common keys
{'x', 'y'}
>>> a.keys() - b.keys().    # find keys in a that are not in b
{'z'}
>>> a.items() - b.items().  # find unique key values pairs from both dicts, the key 'y' has same value and hence removed
{('x', 1), ('z', 3)}


# Recipe 8: Remove duplicate values from a sequence but preserve order of sequence
>>> a
[1, 5, 2, 1, 9, 1, 5, 10]
>>> set(a)
{1, 2, 5, 9, 10}          # notice that duplicates removed BUT order has changed

# instead use this method to preserve the order of elements
>>> s = set()
>>> for item in a:
...     if item not in s:
...         print(item)
...         s.add(item)
...
1
5
2
9
10


# Recipe 9: 













