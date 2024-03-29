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

### 3.Templating with Jinja2 ###

### 4.Connecting SQLite with Flask: ###
```
import sqlite3
.
.
with sqlite3.connect("/home/lunaniverse/books.db") as con: 
    cursor = con.cursor() 
    cursor.execute("INSERT INTO lib (id, name, author, copies) VALUES (?,?,?,?)", (id, name, author, copies)) 
    con.commit() 
.
.
```

### 5.How to hide the login details
```
@app.route('/', methods = ['GET', 'POST'])  
def login(): 
    error = None     
    if request.method == 'POST': 
        con = sqlite3.connect("/home/lunaniverse/books.db")
        cur = con.cursor()
        cur.execute("SELECT * from admin")
        record=cur.fetchall()

        for row in record:
            if request.form['username']==row[0] and request.form['password']==row[1]:
                return redirect(url_for('home'))
                break
            else: 
                error = 'Invalid username or password. Please try again !'
        
             
    return render_template('login.html', error = error)
```


## Errors

1) The databae file must be created in the project folder itself or the code will not be able to  find it.
2) WHile inputting, the name field must be written carefully. I used a different variable in that and the js file and spent a bunch of time trying to figure out what is wrong.

## Vulnerabilities
1) Initially i had just placed the username and password in the js file but that would be visible to anyone who would inspect the page. Hence i placed inside a database instead.
