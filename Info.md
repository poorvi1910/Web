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
First, create a class for the object you want to serialize and deserialize and it should have data members that hold the object’s state.
Now, implement the method in the class to serialize the object and write its data to a file named data.bin.
In this method, we will be using the ofstream::write() method to write the data in the binary form.
Implement the static method to deserialize the object from the file and reconstruct it using the ifstream::read() method.
In the main method, serialize the data again deserialize it, and then print it.
```
```
// C++ Program to illustrate how we can serialize and
// deserialize an object
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

class Serializable {
private:
    string name;
    int age;

public:
    Serializable(){};
    // Constructor to initialize the data members
    Serializable(const string& name, int age)
        : name(name)
        , age(age)
    {
    }

    // Getter methods for the class
    string getName() const { return name; }
    int getAge() const { return age; }

    //  Function for Serialization
    void serialize(const string& filename)
    {
        ofstream file(filename, ios::binary);
        if (!file.is_open()) {
            cerr
                << "Error: Failed to open file for writing."
                << endl;
            return;
        }
        file.write(reinterpret_cast<const char*>(this),
                   sizeof(*this));
        file.close();
        cout << "Object serialized successfully." << endl;
    }

    //  Function for Deserialization
    static Serializable deserialize(const string& filename)
    {
        Serializable obj("", 0);
        ifstream file(filename, ios::binary);
        if (!file.is_open()) {
            cerr
                << "Error: Failed to open file for reading."
                << endl;
            return obj;
        }
        file.read(reinterpret_cast<char*>(&obj),
                  sizeof(obj));
        file.close();
        cout << "Object deserialized successfully." << endl;
        return obj;
    }
};

int main()
{
    // Create and serialize an object
    Serializable original("Alice", 25);
    original.serialize("data.bin");

    // Deserialize the object
    Serializable restored
        = Serializable::deserialize("data.bin");

    // Test the  deserialized object
    cout << "Deserialized Object:\n";
    cout << "Name: " << restored.getName() << endl;
    cout << "Age: " << restored.getAge() << endl;

    return 0;
}

```

* Python
Uses pickle module
```
import pickle

obj = [1,2,3]

# pickling
with open('data.pkl', 'wb') as file:
    pickle.dump(obj, file)

# unpickling
with open('data.pkl', 'rb') as file:
    new_obj = pickle.load(file)

```

* Java
To make a Java object serializable we implement the java.io.Serializable interface. The ObjectOutputStream class contains writeObject() method for serializing an Object. <br>
The ObjectInputStream class contains readObject() method for deserializing an object. 
```
// Java code for serialization and deserialization 
// of a Java object
import java.io.*;

class Demo implements java.io.Serializable
{
	public int a;
	public String b;

	// Default constructor
	public Demo(int a, String b)
	{
		this.a = a;
		this.b = b;
	}

}

class Test
{
	public static void main(String[] args)
	{ 
		Demo object = new Demo(1, "geeksforgeeks");
		String filename = "file.ser";
		
		// Serialization 
		try
		{ 
			//Saving of object in a file
			FileOutputStream file = new FileOutputStream(filename);
			ObjectOutputStream out = new ObjectOutputStream(file);
			
			// Method for serialization of object
			out.writeObject(object);
			
			out.close();
			file.close();
			
			System.out.println("Object has been serialized");

		}
		
		catch(IOException ex)
		{
			System.out.println("IOException is caught");
		}


		Demo object1 = null;

		// Deserialization
		try
		{ 
			// Reading the object from a file
			FileInputStream file = new FileInputStream(filename);
			ObjectInputStream in = new ObjectInputStream(file);
			
			// Method for deserialization of object
			object1 = (Demo)in.readObject();
			
			in.close();
			file.close();
			
			System.out.println("Object has been deserialized ");
			System.out.println("a = " + object1.a);
			System.out.println("b = " + object1.b);
		}
		
		catch(IOException ex)
		{
			System.out.println("IOException is caught");
		}
		
		catch(ClassNotFoundException ex)
		{
			System.out.println("ClassNotFoundException is caught");
		}

	}
}

```

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

     
