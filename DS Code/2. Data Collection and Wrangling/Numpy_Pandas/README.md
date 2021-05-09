# NumPy and Pandas

## Definition and Usage

1. **NumPy**: "Numerical Python" is used when working with numerical data. In data analysis, it is used as a container for data to be passed between algorithms and libraries.
2. **Pandas**: "Panel Data" provides high-level data structures and functions designed to make working with structured or tabular data fast, easy, and expressive.

## A. NumPy Basics: Arrays and Vectorized Computation

==> One of the reasons NumPy is so important for numerical computations in Python is
because it is designed for efficiency on large arrays of data. There are a number of
reasons for this:

1. NumPy internally stores data in a contiguous block of memory, independent of
other built-in Python objects. NumPy’s library of algorithms written in the C lan‐
guage can operate on this memory without any type checking or other overhead.
NumPy arrays also use much less memory than built-in Python sequences.
2. NumPy operations perform complex computations on entire arrays without the
need for Python for loops.

NumPy-based algorithms are generally 10 to 100 times faster (or more) than their
pure Python counterparts and use significantly less memory.

### 1. The NumPy ndarray: A Multidimensional Array Object

One of the key features of NumPy is its N-dimensional array object, or ndarray,
which is a fast, flexible container for large datasets in Python. Arrays enable you to
perform mathematical operations on whole blocks of data using similar syntax to the
equivalent operations between scalar elements

Example:

```python
    In [1]: import numpy as np

    # Generate some random data
    In [2]: data = np.random.randn(2, 3)

    In [3]: data
    Out [3]:
    array([[-0.2047, 0.4789, -0.5194],
    [-0.5557, 1.9658, 1.3934]])
```

I then write mathematical operations with **data**:

```python
    In [4]: data * 10
    Out [4]:
    array([[ -20471, 4.7894, -5.1944],
    [-5.5573, 19.6578, 13.9341]])

    In [5]: data + data
    Out [5]:
    array([[-0.4094, 0.9579, -1.0389],
    [-1.1115, 3.9316, 2.7868]])
```

An ndarray is a generic multidimensional container for homogeneous data; that is, **all
of the elements must be the same type**. Every array has a **shape** , a _tuple indicating the
size of each dimension_, and a **dtype** , _an object describing the data type of the array_:

Example:

```python
    In [6]: data.shape
    Out[6]: (2, 3)

    In[7]: data.type
    Out[7]: dtype('float64')
```

#### Creating ndarrays

The easiest way to create an array is to use the **array** function. This _accepts any
sequence-like object (including other arrays) and produces a new NumPy array con‐
taining the passed data_.

Example:

```python
    In [8]: data1 = [6, 7.5, 8, 0, 1]

    In [9]: arr1 = np.array(data1)

    In [10]: arr1
    Out[10]: array([6, 7.5, 8., 0. 1.])
```

Nested sequences, like a list of equal-length lists, will be converted into a multidimen‐
sional array:

```python
    In [11]: data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

    In [12]: arr2 = np.array(data2)

    In [13]: arr2
    Out[13]:
    array([[1, 2, 3, 4],
    [5, 6, 7, 8]])
```

Since **data2** was a list of lists, the NumPy array **arr2** has two dimensions with shape
inferred from the data. We can confirm this by inspecting the **ndim** and **shape**
attributes:

```python
    In [14]: arr2.ndim
    Out[14]: 2

    In [15]: arr2.shape
    Out[15]: (2, 4)
```

Unless explicitly specified, np.array _tries to infer a good data
type for the array that it creates_.

##### Array creation functions

