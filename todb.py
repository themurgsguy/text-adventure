# Basically this scipt loads the json of all rooms into
# A make shift database so optimize on space

import sys
import sqlite3
import os
import os.path

def main(database_name):
# So here I'm making a database with 1 table

	connection = sqlite3.connect(database_name)
	connection.execute("CREATE TABLE IF NOT EXISTS rooms(id INTEGER PRIMARY KEY, json TEXT NOT NULL)")
	connection.commit()

	for filename in os.listdir():
		base, extension = os.path.splitext(filename)

		if extension == '.json':
			with open(filename, 'r') as f:
				json = f.read()

				print("Inserting room {0}".format(int(base)))

