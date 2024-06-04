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
  * Any object in Python can be pickled so that it can be saved on disk. What Pickle does is it “serializes” the object first before writing it to a file.
  * Pickling is a way to convert a Python object (list, dictionary, etc.) into a character stream.
  * The idea is that this character stream contains all the information necessary to reconstruct the object in another Python script.
  * It provides a facility to convert any Python object to a byte stream.
  * This Byte stream contains all essential information about the object so that it can be reconstructed, or “unpickled” and get back into its original form in any Python.
  