- **array**: Convert input data (list, tuple, array, or other sequence type) to an ndarray either by inferring a dtype
or explicitly specifying a dtype; copies the input data by default
- **asarray**: Convert input to ndarray, but do not copy if the input is already an ndarray
- **arange**: Like the built-in range but returns an ndarray instead of a list
- **ones, ones_like**: Produce an array of all 1s with the given shape and dtype; ones_like takes another array and
produces a ones array of the same shape and dtype
- **zeros, zeros_like**: Like ones and ones_like but producing arrays of 0s instead
- **empty, empty_like**: Create new arrays by allocating new memory, but do not populate with any values like ones and
zeros
- **full, full_like**: Produce an array of the given shape and dtype with all values set to the indicated “fill value”. full_like takes another array and produces a filled array of the same shape and dtype
- **eye, identity**: Create a square N × N identity matrix (1s on the diagonal and 0s elsewhere)

Examples:

```python
    In [16]: np.zeros(10)
    Out[29]: array([ 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

    In [17]: np.zeros((3, 6))
    Out [17]: 
    array([[0.,0., 0., 0., 0., 0.,],
    [0.,0., 0., 0., 0., 0.,],
    [0.,0., 0., 0., 0., 0.,]])

    In [18]: np.empty((2, 3, 2))
    Out [18]:
    array([[[ 0., 0.],
            [ 0., 0.],
            [ 0., 0.]],
           [[ 0., 0.],
            [ 0., 0.],
            [ 0., 0.]]])

    In [19]: np.arange(15)
    Out [19]: 
    array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
```

❗ It’s not safe to assume that **np.empty** will return an array of all
zeros. In some cases, it may return uninitialized “garbage” values.

#### Data Types for ndarrays

The _data type_ or **dtype** is a special object containing the information (or _metadata_,
data about data) the ndarray needs to interpret a chunk of memory as a particular
type of data.

```python
    In [20]: arr1 = np.array([1, 2, 3], dtype=np.float64)

    In [21]: arr2 = np.array([1, 2, 3], dtype=np.int32)

    In [22]: arr1.dtype
    Out[22]: dtype('float64')

    In [23]: arr2.dtype
    Out[23]: dtype('int32')
```

dtypes are a source of NumPy’s flexibility for interacting with data coming from other
systems. In most cases they provide a mapping directly onto an underlying disk or
memory representation, which makes it easy to read and write binary streams of data
to disk and also to connect to code written in a low-level language like C or Fortran.

📍 The numerical dtypes are named the same way: a type name, like float or int , followed by a number indicating the number of bits per element.

##### Numpy Data Types

- **int8, uint8 (i1, u1)**: Signed and unsigned 8-bit (1 byte) integer types
- **int16, uint16 (i2, u2)**: Signed and unsigned 16-bit integer types
- **int32, uint32 (i4, u4)**: Signed and unsigned 32-bit integer types
- **int64, uint64 (i8, u8)**: Signed and unsigned 64-bit integer types
- **float16 (f2)**: Half-precision floating point
- **float32 (f4 or f)**: Standard single-precision floating point; compatible with C float
- **float64 (f8 or d)**: Standard double-precision floating point; compatible with C double and
Python float object
- **float128 (f16 or g)**: Extended-precision floating point
- **complex64 ,
complex128 ,
complex256 (c8, c16,
c32)**: Complex numbers represented by two 32, 64, or 128 floats, respectively
- **bool (?)**: Boolean type storing True and False values
- **object (O)**: Python object type; a value can be any Python object
- **string_ (S)**: Fixed-length ASCII string type (1 byte per character); for example, to create a
string dtype with length 10, use 'S10'
- **unicode_(U)**: Fixed-length Unicode type (number of bytes platform specific); same
specification semantics as string_ (e.g., 'U10' )

👉🏼 **Those in parentheses are the type code**

You can explicitly convert or cast an array from one dtype to another using ndarray’s
**astype** method:

```python
    In [24]: arr = np.array([1, 2, 3, 4, 5])

    In [25]: arr.dtype
    Out[25]: dtype('int64')

    In [26]: float_arr = arr.astype(np.float64)

    In [27]: float_arr.dtype
    Out[27]: dtype('float64')
```

- In this example, integers were cast to floating point. If I cast some floating-point
numbers to be of integer dtype, the decimal part will be truncated.
- If you have an array of strings representing numbers, you can use astype to convert
them to numeric form.

