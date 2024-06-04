* Serialisation
  * Serializing is about moving structured data over a storage/transmission medium in a way that the structure can be maintained. 
  * Serialization is the process of converting an object or data structure into a format that can be easily stored or transmitted and reconstructed later. 
  * The main goal of serialization is to convert complex data structures or objects into a linear stream of bytes so that they can be saved to a file, sent over a network, or stored in a database. 
  * When an object is serialized, all of its data fields are converted into a format that can be reconstructed later to recreate the original object.

* Encoding
  * Encoding is more broad, like about how said data is converted to different forms, etc
  * Encoding, on the other hand, is the process of converting data from one form to another.
  * Encoding is typically used to ensure that data can be correctly interpreted and transmitted across different systems or devices.
  * Encoding can involve transforming data into a specific format to meet certain requirements such as data compression, error detection/correction, or ensuring that data is represented in a compatible form for transmission

  
* With regard to a web service, you will probably be considering serializing/deserializing certain data for making/receiving requests/responses - effectively transporting "messages". 
Encoding is at a lower level, like how your messaging/web service type/serialization mechanism works under the hood.

* C++
```
To write object's data members in a file :
// Here file_obj is an object of ofstream
file_obj.write((char *) & class_obj, sizeof(class_obj));

To read file's data members into an object :
// Here file_obj is an object of ifstream
file_obj.read((char *) & class_obj, sizeof(class_obj));
```

* Python



* Java


* Pickling

  * Python pickle module is used for serializing and de-serializing a Python object structure.
    Any object in Python can be pickled so that it can be saved on disk. What Pickle does is it “serializes” the object first before writing it to a file.
    Pickling is a way to convert a Python object (list, dictionary, etc.) into a character stream.
    The idea is that this character stream contains all the information necessary to reconstruct the object in another Python script.
    It provides a facility to convert any Python object to a byte stream.
    This Byte stream contains all essential information about the object so that it can be reconstructed, or “unpickled” and get back into its original form in any Python.
    
  * To successfully unpickle the object, the pickled byte stream contains instructions to the unpickler to reconstruct the original object structure along with instruction operands, which help in     populating the object structure
      
  * Escape characters:
    * \xhh	Gives the hexadecimal representation
 
 * The structure of a pickle file includes:
     * Header: Indicates the pickle protocol version.
     * Opcodes and Arguments: Define the serialized object structure.
     * Stop Opcode: Marks the end of the pickle data.
  ![image](https://github.com/poorvi1910/Web/assets/146640913/4e00b717-8dfc-4953-904b-90f94c41b153)

  *  ```
     0x80 to 0x00 -> non-printable
     0x5D -> ]
     0x94 -> non-printable
     0x28 -> (
     0x4B -> K
     0x01 -> non-printable
     0x4B -> K
     0x02 -> non-printable
     0x7D -> }
     0x94 -> non-printable
     0x8C -> non-printable
     0x03 -> non-printable
     0x63 -> c
     0x61 -> a
     0x74 -> t
     0x94 -> non-printable
     0x8C -> non-printable
     0x05 -> non-printable
     0x6D -> m
     0x6F -> o
     0x75 -> u
     0x73 -> s
     0x65 -> e
     0x94 -> non-printable
     0x73 -> s
     0x65 -> e
     0x2E -> .
     ```
     ```
     Header (0x80 0x04): The pickle protocol version is 4.
     Frame (0x95...): Indicates a frame with a specified size.
     Empty List (0x5D): An empty list is pushed onto the stack.
     Memoize (0x94): The empty list is memoized for later reference.
     Mark (0x28): Marks the start of a tuple.
     Integers (0x4B 0x01, 0x4B 0x02): Integers 1 and 2 are pushed onto the stack.
     Empty Dict (0x7D): An empty dictionary is pushed onto the stack.
     Memoize (0x94): The empty dictionary is memoized.
     Short Unicode Strings (0x8C...): "cat" and "mouse" strings are pushed onto the stack and memoized.
     Set Item (0x73): Sets "cat" as a key and "mouse" as a value in the dictionary.
     Appends (0x65): Appends items (possibly a list or dictionary) to another structure.
     Stop (0x2E): Ends the pickling process.
     ```
  * Net result of the operation: 
   ![image](https://github.com/poorvi1910/Web/assets/146640913/420daa06-d7e0-4253-9385-8d3f8405c240)

     
