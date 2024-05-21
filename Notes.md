- Python Magic methods are the methods starting and ending with double underscores ‘__’. They are defined by built-in classes in Python and commonly used for operator overloading. 
They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.
- Name Mangling : interpreter of the Python alters the variable name in a way that it is challenging to clash when the class is inherited.
-  Double Pre Underscores are used for the name mangling.Double Pre Underscores tells the Python interpreter to rewrite the attribute name of subclasses to avoid naming conflicts.

1) __dir__ : It can be used to obtain the current code working directory.
2) __qualname__ : If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name.__qualname__gives more complete information than __name__ and therefore can be more helpful in debugging
3)  __getitem__ : when used in a class, allows its instances to use the [] (indexer) operators.this method is used to access the items from the list, dictionary, and array.
4)
5)
6)
7)
8)
9)
10)

-  __init: method to initiate object
-  __del__: destructor method. It is called after an object’s garbage collection occurs, which happens after all references to the item have been destroyed.
-  __repr__ : defines how an object is presented as a string.
-  __str__ : returns a human-readable, or informal, string representation of an object
-  __call__: The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function
-  __len__ :When the object doesn’t have a predefined __len__ method, then while executing the len function it gives a TypeError, but it can be corrected by defining a __len__ method by our own
-  __setitem__ :  used to assign the values to the item. When we assign or set a value to an item in a list, array, or dictionary, this method is called internally.
-  __delitem__ :  deletes the items in the list, dictionary, or array
-  __iter__
-  __next__
-  __getattr__ : his method will allow you to “catch” references to attributes that don’t exist in your object.
-  __setattr__
-  __delattr__
-  __enter__
-  __exit__
-  __bool__
-  __format__
-  __doc__
-  __class__
-  __module__
-  __bases__
-  __import__
-  __annotations__ : It outputs the dictionary having a special key ‘return’ and other keys having name of the annotated arguments. The following code will print the annotations.
-  __dict__
-  __weakref__
-  __reduce__
-  __reduce_ex__
-  __copy__ :  Implements the shallow copy operation.
-  __deepcopy__ :  Implements the deep copy operation.
-  __slots__
-  __mro__
-  __globals__
-  __builtins__
