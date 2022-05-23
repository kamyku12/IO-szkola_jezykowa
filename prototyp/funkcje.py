import getpass
import mysql.connector

def logowanie():
    login = input("Login: ")
    haslo = getpass.getpass(prompt='Password: ')

