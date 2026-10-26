import sqlite3
import hashlib
import os
import pickle
from argon2 import PasswordHasher, VerifyMismatchError

def login(username, password):
    conn = sqlite3.connect("users.db")

    try:
        cursor = conn.cursor()

        query = "SELECT password FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result is None:
            return False

        stored_hash = result[0]

        try:
            ph.verify(stored_hash, password)
            return True
        except VerifyMismatchError:
            return False

    finally:
        conn.close()

    return result is None

from argon2 import PasswordHasher

ph = PasswordHasher()

def save_password(password):
    return ph.hash(password)

import json

def load_user_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def get_app_secret():
    secret = os.environ.get("APP_SECRET")
    if not secret:
        raise ValueError("APP_SECRET is not configured")
    return secret

if __name__ == "__main__":
    print("Demo login application")
    print("This file is for security review only.")

