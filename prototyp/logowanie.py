from getpass import getpass
import mysql.connector
from mysql.connector import errorcode


def logowanie():
    login = input("Login: ")
    haslo = getpass("Haslo: ")
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"
        )
    except mysql.connector.Error as Err:
        print(Err)
    else:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * from customers")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    mydb.close()
    return True