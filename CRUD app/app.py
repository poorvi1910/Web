from flask import Flask, render_template,request,redirect,url_for,flash,make_response

app=Flask(__name__)
app.secret_key = 'your_secret_key_here'

import sqlite3  


@app.route('/', methods = ['GET', 'POST'])  
def login(): 
    error = None     
    if request.method == 'POST': 
        con = sqlite3.connect("books.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * from admin")
        except sqlite3.OperationalError as e:
            print(e)
            cur.execute("CREATE TABLE admin (username char(50), password char(50));")
            cur.execute("SELECT * from admin")
        record = cur.fetchall()

        for row in record:
            if request.form['username']==row[0] and request.form['password']==row[1]:
                return redirect(url_for('home'))
                break
            else: 
                error = 'Invalid username or password. Please try again !'
        
             
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
            with sqlite3.connect("books.db") as con: 
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
        con = sqlite3.connect("books.db")
        cur = con.cursor()
        cur.execute("select * from lib")
        rows = cur.fetchall()
        con.close()  
        return render_template("read.html", rows=rows)
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/accread')
def accread():
    try:
        con = sqlite3.connect("books.db")
        cur = con.cursor()
        cur.execute("select * from admin")
        rows = cur.fetchall()
        con.close()  
        return render_template("accread.html", rows=rows)
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/update', methods=['GET', 'POST'])
def update(): 
    if request.method == 'POST': 
        id = request.form['id']
        copies = request.form['copies']
        if int(copies)>0:
            with sqlite3.connect("books.db") as con: 
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
        with sqlite3.connect("books.db") as con: 
            cursor = con.cursor()
            
            cursor.execute("SELECT * FROM lib WHERE id=?", (id,))
            record = cursor.fetchone()

            if record:
                cursor.execute("DELETE from lib where id=?", (id,)) 
                con.commit() 
        return render_template("home.html") 
    else: 
        return render_template('delete.html') 

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST': 
        user = request.form['user']
        password = request.form['passwd']
        con = sqlite3.connect("books.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * from admin")
        except sqlite3.OperationalError as e:
            print(e)
            cur.execute("CREATE TABLE admin (username char(50), password char(50));")
            cur.execute("SELECT * from admin")
        record = cur.fetchall()

        for row in record:
            if row[0]==user :
                break
        else: 
            cur.execute("INSERT INTO admin VALUES (?, ?)", (user, password))
            con.commit()
    return render_template('register.html')

@app.route('/remacc', methods=['GET', 'POST'])
def remacc():
    if request.method == 'POST': 
        user = request.form['user']
        password = request.form['passwd']
        con = sqlite3.connect("books.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * from admin")
        except sqlite3.OperationalError as e:
            print(e)
            cur.execute("CREATE TABLE admin (username char(50), password char(50));")
            cur.execute("SELECT * from admin")
        record = cur.fetchall()

        for row in record:
            if (row[0]==user and row[1]==password):
                cur.execute("DELETE from admin where username=?", (user,))
                con.commit()
    return render_template('remacc.html')


app.run(debug=True) 
