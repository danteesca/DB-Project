import mysql.connector
from flask import Flask
from flask import render_template 
from flask import request, redirect
import random
import math


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
      # print(results)
       for row in results:
          fname = row[0]
          lname = row[2]
          sex = row[6]
          income = row[7]
          # Now print fetched result
          #print ("fname=%s,lname=%s,sex=%s,income=%d" % \
          #       (fname, lname, sex, income ))
    except:
      print ("Error: unable to fecth data")
    return results
      
def Insert(sql):
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       mydb.commit()
    except:
       # Rollback in case there is any error
       mydb.rollback()
       print ("SOMETHING BAD HAPPENED")
       
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
        donorID = request.form["donorID"]
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
        receiverID = request.form["receiverID"]
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


@app.route("/AddExistingFood", methods=["GET", "POST"])             #Not working properly
def addExistingFood():
    if request.method == "POST":
        foodID = request.form["foodID"]
        foodName = request.form["foodName"]
        foodType = request.form["foodType"]
        expDate = request.form["expDate"]
        donorID = request.form["donorID"]
        quantity = request.form["quantity"]
        print (foodID,foodName,foodType,expDate, donorID, quantity)
        sql = "INSERT INTO FOOD(foodID, foodName, foodType, expDate) \
            VALUES ('%s', '%s','%s', '%s')" % \
            (foodID, foodName, foodType, expDate)
        print (sql)
        Insert (sql)
        sql2 = "INSERT INTO DONATES(donorID, foodID, quantity) \
            VALUES ('%s' , '%s' , '%d')" % \
            (donorID, foodID, int(quantity))
        print(sql2)
        Insert(sql2)

        return redirect(request.url)
    return render_template("AddExistingFood.html")


@app.route("/AddNewFood", methods=["GET", "POST"])                  #Used
def addNewFood():
    if request.method == "POST":
        foodID = ""
        for i in range(5):
            index = math.floor(random.random()*5)
            foodID += str(index)
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
        sql2 = "INSERT INTO DONATES(donorID, foodID, quantity) \
            VALUES ('%s' , '%s' , '%d')" % \
            (donorID, foodID, int(quantity))
        print(sql2)
        Insert(sql2)

        return redirect(request.url)
    return render_template("AddNewFood.html")



@app.route("/AddFood")                                             #Used
def addFood():
    return render_template('Food_Choice.html')  

@app.route("/AddReceives", methods=["GET","POST"])
def addReceives():
    if request.method == "POST":
        receiverID = request.form["receiverID"]
        foodID = request.form["foodID"]
        quantity = request.form["quantity"]
        print(receiverID,foodID,quantity)
        sql = "INSERT INTO RECEIVES(donorID, foodID, quantity) \
            VALUES ('%s' , '%s' , '%d')" % \
            (receiverID, foodID, int(quantity))
        print(sql)
        Insert(sql)

        return redirect(request.url)
    return render_template("AddReceives.html")
    







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

#You can add Update as well 
 


