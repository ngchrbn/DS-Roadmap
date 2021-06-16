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

#### Definition

- A Series is a _one-dimensional array-like object containing a sequence of values_ (of similar types to NumPy types) and _an associated array of data labels, called its_ **index**.
- Another way to think about a Series is as _a fixed-length, ordered dict_, as it is a mapping of index values to data values.

#### Constructing a Series

- Passing a list of values:

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

❗ This representation shows the _index on the left_ and the _values on the right_. Since we did not specify an index for the data, a _default one consisting of the integers 0 through N - 1 (where N is the length of the data) is created_.

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

- You can create a Series with a _dict (with key-value pair)_ or _a dict(with key-value pair) and index values as a list_ and _for the list's values if there is no value for it in the dict_, the _value in the Series will be NaN_("Not a number").

👉🏼 When you are only passing a dict, the _index in the resulting Series will have the dict’s keys in sorted order._

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

#### Accesing values and Operations on values

- Values in Series can be accessed through index.

```python
    In [7]: obj2['a']
    Out [7]: -5
```

- Using NumPy functions or NumPy-like operations, such as filtering with a boolean array, scalar multiplication, or applying math functions, will preserve the index-value.

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

#### DataFrame Definition

- A DataFrame represents a **rectangular table of data and contains an ordered collection of columns**, _each of which can be a different value type (numeric, string,
boolean, etc.)_,
- The DataFrame has _both a row and column index_; it can be thought of as a dict of Series all sharing the same index.
- Under the hood, the data is stored as _one or more two-dimensional blocks_ rather than a list, dict, or some other collection of one-dimensional arrays.

#### How to construct a DataFrame?

- one of the most common is from a dict of equal-length lists or NumPy array:

```python
    In [19]: data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
                    'year': [2000, 2001, 2002, 2001, 2002, 2003],
                    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
                    
    In [20]: frame = pd.DataFrame(data)

    In [21]: frame
    Out [21]:
        pop     state   year
    0   1.5     Ohio    2000
    1   1.7     Ohio    2001
    2   3.6     Ohio    2002
    3   2.4   Nevada    2001
    4   2.9   Nevada    2002
    5   3.2   Nevada    2003
```

❗ Here as we didn't specify the index, the result will have _its index assigned automatically as with Series_, and the _columns are placed in sorted order_.

- If you specify a sequence of columns, the DataFrame’s columns will be arranged in that order:

```python
    In [22]: pd.DataFrame(data, columns=['year', 'state', 'pop'])
    Out [22]:
        year    state   pop
    0   2000    Ohio    1.5
    1   2001    Ohio    1.7
    2   2002    Ohio    3.6
    3   2001  Nevada    2.4
    4   2002  Nevada    2.9
    5   2003  Nevada    3.2
```

- If you pass a column that isn't contained in the dict, it will appear with missing values in the result.

- Another common form of data is a nested dict of dicts:

```python
    In [23]: pop = {'Nevada': {2001: 2.4, 2002: 2.9},
                    'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
    
    In [24]: frame3 = pd.DataFrame(pop)

    In [25]: frame3
    Out [25]:
            Nevada  Ohio
    2000       NaN  1.5
    2001       2.4  1.7
    2002       2.9  3.6
```

📍 If the nested dict is passed to the DataFrame, **pandas will interpret the outer dict keys as the columns and the inner keys as the row indices.**

##### Possible data inputs to DataFrame constructor

Type | Notes
---- | -----
**2D ndarray**| A matrix of data, passing optional row and column labels.
**dict of arrays, lists, or tuples**| Each sequence becomes a column in the DataFrame; all sequences must be the same length.
**NumPy structured/record array** | Treated as the “dict of arrays” case.
**dict of Series** | Each value becomes a column; indexes from each Series are unioned together to form the
result’s row index if no explicit index is passed.
**dict of dicts** | Each inner dict becomes a column; keys are unioned to form the row index as in the “dict of
Series” case.
**List of dicts or Series** | Each item becomes a row in the DataFrame; union of dict keys or Series indexes become the DataFrame’s column labels.
**List of lists or tuples** | Treated as the “2D ndarray” case.
**Another DataFrame** | The DataFrame’s indexes are used unless different ones are passed.
**NumPy MaskedArray** | Like the “2D ndarray” case except masked values become NA/missing in the DataFrame result.

#### Operations On DataFrame

- For large DataFrames, the **head** method _selects only the first five rows_.

- A column in a DataFrame can be retrieved as a Series either by dict-like notation or by attribute:

```python
    In [26]: frame['state']

    // Or
    In [27]: frame.state
    // data in the column state...
```

- Rows can also be retrieved by position or name with a special **loc** atribute.

```python
    In [28]: frame.loc[0]
```

