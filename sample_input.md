#~ page_title  Advanced Python
#~ slide_title Advanced Python Programming
#~ thankyou_slide       yes
#~ thankyou_slide_title Thanks ...

# Agenda

---------

* Exception Handling in Python

* Python defining Modules & Packages

* Anonymous Functions

* map, reduce, and filter function

* Decorators

* Iterators and Generators

* Context Managers

* Monkey patching

* Multi-threading in Python

* Assignments

---

# Exception Handling in Python
---------

* What are Exceptions?

  - Exceptional Event
  - Which occurs during the execution of a program, that disrupts the normal flow of the program's instructions.
  - Something that can be handled
  - or made to be handled

--
count: false

* Error vs Exception

  - Exception - expected but irregular situations at runtime - that could be handled.
  - Error - mistakes in the running program that can be resolved only by fixing the program.

--
count: false

* Keywords involved

  - try
  - except
  - else
  - finally
  - raise

--
count: false

### That's It

---
# Exception Handling in Python
---------

Simple try-except

```python
#!/usr/bin/python3

def temp_convert(var):
   try:
      return int(var)
   except ValueError as errmsg:
      print("The argument does not contain numbers\n", errmsg)

temp_convert("xyz");
```


* `try`    - monitors block of code for exceptional case
* `except` - block of code which gets executed on specific Exceptions
---

# Exception Handling in Python
-------------------------------

```python
def temp_convert(var):
   n = 0
   try:
      if var == None:
        raise IOError("Type None passed")
      n = int(var)
   except ValueError as errmsg:
      print("Error 1:", errmsg)
   except IOError as errmsg:
      print("Error 2:", errmsg)
   else:
      print("1. would be executed, only if no Exception occurred")
   finally:
      print("2. would be executed, everytime after try block")
   return n

temp_convert("1")
temp_convert("xyz")
temp_convert(None)
```
---

# Exception Handling in Python
-------------------------------

```python
#!/usr/bin/python3

def temp_convert(var):
   n = 0
   try:
      if var == None:
        raise IOError("Type None passed")
      n = int(var)
   except Exception as errmsg:
      print("Error: Oops something went wrong:", errmsg)

   return n


temp_convert("1")
temp_convert("xyz")
temp_convert(None)
```
---

# Exception Handling in Python
-------------------------------

* `Exception` is base class for all Exception Types in Python
* excepting Base class Exception will handle all Exceptions derived from it
* Check the official page for Built-In Exception hierarchy - https://docs.python.org/3/library/exceptions.html

      ```text
      Exception
      +-- ArithmeticError
      +-- EOFError
      +-- ImportError
      +-- MemoryError
      +-- OSError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- TypeError
      +-- ValueError
      ```

---

# Exception Handling in Python
-------------------------------

Creating User defined Exception

```python
class InvalidArguementsPassed(Exception):
  def __init__(self, msg):
    self.msg = msg

def temp_convert(var):
   n = 0
   try:
      if var == None or var.isdigit() == False:
       raise InvalidArguementsPassed("var should be passed and has to be numeric")
      n = int(var)
   except InvalidArguementsPassed as errmsg:
      print("Error: Invalid args passed:", errmsg)

   return n

temp_convert("1")
temp_convert("xyz")
temp_convert(None)

```

---

# Python modules and packages
-----------------------------

* module: 

  - simply a Python source file, which can expose classes, functions and global variables.

  - imagine the following directory tree in `/usr/lib/python/site-packages`:

      ```text
      mymodule/__init__.py #this tells Python to treat this directory as a package

      mymodule/mymodule.py
      ```

  - A module is a single file (or files) that are imported under one import and used. e.g.

      ```python
      import mymodule
      ```
---

# Python modules and packages
-----------------------------

* package: simply a directory of Python module(s).


* A package is a collection of modules in directories that give a package hierarchy.

  ```python
  import my_module

  from my_package.timing.danger.internets import function_of_love
  ```

* A special file `__init__.py` differentiates a directory consisting bunch of python source files, from that of package

