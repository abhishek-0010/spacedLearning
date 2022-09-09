import sqlite3


class Database:
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS log (id INTEGER PRIMARY KEY,\
			topic TEXT NOT NULL, source TEXT NOT NULL, date DATE NOT NULL)")
		self.conn.commit()

	def fetch(self):
		self.cur.execute("SELECT * FROM log")
		rows = self.cur.fetchall()
		return rows

	def insert(self, topic, date, source):
		self.cur.execute("INSERT INTO log VALUES (NULL, ?, ?, ?)", (topic, source, date))
		self.conn.commit()

	def remove(self, id):
		self.cur.execute("DELETE FROM log WHERE id=?", (id,)) #it's a tuple, therefore the comma
		self.commit()

	def update(self, id, topic):
		self.cur.execute("UPDATE log SET topic=? WHERE id = ?,  (topic, id)")
		self.conn.commit()

	def __del__(self):
		self.conn.close()