- Columns can be modified by _assignment_.
- _When you are assigning lists or arrays to a column, the value’s length must match the length of the DataFrame._
- If you assign a **Series**, its _labels will be realigned exactly to the DataFrame’s index, inserting missing values in any holes._
- Assign a column that doesn't exist will create a new column. The **del** keyword will delete columns as with a dict. But it **has to be created with dick-like notation** (as seen above).
- You can _transpose the DataFrame_ (swap rows and columns) with similar syntax to a NumPy array.
- The _keys in the inner dicts are combined and sorted to form the index in the result_. This **isn’t true if an explicit index is specified**.
- If a DataFrame’s _index and columns have their name attributes set, these will also be displayed_.
- As with Series, the **values** attribute _returns the data contained in the DataFrame as a two-dimensional ndarray_.

### Index Objects

#### Index Objects Definition

- pandas’s **Index objects** are _responsible for holding the axis labels and other metadata_ (like the axis name or names).
- Any array or other sequence of labels you use when
constructing a Series or DataFrame is internally converted to an **Index**.

```python
    In [29]: obj = pd.Series(range(3), index=['a', 'b', 'c'])

    In [30]: index = obj.index

    In [31]: index
    Out [31]: Index(['a', 'b', 'c'], dtype='object')

    In [32]: index[1:]
    Out [32]: Index(['b', 'c'], dtype='object')
```

- Index objects are immutable. Their immutability make them safer to be shared among data structures.
-In addition to being array-like, an Index also behaves like a fixed-size set, but can contain duplicate labels.

```python
    In [33]: dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])

    In [34]: dup_labels
    Out [34]: Index(['foo', 'foo', 'bar', 'bar'], dtype='object')
```

##### Some Index methods and properties

Method | Description
------ | -----------
**append** | Concatenate with additional Index objects, producing a new Index.
**difference** | Compute set difference as an Index.
**intersection** | Compute set intersection.
**union** | Compute set union.
**isin** | Compute boolean array indicating whether each value is contained in the passed collection.
**delete** | Compute new Index with element at index i deleted.
**drop** | Compute new Index by deleting passed values.
**insert** | Compute new Index by inserting element at index i.
**is_monotonic** | Returns True if each element is greater than or equal to the previous element.
**is_unique** | Returns True if the Index has no duplicate values.
**unique** | Compute the array of unique values in the Index.

## Essential Functionality

- This is a part to show the fundamentals mechanics of interacting with the data contained in a Series or DataFrame.

### Reindexing

- **reindex**: method to create a new object with the data conformed to a new index. Calling reindex on a Series rearranges the data according to the new index, _introducing missing values if any index were not already present_.

```python
    In [35]: obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])

    In [36]: obj
    Out [36]:
    d   4.5
    b   7.2
    a  -5.3
    c   3.6
    dtype: float64

    In [37]: obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
    
    In [38]: obj2
    Out [38]:
    a   -5.3
    b   7.2
    c   3.6
    d   4.5
    e   NaN
    dtype: float64
```

#### reindex function arguments

Argument | Description
---------| -----------
**index** | New sequence to use as index. Can be Index instance or any other sequence-like Python data structure. An Index will be used exactly as is without any copying.
**method** | Interpolation (fill) method; 'ffill' fills forward, while 'bfill' fills backward.
**fill_value** | Substitute value to use when introducing missing data by reindexing.
**limit** | When forward- or backfilling, maximum size gap (in number of elements) to fill.
**tolerance** | When forward- or backfilling, maximum size gap (in absolute numeric distance) to fill for inexact matches.
**level** | Match simple Index on level of MultiIndex; otherwise select subset of.
**copy** | If True , always copy underlying data even if new index is equivalent to old index; if False , do not copy the data when the indexes are equivalent.

### Dropping Entries from an Axis

- **drop**: method to return a new object with the indicated _value or values_ deleted from an axis.

```python
    In [39]: obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])

    In [40]: obj
    Out [40]:
    a   0.0
    b   1.0
    c   2.0
    d   3.0
    e   4.0
    dtype: float64

    In [41]: new_obj = obj.drop('c')

    In [42]: new_obj
    Out [43]:
    a   0.0
    b   1.0
    d   3.0
    e   4.0
    dtype: float64

    In [43]: obj.drop(['d', 'c'])
    Out [44]:
    a   0.0
    b   1.0
    e   4.0
    dtype: float64
```

📍 With DataFrame, index values can be deleted from either axis.

```python
    In [45]: data.drop('two', axis=1)
    # or
    In [46]: data.drop(['two', 'four'], axis='columns')
```

- Many functions, like **drop** , which _modify the size or shape of a Series or DataFrame_, _can manipulate an object in-place without returning a new object_.

```python
    In [47]: obj.drop('c', inplace=True)
```

❗ Be careful with the **inplace**, as it destroys any data that is dropped.

### Indexing, Selection, and Filtering

#### Indexing

