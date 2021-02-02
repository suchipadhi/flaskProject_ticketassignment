import sqlite3

conn = sqlite3.connect('identifier.sqlite.db')
c = conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS agent (name TEXT, language_skills TEXT, assigned_task TEXT)")
c.execute("INSERT INTO agent VALUES('A',['English', 'German'],['facebook_chat', 'email', 'facebook_chat'])")
c.execute("INSERT INTO agent VALUES('B',['English', 'French'],['website_chat','facebook_chat', 'call'])")
c.execute("INSERT INTO agent VALUES('C',['English', 'French'],['website_chat','facebook_chat'])")

conn.commit()
c.close()
conn.close()

