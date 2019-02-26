# PyCurry — Currying functions in Python

You want to use PyCurry if you
 - think that currying is really cool
 - want to force a function to only take arguments of certain types

To curry a function in Python using this module, you can decorate it with the `curry`-decorator. `curry` takes as arguments the types that the curried function's arguments should have. If you later call the function with different types, it will raise a `TypeError`. If you don't care about the types, you can use `pycurry.Any` as a placeholder for an arbitrary type.

Check this out:

```python
from pycurry import curry

@curry(int, int, int)
def f(x,y,z):
  return x+y+z

f(1,2,3)    # => 6
f(1,2)(3)   # => also 6
f(1)(2,3)   # => also 6
f(1)(2)(3)  # => also 6

g = f(3)
g(2,1)  # => 6
h = g(2)
h(1)  # => 6

g("haha")  # => TypeError: in f: expected <class 'int'>, got <class 'str'>

```

Another example:
```python
from pycurry import Any

@curry(int,Any)
def mult(x,y):
  return x*y

times3 = mult(3)
times3("haha ")  # => "haha haha haha "
times3(4)  # => 12
```

## Why would I ever want to do this?
This is useful when you have a general function and you need to generate more special versions of it on the fly, for example to pass them to other functions like `map` or `filter`.

Real life scenario:

```python
@curry(int, Any, Any)
def myfunc(x, m,t):
  return t + m*x

list(map(myfunc(3,"!"), ["I'm hungry", "I need sleep", "I love functional programming"]))
# => ["I'm hungry!!!", 'I need sleep!!!', 'I love functional programming!!!']
```

---------------

This software comes with no warranty.
