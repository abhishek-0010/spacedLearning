import sqlite3
import datetime


class Database:
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS log (id INTEGER PRIMARY KEY,\
			topic text NOT NULL, date DATE NOT NULL, revision INTEGER)")
		self.conn.commit()

	def fetch(self):
		self.cur.execute("SELECT * FROM log")
		rows = self.cur.fetchall()
		return rows

	def insert(self, topic, date):
		self.cur.execute("INSERT INTO log VALUES (NULL, ?, ?, ?)", (topic, date, 0))
		self.conn.commit()

	def remove(self, id):
		self.cur.execute("DELETE FROM log WHERE id=?", (id,)) #it's a tuple, therefore the comma
		self.commit()

	def update(self, id, topic):
		self.cur.execute("UPDATE log SET topic=? WHERE id = ?,  (topic, id)")
		self.conn.commit()

	def __del__(self):
		self.conn.close()



current_date = datetime.date.today()

#db = Database("spaced_interval.db")
#db.insert("tkinter", current_date) 
#db.insert("flask", current_date) 
#db.insert("arrays", current_date) 
#db.insert("trees", current_date) 
#db.insert("linked list", current_date) 