from types import NoneType
import mysql.connector
from flask import Flask
from flask import render_template 
from flask import request, redirect
import random
import math
import functools


###Change you password 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database='Project',
  password="escamilla123"
)

cursor = mydb.cursor();

def Select(sql):
    try:
       # Execute the SQL command
       cursor.execute(sql)
       
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
    except:
      print ("Error: unable to fecth data")
    return results
      
def Insert(sql):
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       mydb.commit()
    except Exception as e:
       # Rollback in case there is any error
       mydb.rollback()
       print ("SOMETHING BAD HAPPENED")
       print(e)
       
def update(sql):
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       mydb.commit()
    except:
       # Rollback in case there is any error
       mydb.rollback()
       print ("somethingbad happened")
       
def Delete(sql):
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       mydb.commit()
    except:
       # Rollback in case there is any error
       mydb.rollback()
       print ("somethingbad happened")
       
#Web interface starts here

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("home.html")


@app.route("/Manager")
def Manager():
    #Manger page with what he can do 

    return render_template('Manager.html') 
@app.route("/Display_Donors")                                       #Used 
def Donors():
    #Special select statement for the manager 
    sql = "SELECT * FROM DONORS;"
    users= Select(sql)
#     
    return render_template('Display_Donors.html', users=users)  

@app.route("/Display_Receivers")                                    #Used
def Receivers():
    #Special select statement for the manager 
    sql = "SELECT * FROM RECEIVERS;"
    users= Select(sql)
#     
    return render_template('Display_Receivers.html', users=users) 

@app.route("/Display_Foods")                                        #Used
def Foods():
    #Special select statement for the manager 
    sql = "SELECT * FROM FOOD;"
    users= Select(sql)
#     
    return render_template('Display_Food.html', users=users) 
 
@app.route("/AddDonor", methods=["GET", "POST"])                    #Used
def addDonor():
    #Adding a donor
    if request.method == "POST":
        donorID = ""
        for i in range(5):
            index = math.floor(random.random()*5)
            donorID += str(index)
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        address = request.form["address"]
        phone = request.form["phone"]
        print (donorID,firstName,lastName,address,phone)
        sql = "INSERT INTO DONORS(donorID, firstName, lastName, address, phone) \
            VALUES ('%s', '%s','%s', '%s', '%s')" % \
            (donorID, firstName, lastName, address, phone)
        print (sql)
        Insert (sql)

        return redirect(request.url)
    return render_template("AddDonor.html")

@app.route("/AddReceiver", methods=["GET", "POST"])                 #Used
def addReceiver():
    #Adding a donor
    if request.method == "POST":
        receiverID = ""
        for i in range(5):
            index = math.floor(random.random()*5)
            receiverID += str(index)
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        address = request.form["address"]
        phone = request.form["phone"]
        print (receiverID,firstName,lastName,address,phone)
        sql = "INSERT INTO RECEIVERS(receiverID, firstName, lastName, address, phone) \
            VALUES ('%s', '%s','%s', '%s', '%s')" % \
            (receiverID, firstName, lastName, address, phone)
        print (sql)
        Insert (sql)

        return redirect(request.url)
    return render_template("AddReceiver.html")


@app.route("/AddExistingFood", methods=["GET", "POST"])             #Used
def addExistingFood():
    if request.method == "POST":
        dtID = ""
        for i in range(5):
            index = math.floor(random.random()*5)
            dtID += str(index)
        foodID = request.form["foodID"]
        donorID = request.form["donorID"]
        quantity = request.form["quantity"]
        print (foodID, donorID, quantity)
        sql = "INSERT INTO DONATES(dtID, donorID, foodID, quantity) \
            VALUES ('%s', '%s', '%s', '%d')" % \
            (dtID, donorID, foodID, int(quantity))
        print (sql)
        Insert(sql)
        


        return redirect(request.url)
    return render_template("AddExistingFood.html")

def insertDonates(donorID, foodID, quantity):
    sql2 = "INSERT INTO DONATES(donorID, foodID, quantity) \
        VALUES ('%s', '%s', '%d')" % \
        (donorID, foodID, int(quantity))
    print(sql2)
    Insert(sql2)
    return