❗ It’s important to be cautious when using the **numpy.string_** type,
as string data in NumPy is fixed size and may truncate input
without warning. pandas has more intuitive out-of-the-box behav‐
ior on non-numeric data.

You can also use another array’s dtype attribute and for dtype, you can use the type code:

```python
    In [28]: empty_uint32 = np.empty(8, dtype='u4')
```

📢 Calling **astype** always creates a new array (a copy of the data), even
if the new dtype is the same as the old dtype.

#### Arithmetic with NumPy Arrays

Arrays are important because they enable you to express batch operations on data
without writing any for loops. NumPy users call this vectorization. Any arithmetic
operations between equal-size arrays applies the operation element-wise.

```python
    In [29]: arr = np.array([[1., 2., 3.], [4., 5., 6.]])

    In [30]: arr
    Out[30]:
    array([[ 1., 2., 3.],
        [ 4., 5., 6.]])

    In [31]: arr * arr
    Out [31]:
    array([[ 1.,4., 9.],
    [ 16., 25., 36.]])

    In [32]: arr - arr
    Out [32]:
    array([[0., 0., 0.],
        [0., 0., 0.]])
```

- Arithmetic operations with scalars propagate the scalar argument to each element in
the array;
- Comparisons between arrays of the same size yield boolean arrays;

📢 Operations between differently sized arrays is called **broadcasting**.

#### Basic Indexing and Slicing

- NumPy array indexing is a rich topic, as there are many ways you may want to select a subset of your data or individual elements. One-dimensional arrays are simple; on the surface they act similarly to Python lists.
- An important first distinction from Python’s built-in lists is that array slices are **views** on the original array. This _means that the data is not copied_, and _any modifications to the view will be reflected in the source array_.

Example:

```python
    In [33]: arr = np.arange(10)

    In [34]: arr_slice = arr[5:8]

    In [35]:arr_slice
    Out [35]: array([12, 12, 12])

    # Now, when i change values in arr_slice, the
    # mutations are reflected in the original array arr:
    In [36]: arr_slice[1] = 12345

    In [37]: arr
    Out [37]: array([0, 1, 2, 3, 4, 12, 12345, 12, 8, 9])

    # The "bare" slice [:] will assign to all values in
    # an array:
    In [38]: arr_slice[:] = 64

    In [39]: arr
    Out [39]: array([0, 1, 2, 3, 4, 64, 64, 64, 8, 9])
```

📢 If you want a copy of a slice of an ndarray instead of a view, you will need to explicitly copy the array—for example, _**arr[5:8].copy()**_.

- With higher dimensional arrays, you have many more options. In a two-dimensional array, the elements at each index are no longer scalars but rather one-dimensional arrays;

```python
    In [40]: arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    In [41]: arr2d[2]
    Out [41]: array([7, 8, 9])
```

- Thus, individual elements can be accessed recursively. But that is a bit too much work, so you can pass a comma-separated list of indices to select individual elements. So these are equivalent;

```python
    In [42]: arr2d[0][2]
    Out [42]: 3

    In [43]: arr2d[0, 2]
    Out [43]: 3
```

- You also can pass multiple slices just like you can pass multiple indexes.

```python
    In [44]: arr2d[:2, 1:]
    Out [44]:
    array([[2, 3],
        [5, 6]])
```

- Of course, assigning to a slice expression assigns to the whole selection.

```python
    In [45]: arr2d[:2, 1:] = 0

    In [46]: arr2d
    Out [46]:
    array([[1, 0, 0],
        [4, 0, 0],
        [7, 8, 9]])
```

#### Boolean Indexing

- Let’s consider an example where we have some data in an array and an array of names with duplicates.

