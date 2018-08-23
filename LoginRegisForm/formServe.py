from flask import Flask, render_template, request, url_for
import mysql.connector as mysqlcon
import __future__

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route('/signUpReq', methods=['POST', 'GET'])

# def databaseEntry(username, email, password):
#     try:
#         with sql.connect('database.db') as con:
#             cur = con.cursor()
#             cur.execute("INSERT INTO logInfo(username, email, password) VALUES (?,?,?)", (username, email, password))
#             con.commit()
#             msg = "Record submitted succesfully"
#     except:
#         con.rollback()
#         msg = "error in inserting data"
#     finally:
#         return render_template('hello.html', username = username)
#         con.close()



def gettingData():
    msg=False
    if request.method == 'POST':

        username = request.form['Username']
        email = request.form['email']
        password = request.form['password']
      
        con = mysqlcon.connect(
            host="localhost",
            user="root",
            password="9329025673*",
            db="flaskProj"
        )
        cur = con.cursor()

        cur.execute("INSERT INTO logInfo(username, email, password) VALUES (%s,%s,%s)", (username, email, password))        
        con.commit()
        msg = True
        con.close()
        
                       
        if (msg):
            return render_template('hello.html', username=username, mesg=msg)
        else:
            return "Connectivity Issue"

@app.route("/login")
def login():
   return render_template("login.html")

@app.route("/loginCheck", methods=['POST', 'GET'])

def auth():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        con = mysqlcon.connect(
            host="localhost",
            user="root",
            password="9329025673*",
            db="flaskProj"
        )
        cur = con.cursor()

        query = ("SELECT password FROM logInfo WHERE email = %s")

        mailFetch = (str(email),)

        cur.execute(query, mailFetch)

        authPass = cur.fetchall()
        

        con.commit()
        con.close()

        for pas in authPass:
            print(str(pas[0]))
            print(password)
            if password == str(pas[0]):
                return 'authenticated user'
            else:
                return 'Please signup for our service'
            
             


if __name__ == '__main__':
    app.run(debug=True)
