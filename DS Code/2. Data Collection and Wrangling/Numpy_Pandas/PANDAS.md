# Pandas

## Introduction

Pandas contains **data structures and data manipulation tools designed to make data cleaning and analysis fast and easy in Python**.
The big difference between **pandas** and **NumPy** is that _pandas is designed for working with tabular or heterogeneous data_ whereas _NumPy is best suited for working with homogeneous numerical array data_.

## Import convention

- To import pandas

```python
    In [1]: import pandas as pd
```

- To import Series and DataFrame (If you want to use them only)

```python
    In [2]: from pandas import Series, DataFrame
```

## pandas Data Structures

### Series

- A Series is a _one-dimensional array-like object containing a sequence of values_ (of similar types to NumPy types) and _an associated array of data labels, called its_ **index**.
- Another way to think about a Series is as _a fixed-length, ordered dict_, as it is a mapping of index values to data values.

```python
    In [3]: obj = pd.Series([4, 7, -5, 3])

    In [4]: obj
    Out[4]:
    0   4
    1   7
    2  -5
    3   3
    dtype: int64
```

- This representation shows the _index on the left_ and the _values on the right_. Since we did not specify an index for the data, a _default one consisting of the integers 0 through N - 1 (where N is the length of the data) is created_.

- You can create a Series with an index(interpreted as an indice) identifying each data point with a label:

```python
    In [5]: obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

    In [6]: obj2
    Out [6]:
    d   4
    b   7
    a  -5
    c   3
    dtype: int64
```

- Values in Series can be accessed through index.

```python
    In [7]: obj2['a']
    Out [7]: -5
```

- Using NumPy functions or NumPy-like operations, such as filtering with a boolean array, scalar multiplication, or applying math functions, will preserve the index-value.

- You can create a Series with a _dict (with key-value pair)_ or _a dict(with key-value pair) and index values as a list_ and _for the list's values if there is no value for it in the dict_, the _value in the Series will be NaN_("Not a number").

- 👉🏼 When you are only passing a dict, the _index in the resulting Series will have the dict’s keys in sorted order._

```python
    In [8]: sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

    In [9]: obj3 = pd.Series(sdata)

    In [10]: obj3
    Out [10]:
    Ohio    35000
    Oregon  16000
    Texas   71000
    Utah     5000

    In [11]: states = ['California', 'Ohio', 'Oregon', 'Texas']

    In [12]: obj4 = pd.Series(sdata, index=states)

    In [13]: obj4
    Out [13]:
    California  NaN
    Ohio    35000.0
    Oregon  16000.0
    Texas   71000.0
    dtype: float64
```

- Both the Series object itself and its index have a _name_ attribute.

```python
    In [14]: obj4.name = 'population'

    In [15]: obj4.index.name = 'state'
```

- A Series’s index can be altered in-place by assignment:

```python
    In [16]: obj
    Out [16]:
    0   4
    1   7
    2  -5
    3   3
    dtype: int64

    In [17]: obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
    
    In [18]: obj
    Out [18]:
    Bob     4
    Steve   7
    Jeff   -5
    Ryan    3
    dtype: int64
```

### DataFrame
