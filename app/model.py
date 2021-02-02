import sqlite3
from app import app

# logic for using data from two different tables and updating the solution after analysis to agent_name column.

@app.route("/assignment_tasktoagent")
def assignment_tasktoagent():
    conn = sqlite3.connect('identifier.sqlite.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM user ORDER BY priority ASC ")
    data_user = dict(result=[dict(r) for r in cur.fetchall()])

    conn1 = sqlite3.connect('identifier.sqlite.db')
    conn1.row_factory = sqlite3.Row
    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM agent ")
    data_agent = dict(result=[dict(r) for r in cur1.fetchall()])

# Loop over the data from 2 tables
    for i in data_user['result']:
        for i1 in data_agent['result']:
            if i['language_restrictions'] in i1['language_skills']:
                if i['platform'] in i1['assigned_task']:

                    cur1.execute("UPDATE user SET agent_name = (SELECT name from agent WHERE agent.id = user.id) ")

    conn1.commit()
    return str(data_user['result'])
