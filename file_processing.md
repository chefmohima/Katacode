### Reading csv files
use the csv module
Suppose we have the below file f1.csv

Symbol,Price,Date,Time,Change,Volume
"AA",39.48,"6/11/2007","9:36am",-0.18,181800
"AIG",71.38,"6/11/2007","9:36am",-0.15,195500
"AXP",62.58,"6/11/2007","9:36am",-0.46,935000
"BA",98.31,"6/11/2007","9:36am",+0.12,104800
"C",53.08,"6/11/2007","9:36am",-0.25,360900
"CAT",78.29,"6/11/2007","9:36am",-0.23,225400


```python
# read using csv.read() method.Each row is read into an array
# access each cell by index
>>> import csv
>>> with open("f1.csv", 'r') as f1:
...     f1_csv = csv.reader(f1)
...     for row in f1_csv:
...         print(row)                                  # access cell values with index, ex: row[0], row[1] etc.
... 
['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800']
['AIG', '71.38', '6/11/2007', '9:36am', '-0.15', '195500']
['AXP', '62.58', '6/11/2007', '9:36am', '-0.46', '935000']
['BA', '98.31', '6/11/2007', '9:36am', '+0.12', '104800']
['C', '53.08', '6/11/2007', '9:36am', '-0.25', '360900']
['CAT', '78.29', '6/11/2007', '9:36am', '-0.23', '225400']
```

using dictReader the cell values can be mapped to respective header column names in the form of a dictionary where the keys are the header row elements

```python
>>> with open("f1.csv", 'r') as f1:
...     f_dict = csv.DictReader(f1)
...     for row in f_dict:
...         print(row["Symbol"], row["Date"])
... 
AA 6/11/2007
AIG 6/11/2007
AXP 6/11/2007
BA 6/11/2007
C 6/11/2007
CAT 6/11/2007
```






