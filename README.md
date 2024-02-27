## Task
To learn web dev and hence web exploitation by creating a website and fixing vulnerabilitties. </br>
I started out by learning how to make a CRUD app using flask, jinja2 and sqlite(A CRUD app is a specific type of software application that consists of four basic operations; Create, Read, Update, Delete).CRUD is the simplest form to interact with tables and documents, and it provides you with a representation of the database itself as it is.</br>

THEME : Library Management

## Things I learnt

### 1.How to create an input field: ###
The HTML code snippet ```<input type="text" id="username" name="username">``` creates a text input field where users can enter text.

```<input>```: This is an HTML element used to create various types of input fields, such as text fields, checkboxes, radio buttons, etc.

type="text": This attribute specifies the type of input field. In this case, it's a text field, which allows users to enter single-line text.

id="username": This attribute assigns an identifier to the input field. The value of this attribute can be used to uniquely identify the input field in the document or to associate it with other elements using JavaScript or CSS.

name="username": This attribute specifies the name of the input field. When the form containing this input field is submitted, the data entered by the user will be sent to the server with the specified name as the key. It is important for form handling and processing on the server-side.

### 2.Basic Flask syntax: ###
```
# an object of WSGI application 
from flask import Flask     
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(): 
    return 'HELLO'
  
if __name__=='__main__': 
   app.run()
```
 
## Errors

1) The entire path of the database must be given or it does not identify the tables. It will not ahow that database is not found, it shows table is not found and we waste a lot of time trying to get the table instead.
2) WHile inputting, the name field must be written carefully. I used a different variable in that and the js file and spent a bunch of time trying to figure out what is wrong.

## Vulnerabilities