```python
    In [47]: names = np.array(['Bob', 'Joe', 'Will', 'Joe', 'Joe'])

    In [48]: data = np.random.randn(7, 4)

    In [49]: names
    Out [49]:
    array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'], dtype='<U4')

    In [50]: data
    Out [50]:
    array([[ 0.0929, 0.2817, 0.769 , 1.2464],
            [ 1.0072, -1.2962, 0.275 , 0.2289],
            [ 1.3529, 0.8864, -2.0016, -0.3718],
            [ 1.669 , -0.4386, -0.5397, 0.477 ],
            [ 3.2489, -1.0212, -0.5771, 0.1241],
            [ 0.3026, 0.5238, 0.0009, 1.3438],
            [-0.7135, -0.8312, -2.3702, -1.8608]])
```

- Suppose each name corresponds to a row in the data array and we wanted to select all the rows with corresponding name 'Bob' . Like arithmetic operations, comparisons (such as == ) with arrays are also vectorized. Thus, comparing names with the string 'Bob' yields a boolean array.

```python
    In [51]: names == 'Bob'
    Out [51]: array([True, False, False, True, False, False, False], dtype=bool)

    # This boolean array can be passed when indexing
    # the array
    In [52]: data[names == 'Bob']
    Out [52]:
    array([[ 0.0929, 0.2817, 0.769, 1.2464],
        [1.669 , -0.4386, -0.5397, 0.477]])
```

- The boolean array must be of the same length as the array axis it’s indexing. You can
even mix and match boolean arrays with slices or integers.

❗ Boolean selection will not fail if the boolean array is not the correct length.

- More examples:

```python
    In [53]: data[names == 'Bob', 2:]
    Out [53]:
    array([[0.769, 1.2464],
        [-0.5397, 0.477]])

    In [54]: data[names == 'Bob', 3]
    Out [54]: array([1.2464, 0.477])

    # To select everythin but 'Bob', you can either use
    # != or negate the condition using ~:
    In [55]: names != 'Bob'
    Out [55]: array([False, True, True, False, True, True, True], dtype=bool)

    In [56]: data[~(names == 'Bob')]
    Out [56]:
    array([ [ 1.0072, -1.2962, 0.275 , 0.2289],
            [ 1.3529, 0.8864, -2.0016, -0.3718],
            [ 3.2489, -1.0212, -0.5771, 0.1241],
            [ 0.3026, 0.5238, 0.0009, 1.3438],
            [-0.7135, -0.8312, -2.3702, -1.8608]])    

```

- The **~** operator can be useful when you want to invert a general condition.

- You can ue arithmetic operators like & and | to combine multiple conditions:

```python
    In [57]: mask = (names == 'Bob') | (names == 'Will')

    In [58]: mask
    Out [58]: array([True, False, True, True, True, False, False], dtype=bool)

    In [59]: data[mask]
    Out [59]:
    array([[ 0.0929, 0.2817, 0.769 , 1.2464],
            [ 1.3529, 0.8864, -2.0016, -0.3718],
            [ 1.669 , -0.4386, -0.5397, 0.477 ],
            [ 3.2489, -1.0212, -0.5771, 0.1241]])
```

📢 Selecting data from an array by boolean indexing always creates a copy of the data, even if the returned array is unchanged.

❗ The Python keywords **and** and **or** do not work with boolean arrays. Use **&** (and) and **|** (or) instead.

- Setting values with boolean arrays works in a common-sense way.

#### Fancy Indexing

- **Fancy indexing** is a term adopted by NumPy to describe indexing using integer arrays.

```python
    In [60]: arr = np.empty((8, 4))

    In [61]:for i in range(8):
                arr[i] = i

    In [62]: arr
    Out [63]:
    array([[0., 0., 0., 0.],
            [1., 1., 1., 1.],
            [2., 2., 2., 2.],
            [3., 3., 3., 3.],
            [4., 4., 4., 4.],
            [5., 5., 5., 5.],
            [6., 6., 6., 6.],
            [7., 7., 7., 7.]])
```

- To select out a subset of the rows in a particular order, you can simply pass a list or ndarray of integers specifying the desired order.

```python
    In [64]: arr[[4, 3, 0, 6]]
    Out [64]:
    array([[4., 4., 4., 4.],
            [3., 3., 3., 3.],
            [0., 0., 0., 0.],
            [6., 6., 6., 6.]])
```

