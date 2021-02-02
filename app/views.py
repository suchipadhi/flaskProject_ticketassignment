import flask
import sqlite3
from app import app

# gives a message to the user after successful creation of user table in db.
@app.route("/create_task")
def index():
    conn = sqlite3.connect('identifier.sqlite.db')
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS user (id INT, language_restrictions TEXT, platform TEXT)")
    c.execute("INSERT INTO user VALUES(3, 'French', 'call')")
    conn.commit()
    return "Task created from a user request."

# queries all data from user table
@app.route("/displaycreated_task")
def displaycreated_task():

    conn = sqlite3.connect('identifier.sqlite.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM user ")

    data = dict(result=[dict(r) for r in cur.fetchall()])

    return str(data['result'])