- Series indexing ( obj[...] ) _works analogously to NumPy array indexing, except you can use the Series’s index values instead of only integers._
- _Slicing with labels behaves differently than normal Python slicing_ in that the _end‐point is inclusive_.
- **Setting** using these methods _modifies the corresponding section of the Series_.
- **Indexing** into a DataFrame is for _retrieving one or more columns either with a single value or sequence_.

#### Selection with loc and iloc

- **loc** and **iloc** enable you to _select a subset of the rows and columns from a DataFrame with NumPy-like notation using either axis **labels** (loc) or **integers**(iloc)._ **They are used on the rows**.

```python
    In [48]: data.loc['Colorado', ['two', 'three']]
    # Or
    In [49]: data.iloc[2, [3, 0, 1]]
    # Or
    In [50]: data.iloc[2]
```

#### Indexing options with DataFrame

Type | Notes
---- | -----
**df[val]** | Select single column or sequence of columns from the DataFrame; special case conveniences: boolean array (filter rows), slice (slice rows), or boolean DataFrame (set values based on some criterion).
**df.loc[val]** | Selects single row or subset of rows from the DataFrame by label.
**df.loc[:, val]** | Selects single column or subset of columns by label.
**df.loc[val1, val2]** | Select both rows and columns by label.
**df.iloc[where]** | Selects single row or subset of rows from the DataFrame by integer position.
**df.iloc[:, where]** | Selects single column or subset of columns by integer position.
**df.iloc[where_i, where_j]** | Select both rows and columns by integer position.
**df.at[label_i, label_j]** | Select a single scalar value by row and column label.
**df.iat[i, j]** | Select a single scalar value by row and column position (integers).
**reindex method** | Select either rows or columns by labels.
**get_value, set_value methods** | Select single value by row and column label.

### Arithmetic and Data Alignment

#### Flexible arithmetic methods

Method | Description
------ | -----------
add, radd | Method for addition(+)
sub, rsub | Method for substraction(-)
div, rdiv | Method for division(/)
floordiv, rfloordiv | Method for floor division(//)
mul, rmul | Method for multiplication(*)
pow, rpow | Method for exponentiation(**)

### Function Application and Mapping

- **apply**: method used to apply a function on one dimensional arrays to each column or row on a DataFrame.

```python
    In [51]: f = lambda x: x.max() - x.min()

    In [52]: frame.apply(f) # We already have a 'frame' DataFrame
    #...
```

👉🏼 Here the function f , which computes the difference between the maximum and minimum of a Series, is invoked once on each column in frame . The result is a Series having the columns of frame as its index.
📍 If you pass axis='columns' to apply , the function will be invoked once per row instead.

- **applymap**:  method _used to apply a function on each value of a DataFrame_. The reason for the name applymap is that Series has a **map** _method for applying an element-wise function_.

### Sorting and Ranking

- **sort_index**: method which returns a new sorted object.
- With a DataFrame, you can sort by index on either axis by giving the argument: **axis**(0[default] or 1)
- The data is _sorted in ascending order by default_, but _can be sorted in descending order with the argument_: **ascending=False**.

- To sort a Series by its values, use **sort_values** method.
📍 Any missing values are sorted to the end of the Series by default.

- When _sorting a DataFrame, you can use the data in one or more columns as the sort keys. To do so, pass one or more column names to the by option of sort_values_.

```python
    In [53]: frame.sort_values(by='b')
    # to sort by multiple columns
    In [54]: frame.sort_values(by=['a', 'b'])
```

- **Ranking** assigns ranks from one through the number of valid data points in an array.
- **rank**: method for Series and DataFrames, which by default rank breaks ties by assigning each group the mean rank.
📍 Ranks can also be assigned according to the order in which they’re observed in the data:

```python
    In [55]: obj.rank(method='first')
```

- You can rank in descending order using argument: **ascending=False**.
- DataFrame can compute ranks over the rows or the columns using argument: **axis='columns'** for column ranking.

#### Tie-breaking method with rank

Method | Description
------ | -----------
**'average'** | Default: assign the average rank to each entry in the equal group.
**'min'** | Use the minimum rank for the whole group.
**'max'** | Use the maximum rank for the whole group.
**'first'** | Assign ranks in the order the values appear in the data.
**'dense'** | Like method='min' , but ranks always increase by 1 in between groups rather than the number of equal elements in a group.

### Axis Indexs with duplicates Labels

- While many pandas functions (like **reindex** ) require that the labels be unique, it’s not mandatory.
- **is_unique**: property that tell you whether its labels are unique or not.
❗**Data selection** is one of the main things that behaves differently with duplicates. _Indexing a label with multiple entries returns a Series, while single entries return a scalar value_:

```python
    In [56]: obj['a']
    Out [56]:
    a   0
    a   1
    dtype: int64

    In [57]: obj['c']
    Out [57]: 4
```

📢 This can make your code more complicated, as the output type from indexing can vary based on whether a label is repeated or not. The same logic extends to indexing rows in a DataFrame.

## Summarizing and COmputing Descriptive Statistics