---
# Python modules and packages
-----------------------------

### mymodule_demo.py

```python
import mymodule

mymodule.greetme()
mymodule.greetme("abhijit")
```

### mymodule.py

```python
def greetme(name="world"):
  print("Hello", name.title(), "!!!")
```

### Files

```
mymodule_demo.py
mymodule.py
```

---

# Python modules and packages
-----------------------------

### mypackage_demo.py

```python
import mypackage

mypackage.greetme()
mypackage.greetme("abhijit")

```

### mypackage/`__init__.py`

```python
from mymodule import greetme
```

### Files

```python
mypackage_demo.py
mypackage/__init__.py
mypackage/mymodule.py
```

---

# Anonymous Functions
----------------------

* functions with no-name

* also termed as `lambda` functions

* can be used wherever function objects are required. 

* syntactically restricted to a 'single' expression. Semantically, they are just syntactic sugar for a short function definition.

* example:

  ```python
  iseven = lambda x: (x%2 == 0)

  #or
  
  def iseven(x):
        return (x%2 == 0)

  ```

---

# Anonymous Functions
----------------------

* So where it is actually required?

* To create Function object

* Used extensively in/with `map`, `reduce`, `filter` function

* and in list comprehensions!

* ex:

  ```python
  >>> n = 3
  >>> l = [i + n for i in range(10)]
  >>> print(l)
  [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  >>> print(l[3])
  6

  # with lambda:
  >>> fs = [(lambda n,i=i: i + n) for i in range(10)]
  >>> print(fs[3](3))
  6
  ```
---
# Anonymous Functions
----------------------

More examples:

```
python
>>> f = lambda d1,d2,d3: (d1*100)+(d2*10)+d3
>>> f(1,2,3)
```
what is the output?


Usage of lambda in sorted, sort function - key arg


```python
>>> heroes = [
    ('Amir', 'Khan', 28),
    ('Salman', 'Khan', 27),
    ('Deo', 'Anand', 24),
]

>>> sorted(heroes, key=lambda started: started[2])
[('Deo', 'Anand', 24), ('Salman', 'Khan', 27), ('Amir', 'Khan', 28)]
```

---

# map, reduce, and filter functions
----------------------

* map

  - function has two args: func and seq
  - applies the function func to all the elements of the sequence seq
  - It returns a generator object with the elements changed by func

    ```python
    >>> l = [1,2,3,4,5]
    >>> list(map(lambda x: str(chr(x+48)), l))
    ['1', '2', '3', '4', '5']

    >>> m = [ (10**4),(10**3),(10**2),(10**1),(10**0) ]  #OR
    >>> m = [(10**x) for x in range(len(l)-1, -1, -1)]
    >>> m
    [10000, 1000, 100, 10, 1]
    >>> l = list( map(lambda x,y: (x*y), l,m) )
    >>> l
    [10000, 2000, 300, 40, 5]
    >>> sum(l)
    12345
    ```
---

# map, reduce, and filter functions
----------------------

* reduce

  - function has two args: func and seq

  - continually applies the function func to the sequence seq

  - It returns a single value.

```python
>>> from functools import reduce

# sum of numbers 1+2+3+...100
>>> reduce( (lambda x, y: (x+y)), [x for x in range(1, 101)] )
5050

# max of given list
>>> reduce( (lambda a,b: a if (a > b) else b) , [47,11,42,102,13])
102
```

---

# map, reduce, and filter functions
----------------------

* filter

  - function has two args: func and seq

  - offers elegant way to filter out the elements from the list, for which function returns True
  
  - It returns generator with elements which remained after applying filter function func on seq



```python
>>> fib = [0,1,1,2,3,5,8,13,21,34,55]
>>> list(filter(lambda x: x % 2, fib))
[1, 1, 3, 5, 13, 21, 55]  
```
---

# Decorators
------------

