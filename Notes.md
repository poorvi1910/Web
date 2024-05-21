- Python Magic methods are the methods starting and ending with double underscores ‘__’. They are defined by built-in classes in Python and commonly used for operator overloading. 
They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.
- Name Mangling : interpreter of the Python alters the variable name in a way that it is challenging to clash when the class is inherited.
-  Double Pre Underscores are used for the name mangling.Double Pre Underscores tells the Python interpreter to rewrite the attribute name of subclasses to avoid naming conflicts.

1) __dir__ : list out all the attributes of the parameter passed, is really useful when handling a lot of classes and functions, separately.  
```
class Supermarket:
    def __dir__(self):
        return['customer_name', 'product','quantity', 'price', 'date']
my_cart = Supermarket()
print(dir(my_cart))
Output
['customer_name', 'date', 'price', 'product', 'quantity']
```
2) __qualname__ : If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name.__qualname__gives more complete information than __name__ and therefore can be more helpful in debugging
```
>>> def f(): pass
... class A:
...    def f(self): pass
...    class A:
...        def f(self): pass
>>> f.__qualname__
'f'
>>> A.f.__qualname__
'A.f'
>>> A.A.f
```

3) __mro__ : The method resolution order (mro) attribute __mro__ is computed from the bases of the class. It provides support for multiple inheritance.
```
>>> class A(object):
...     pass
>>> A.__mro__
(<class 'A'>, <type 'object'>)
```

4)  __init: method to initiate object
```
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
print(obj.value)

 Output: 10
```
5) __globals__ : A reference to the global namespace.
```
def func():
    print(__globals__)

func()

Output: {..., '__globals__': <module '__main__' from '...'>, ...}
```
6) __class__ : 
```
class MyClass:
    pass

obj = MyClass()
print(obj.__class__)

Output: <class '__main__.MyClass'>
```

7) __import__ : a built-in method that is used to import modules and functions
```
np = __import__('numpy', globals(), locals(), [], 0)
a = np.array([1, 2, 3])
print(type(a))

Output:
<class 'numpy.ndarray'>
```

8) __builtins__ : The value of __builtins__ is normally either this module or the value of this module's __dict__ attribute.
```
print(__builtins__)

Output: <module 'builtins' (built-in)>
```

9)  __str__ : returns a human-readable, or informal, string representation of an object
```
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Value {self.value}"

obj = MyClass(10)
print(obj)

Output: Value 10

```

10)  __getitem__ : when used in a class, allows its instances to use the [] (indexer) operators.this method is used to access the items from the list, dictionary, and array.
```
class MyClass:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

obj = MyClass([1, 2, 3])
print(obj[1])  

Output: 2

```