- Using negative indices selects rows from the end:

```python
    In [65]: arr([[-3, -5, -7]])
    Out [65]:
    array([ [5., 5., 5., 5.],
            [3., 3., 3., 3.],
            [1., 1., 1., 1.],])
```

- Passing multiple index arrays does something slightly different; **it selects a one-dimensional array of elements corresponding to each tuple of indices**:

```python
    In [66]: arr = np.arange(32).reshape((8, 4))

    In [67]: arr
    array([[0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23],
            [24, 25, 26, 27],
            [28, 29, 30, 31]])
    
    In [68]: arr([[1, 5, 7, 2], [0, 3, 1, 2]])
    Out [68]: array([4, 23, 29,10])
```

❗ Regardless of how many dimensions the array has (here, only 2), the result of fancy indexing is always one-dimensional.

📢 Keep in mind that fency indexing,unlike slicing, always copies th data into a ne array.

#### Transposing Arrays and Swapping Axes

- **Transposing** is a special form of reshaping that similarly returns a view on the underlying data without copying anything.
- Arrays have the **transpose** method and also the
special **T** attribute:

```python
    In [69]: arr = np.arange(15).reshape((3, 5))

    In [70]: arr
    Out [70]:
    array([[0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14]])
    
    In [71]: arr.T
    Out [71]:
    array([[0, 5, 10],
            [1, 6, 11],
            [2, 7, 12],
            [3, 8, 13],
            [4, 9, 14]])
```

- When doing matrix computations, you may do this very often—for example, when computing the inner matrix product using **np.dot**:

```python
    In [72]: arr = np.random.randn(6, 3)

    In [73]: arr
    Out [73]:
    array([[-0.8608, 0.5601, -1.2659],
            [0.1198, -1.0635, 0.3329],
            [-2.3594, -0.1995, -1.542],
            [-0.9707, -1.307 , 0.2863],
            [0.378 , -0.7539, 0.3313],
            [1.3497, 0.0699, 0.2467]])

    In [74]: np.dot(arr.T, arr)
    Out [74]:
    array([[9.2291, 0.9394, 4.948],
            [0.9394, 3.7662, -1.3622],
            [4.948 , -1.3622, 4.3437]])
```

- For higher dimensional arrays, **transpose** will accept a _tuple of axis numbers to permute the axes_ (for extra mind bending):

```python
    In [75]: arr = np.arange(16).reshape((2, 2, 4))

    In [76]: arr
    Out [76]:
    array([[[0, 1, 2, 3],
            [4, 5, 6, 7]],
           [[8, 9, 10, 11],
            [12, 13, 14, 15]]])

    In [77]: arr.transpose((1, 0, 2))
    Out [77]:
    array([[[ 0, 1, 2, 3],
            [ 8, 9, 10, 11]],
           [[ 4, 5, 6, 7],
            [12, 13, 14, 15]]])
```

- Here, the axes have been reordered with the second axis first, the first axis second, and the last axis unchanged.
- Simple transposing with **.T** is a special case of swapping axes. **ndarray** has the method **swapaxes** , which _takes a pair of axis numbers and switches the indicated axes to rearrange the data_:

```python
    In [78]: arr
    Out [78]:
    array([[[0, 1, 2, 3],
            [4, 5, 6, 7]],
           [[8, 9, 10, 11],
            [12, 13, 14, 15]]])
    
    In [79]: arr.swapaxes(1, 2)
    Out [79]:
    array([[[ 0, 4],
            [ 1, 5],
            [ 2, 6],
            [ 3, 7]],
           [[ 8, 12],
            [ 9, 13],
            [10, 14],
            [11, 15]]])

```

📢 **swapaxes** similarly returns a view on the data without making a copy.

### 2. Universal Functions: Fast Element-Wise Array Functions

- A **universal function**, or _ufunc_, is a function that performs element-wise operations on data in ndarrays. You can think of them as fast vectorized wrappers for simple functions that take one or more scalar values and produce one or more scalar results.

