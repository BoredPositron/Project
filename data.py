import sqlite3
import pyperclip as pc
import enc
import json

def get_username(client):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute(f"SELECT username FROM userdata WHERE client = '{client}'")
    username = cur.fetchone()
    conn.commit()
    conn.close()
    return username[0]


def get_password(client):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute(f"SELECT password FROM userdata WHERE client = '{client}'")
    password = cur.fetchone()
    conn.commit()
    conn.close()
    pc.copy(password[0])


def add_data(username, password, client):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO userdata VALUES ('{username}', '{password}', '{client}')")
    conn.commit()
    conn.close()


def get_set_user():
    enc.decrypt_settings()
    file = open("settings.json")
    data = json.load(file)
    username = data["settingsusername"]
    file.close()
    enc.encrypt_settings()
    return username


def get_set_pass():
    enc.decrypt_settings()
    file = open("settings.json")
    data = json.load(file)
    password = data["settingspassword"]
    file.close()
    enc.encrypt_settings()
    return password


def save_theme():
    thm = {}
    if get_theme() == "Dark":
        thme = "Light"
    else:
        thme = "Dark"
    thm["theme"] = thme
    with open("theme.json", "w") as write_file:
        json.dump(thm, write_file)


def get_theme():
    file = open("theme.json")
    data = json.load(file)
    theme = data["theme"]
    file.close()
    return theme
