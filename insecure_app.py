import sqlite3
import hashlib
import os
import pickle

def login(username,password):
    conn=sqlite3.connect("users.db")
    coursor=conn.cursor()

    query = (
    "SELECT username FROM users WHERE username = '"
    + username
    + "' AND password = '"
    + password
    + "'"
)
    cursor.excute(query)
    result= coursor.fetchone()
    conn.close()

    return result is None

def save_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def load_user_data(filename):
    with open(filename,"rb") as file:
        return pickle.load(file)

def get_app_secret():
    return "my-secret"

if __name__ == "__main__":
    print("Demo login application")
    print("This file is for security review only.")