- Many ufuncs are simple element-wise transformations, like **sqrt** or **exp** :

```python
    In [80]: arr = np.arange(10)

    In [81]: arr
    Out [81]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    In [82]: np.sqrt(arr)
    Out [83]:
    array([0., 1., 1.4142, 1.7321, 2., 2.2361, 2.4495,
            2.6458, 2.8284, 3.])
    
    In [84]: np.exp(arr)
    Out [84]:
    array([1., 2.7183, 7.3891, 20.0855, 54.5982,
            148.4132, 403.4288, 1096.6332, 2980.958, 8103.0839])
```

- These are referred to as *unary ufuncs*. Others, such as _add_ or _maximum_ , take two arrays (thus, **binary** **ufuncs**) and return a single array as the result.
- While not common, a ufunc can return _multiple arrays_. **modf** is one example, a vectorized version of the built-in Python divmod ; it _returns the fractional and integral parts of a floating-point array_
- Ufuncs accept an optional **out** argument that allows them to _operate in-place on arrays_:

```python
    In [85]: arr
    Out [85]: array([-3.2623, -6.0915, -6.663 , 5.3731, 3.6182, 3.45 , 5.0077])

    In [86]: np.sqrt(arr)
    Out [86]: array([nan, nan, nan, 2.318 , 1.9022, 1.8574, 2.2378])

    In [87]: np.sqrt(arr, arr)
    Out [87]: array([nan, nan, nan, 2.318 , 1.9022, 1.8574, 2.2378])

    In [88]: arr
    Out [88]: array([nan, nan, nan, 2.318 , 1.9022, 1.8574, 2.2378])
```

#### Unary ufuncs

- **abs, fabs**: Compute the absolute value element-wise for integer, floating-point, or complex values;
- **sqrt**: Compute the square root of each element (equivalent to arr ** 0.5 );
- **square**: Compute the square of each element (equivalent to arr ** 2 );
- **exp**: Compute the exponent of each element;
- **log, log10, log2, log1p**: Natural logarithm (base e), log base 10, log base 2, and log(1 + x), respectively;
- **sign**: Compute the sign of each element: 1 (positive), 0 (zero), or –1 (negative);
- **ceil**: Compute the ceiling of each element (i.e., the smallest integer greater than or equal to that
number);
- **floor**: Compute the floor of each element (i.e., the largest integer less than or equal to each element);
- **rint**: Round elements to the nearest integer, preserving the dtype;
- **modf**: Return fractional and integral parts of array as a separate array;
- **isnan**: Return boolean array indicating whether each value is NaN (Not a Number);
- **isfinite, isinf**: Return boolean array indicating whether each element is finite (non- inf , non- NaN ) or infinite,respectively;
- **cos, cosh, sin, sinh, tan, tanh**: Regular and hyperbolic trigonometric functions;
- **arccos, arccosh, arcsin, arcsinh, arctan, arctanh**: Inverse trigonometric functions;
- **logical_not**: Compute truth value of not x element-wise (equivalent to ~arr ).

#### Binary Universal Functions

- **add**: Add corresponding elements in arrays;
- **subtract**: Subtract elements in second array from first array;
- **multiply**: Multiply array elements;
- **divide, floor_divide**: Divide or floor divide (truncating the remainder);
- **power**: Raise elements in first array to powers indicated in second array;
- **maximum, fmax**: Element-wise maximum; fmax ignores NaN;
- **minimum, fmin**: lement-wise minimum; fmin ignores NaN;
- **mod**: Element-wise modulus (remainder of division)
- **copysign**: Copy sign of values in second argument to values in first argument;
- **greater, greater_equal, less, less_equal, equal, not_equal**: Perform element-wise comparison, yielding boolean array (equivalent to infix
operators >, >=, <, <=, ==, != );
- **logical_and, logical_or, logical_xor**: Compute element-wise truth value of logical operation (equivalent to infix operators
& |, ^ );

### 3. Array-Oriented Programming with Arrays