@app.route("/AddNewFood", methods=["GET", "POST"])                  #Used
def addNewFood():
    if request.method == "POST":
        dtID = ""
        for i in range(5):
            index1 = math.floor(random.random()*5)
            dtID += str(index1)
        foodID = ""
        for i in range(5):
            index2 = math.floor(random.random()*5)
            foodID += str(index2)
        foodName = request.form["foodName"]
        foodType = request.form["foodType"]
        expDate = request.form["expDate"]
        donorID = request.form["donorID"]
        quantity = request.form["quantity"]
        print (foodID,foodName,foodType,expDate, donorID, quantity)
        sql = "INSERT INTO FOOD(foodID, foodName, foodType, expDate) \
            VALUES ('%s', '%s','%s', '%s')" % \
            (str(foodID), foodName, foodType, expDate)
        print (sql)
        Insert (sql)
        sql2 = "INSERT INTO DONATES(dtID, donorID, foodID, quantity) \
            VALUES ('%s', '%s' , '%s' , '%d')" % \
            (dtID, donorID, foodID, int(quantity))
        print(sql2)
        Insert(sql2)

        return redirect(request.url)
    return render_template("AddNewFood.html")



@app.route("/AddFood")                                             #Used
def addFood():
    return render_template('Food_Choice.html')  

@app.route("/AddReceives", methods=["GET","POST"])                  #Used
def addReceives():
    if request.method == "POST":
        rtID = ""
        for i in range(5):
            index1 = math.floor(random.random()*5)
            rtID += str(index1)
        receiverID = request.form["receiverID"]
        foodID = request.form["foodID"]
        quantity = request.form["quantity"]
        print(rtID, receiverID,foodID,quantity)
        sql = "INSERT INTO RECEIVES(rtID, receiverID, foodID, quantity) \
            VALUES ('%s', '%s' , '%s' , '%d')" % \
            (rtID, receiverID, foodID, int(quantity))
        print(sql)
        Insert(sql)

        return redirect(request.url)
    return render_template("AddReceives.html")


@app.route("/TotalQuantity", methods = ["GET", "POST"])
def totalQ():
    myVar =""
    total = 0
    if request.method == "POST":
        foodID = request.form["foodID"]
        print(foodID)
        sql1 = "SELECT SUM(quantity) FROM DONATES d WHERE d.foodID = '%s'" % \
            (foodID)
        print(sql1)
        results = Select(sql1)
        q1 = ''
        for row in results:
            q1 = row[0]
        print(q1)
        sql2 = "SELECT SUM(quantity) FROM RECEIVES r WHERE r.foodID = '%s'" % \
            (foodID)
        print(sql2)
        results = Select(sql2)
        q2 = ''
        for row in results:
            q2 = row[0]
        print(q2)
        if type(q2) == NoneType:
            total = int(q1)
        else:
            total = int(q1) - int(q2)
        print(total)

    myVar = str(total)
    return render_template("totalQuantity.html", myVar = myVar)
    


@app.route("/Search_Donors", methods = ["GET", "POST"])
def searchDonors():
    users=()
    if request.method == "POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        print(firstName, lastName)
        sql = "SELECT * FROM DONORS d WHERE d.firstName = '%s' AND d.lastName = '%s'" % \
            (firstName, lastName)
        print(sql)
        results = Select(sql)
        users = results
    
    
    return render_template("Search_Donors.html", users = users)

@app.route("/Search_Receivers", methods = ["GET", "POST"])
def searchReceivers():
    users=()
    if request.method == "POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        print(firstName, lastName)
        sql = "SELECT * FROM RECEIVERS r WHERE r.firstName = '%s' AND r.lastName = '%s'" % \
            (firstName, lastName)
        print(sql)
        results = Select(sql)
        users = results
    
    
    return render_template("Search_Receivers.html", users = users)

@app.route("/Search_Food", methods = ["GET", "POST"])
def searchFood():
    users=()
    if request.method == "POST":
        foodName = request.form["foodName"]
        foodType = request.form["foodType"]
        print(foodName, foodType)
        sql = "SELECT * FROM FOOD f WHERE f.foodName = '%s' AND f.foodType = '%s'" % \
            (foodName, foodType)
        print(sql)
        results = Select(sql)
        users = results
    
    
    return render_template("Search_Food.html", users = users)











@app.route("/DeleteEmployee", methods=["GET", "POST"])
def DeleteEmployee():
    #Deleting an employee
    if request.method == "POST":
        fname = request.form["fname"]
        ssn = request.form["ssn"]
        print (fname,ssn)
        sql = "Delete from EMPLOYEE where Fname= '%s' and ssn='%d' " % \
            (str(fname), int(ssn))
        print (sql)
        Delete (sql)

        return redirect(request.url)
    return render_template("DeleteEmployee.html")


 


