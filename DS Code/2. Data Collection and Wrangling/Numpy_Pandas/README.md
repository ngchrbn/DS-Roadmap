# NumPy and Pandas

## Definition and Usage

1. NumPy: "Numerical Python" is used when working with numerical data. In data analysis, it is used as a container for data to be passed between algorithms and libraries.
2. Pandas: "Panel Data" provides high-level data structures and functions designed to make working with structured or tabular data fast, easy, and expressive.

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

    In [1]: import numpy as np

    # Generate some random data
    In [2]: data = np.random.randn(2, 3)

    In [3]: data
    Out [3]:
    array([[-0.2047, 0.4789, -0.5194],
    [-0.5557, 1.9658, 1.3934]])

I then write mathematical operations with **data**:

    In [4]: data * 10
    Out [4]:
    array([[ -20471, 4.7894, -5.1944],
    [-5.5573, 19.6578, 13.9341]])

    In [5]: data + data
    Out [5]:
    array([[-0.4094, 0.9579, -1.0389],
    [-1.1115, 3.9316, 2.7868]])

An ndarray is a generic multidimensional container for homogeneous data; that is, **all
of the elements must be the same type**. Every array has a **shape** , a _tuple indicating the
size of each dimension_, and a **dtype** , _an object describing the data type of the array_:

Example:

    In [6]: data.shape
    Out[6]: (2, 3)

    In[7]: data.type
    Out[7]: dtype('float64')

#### Creating ndarrays

The easiest way to create an array is to use the **array** function. This _accepts any
sequence-like object (including other arrays) and produces a new NumPy array con‐
taining the passed data_.

Example:

    In [8]: data1 = [6, 7.5, 8, 0, 1]

    In [9]: arr1 = np.array(data1)

    In [10]: arr1
    Out[10]: array([6, 7.5, 8., 0. 1.])

Nested sequences, like a list of equal-length lists, will be converted into a multidimen‐
sional array:

    In [11]: data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

    In [12]: arr2 = np.array(data2)

    In [13]: arr2
    Out[13]:
    array([[1, 2, 3, 4],
    [5, 6, 7, 8]])

Since **data2** was a list of lists, the NumPy array **arr2** has two dimensions with shape
inferred from the data. We can confirm this by inspecting the **ndim** and **shape**
attributes:

    In [14]: arr2.ndim
    Out[14]: 2

    In [15]: arr2.shape
    Out[15]: (2, 4)

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
    Out [19]: array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

❗ It’s not safe to assume that **np.empty** will return an array of all
zeros. In some cases, it may return uninitialized “garbage” values.

#### Data Types for ndarrays

The _data type_ or **dtype** is a special object containing the information (or _metadata_,
data about data) the ndarray needs to interpret a chunk of memory as a particular
type of data.

    In [20]: arr1 = np.array([1, 2, 3], dtype=np.float64)

    In [21]: arr2 = np.array([1, 2, 3], dtype=np.int32)

    In [22]: arr1.dtype
    Out[22]: dtype('float64')

    In [23]: arr2.dtype
    Out[23]: dtype('int32')

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
- **float16 (f2)**: ger types
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

    In [24]: arr = np.array([1, 2, 3, 4, 5])

    In [25]: arr.dtype
    Out[25]: dtype('int64')

    In [26]: float_arr = arr.astype(np.float64)

    In [27]: float_arr.dtype
    Out[27]: dtype('float64')

- In this example, integers were cast to floating point. If I cast some floating-point
numbers to be of integer dtype, the decimal part will be truncated.
- If you have an array of strings representing numbers, you can use astype to convert
them to numeric form.

❗ It’s important to be cautious when using the **numpy.string_** type,
as string data in NumPy is fixed size and may truncate input
without warning. pandas has more intuitive out-of-the-box behav‐
ior on non-numeric data.

You can also use another array’s dtype attribute and for dtype, you can use the type code:

    In [28]: empty_uint32 = np.empty(8, dtype='u4')

📢 Calling **astype** always creates a new array (a copy of the data), even
if the new dtype is the same as the old dtype.

#### Arithmetic with NumPy Arrays
