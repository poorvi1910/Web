from flask import Flask, render_template,request,redirect,url_for,flash,make_response

app=Flask(__name__)
app.secret_key = 'your_secret_key_here'

import sqlite3  


@app.route('/', methods = ['GET', 'POST'])  
def login():      
   error = None
     
   if request.method == 'POST': 
      if request.form['username'] != 'admin' or request.form['password'] != 'passwd': 
         error = 'Invalid username or password. Please try again !'
      else: 
         return redirect(url_for('home')) 
   return render_template('login.html', error = error) 

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/create', methods=['GET', 'POST'])
def create(): 
    if request.method == 'POST': 
        id = request.form['id']  
        name = request.form['name']
        author = request.form['author'] 
        copies = request.form['copies'] 

        if int(copies)>0:
            with sqlite3.connect("/home/lunaniverse/books.db") as con: 
                cursor = con.cursor() 
                cursor.execute("INSERT INTO lib (id, name, author, copies) VALUES (?,?,?,?)", (id, name, author, copies)) 
                con.commit() 
            return render_template("home.html")
        else:
            return render_template("home.html") 
    else: 
        return render_template('create.html')

@app.route('/read')
def read():
    try:
        con = sqlite3.connect("/home/lunaniverse/books.db")
        cur = con.cursor()
        cur.execute("select * from lib")
        rows = cur.fetchall()
        con.close()  
        return render_template("read.html", rows=rows)
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/update', methods=['GET', 'POST'])
def update(): 
    if request.method == 'POST': 
        id = request.form['id']
        copies = request.form['copies']
        if int(copies)>0:
            with sqlite3.connect("/home/lunaniverse/books.db") as con: 
                cursor = con.cursor() 
                cursor.execute("UPDATE lib set copies=? where id=?", (copies,id)) 
                con.commit() 
            return render_template("home.html")
        else:
            return render_template("home.html")
    else: 
        return render_template('update.html') 

@app.route('/delete', methods=['GET', 'POST'])
def delete(): 
    if request.method == 'POST': 
        id = request.form['id']
        with sqlite3.connect("/home/lunaniverse/books.db") as con: 
            cursor = con.cursor()
            
            cursor.execute("SELECT * FROM lib WHERE id=?", (id,))
            record = cursor.fetchone()

            if record:
                cursor.execute("DELETE from lib where id=?", (id,)) 
                con.commit() 
        return render_template("home.html") 
    else: 
        return render_template('delete.html') 


app.run(debug=True) 