- Allows to make _simple modifications_ to callable objects: _functions, methods, or classes_.
- Ideal when we need to extend the functionality of functions that we don't want to modify
- Essentially works as a wrapper
  - modifying the behavior of code before and after a target function execution
  - without the need to modify the function itself, augmenting the original functionality, thus decorating it.

  ```python
  def logusage(func):
    print("Calling a function:", func.__name__)
    return func

  @logusage
  def hello(msg="world"):
    print("Hello", msg.title())

  hello()

  O/P:
  Calling a function: hello
  Hello World
  ```

---
class: center, middle

# Decorators

Read more at: 

https://realpython.com/blog/python/primer-on-python-decorators/

---

# Iterators and Generators
--------------------------

iterators or iterable objects 

```python
>>> [x for x in [1,2,3,4,5]]
[1,2,3,4,5]
>>> [x for x in (1,2,3,4,5)]
[1,2,3,4,5]
>>> [x for x in {'a': 1, 'b': 2}]
['a','b']
>>> [x for x in 'abcd']
['a','b','c','d']
>>> [l for l in open('input.txt')]
['line 1 from file\n','line 2 from file\n','\n','line 3 from file\n']
```

- works on:
  * `__iter__` and
  * `__next__`

- iterator object can be used only once. 
- it raises `StopIteration` exception.

---

# Iterators and Generators
--------------------------

```python
class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    def __next__(self):
        'Returns the next value till current is lower than high'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
```
---

# Iterators and Generators
--------------------------

```python 
>>> c = Counter(5,10)
>>> for i in c:
...   print(i, end=' ')
...
5 6 7 8 9 10
```
---

# Iterators and Generators
--------------------------

Generators

- easier to create than iterator
- requires `yield` keyword

```python
>>> def my_generator():
...     print("Inside my generator")
...     yield 'a'
...     yield 'b'
...     yield 'c'
...
>>> my_generator()
<generator object my_generator at 0x7fbcfa0a6aa0>
>>> for char in my_generator():
...     print(char)
...
Inside my generator
a
b
c
```

---

# Iterators and Generators
--------------------------

```python
>>> def counter_generator(low, high):
      while low <= high:
         yield low
         low += 1

>>> for i in counter_generator(5,10):     
      print(i, end=' ')

5 6 7 8 9 10
```

---

# Context Managers
------------------

- `with` keyword

- managing the resources and freeing it

- usage:

```python
with open('output.txt', 'w') as f:
    f.write('Hi there!')
``` 

.

- Implementing the user define class as Context Manager, need to override functions:

  * `__enter__` - called when the execution enters inside the with block

  * `__exit__`  - called when the execution exits/returns from with block

---

# Monkey patching
-----------------

* Everything is an Object!!!
  - function, modules, class instances etc.
  - class attributes, function attributes
  - `dir`
  - `help`
  - `id`

* `eval` function
  - allows to arbitrary execute python code from string
  - with great power comes great responsibility!

* Dynamic type system, checking types with `type`
  - Types could be changed on the fly
  - can query on the types though
  - Strict type checking for executing operations!
---

# Multi-threading in Python
---------------------------

- single process - multiple threads

- A thread is a light weight process

- Thread shares it's process resources like :

  * address space

  * global variables

  * open files

  * etc.

- content switch for process and threads

- Scheduling is in-deterministic

- Synchronisation

---

# Multi-threading in Python
---------------------------

Has some issues:

* Deadlock

* Race conditions

* livelock


Majors:

* Locks

* Semaphores

* Using other Concurrency constructs like:

  - Conditional waits

  - Conditional notify

  - Using Events

  - Timer objects 

  - Barrier Objects

Full info at: https://docs.python.org/3/library/threading.html

---

# Multi-threading in Python
---------------------------

```python
import threading

class MyThread(threading.Thread):
    def __ init__(self, name='mythread'):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        # thread code goes here.
        pass

thrd = MyThread()

thrd.start()
```

---

# Multi-threading in Python
---------------------------


```python
# would create the thread lock object
glb_lock_object = threading.Lock()

# would acquire the global lock
glb_lock_object.acquire()

# would release the global lock acquired
glb_lock_object.release()
```

---

class: center, middle

# Assignments
