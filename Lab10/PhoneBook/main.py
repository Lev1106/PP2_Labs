from connect import *

# For convenience
def insert_with_id(name, surname, cursor):
	# adding new entry
	cursor.execute("INSERT INTO users (name, surname) VALUES (%s, %s)", (name, surname))
	# extracting id
	cursor.execute("SELECT id FROM users WHERE name = %s AND surname = %s ORDER BY id DESC LIMIT 1", (name, surname))
	return cursor.fetchone()[0]

# 1
def create_tables():
	conn = connect()
	commands = [
		# '''
		# CREATE ROLE lev;
		# CREATE USER lev WITH PASSWORD '123ewq';
		# GRANT ALL PRIVILEGES ON SCHEMA public TO lev;
		# ''',
		# '''DROP TABLE IF EXISTS users;''',
		# '''DROP TABLE IF EXISTS phonebook;''',

		'''CREATE TABLE IF NOT EXISTS users (
			id SERIAL PRIMARY KEY,
			name TEXT NOT NULL,
			surname TEXT NOT NULL
		);''',
		'''CREATE TABLE IF NOT EXISTS phonebook (
			id SERIAL PRIMARY KEY,
			user_id INTEGER REFERENCES users(id),
			phone VARCHAR(20) NOT NULL
		);''',
		'''
		GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO lev;
		''',
	]
	with conn.cursor() as cur:
		for command in commands:
			cur.execute(command)

		# print(cur.fetchall())
		conn.commit()
		cur.close()
	conn.close()
	print("Successfully created tables users and phonebook!")


# 2.1
def upload_from_csv(path):
	import csv
	conn = connect()
	cursor = conn.cursor()
	with open(path, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		# reading all entries
		for row in spamreader:
			name, surname, phone = row
			# adding every entry into DB
			user_id = insert_with_id(name, surname, cursor)
			cursor.execute("INSERT INTO phonebook (user_id, phone) VALUES (%s, %s)", (user_id, phone))
	conn.commit()
	cursor.close()

# 2.2
def enter_name_phone(name=None, surname=None, phone=None):
	if name is None:
		name = input("Enter name: ")
	if surname is None:
		surname = input("Enter surname: ")
	if phone is None:
		phone = input("Enter phone: ")
	conn = connect()
	cursor = conn.cursor()

	user_id = insert_with_id(name, surname, cursor)
	cursor.execute("INSERT INTO phonebook (user_id, phone) VALUES (%s, %s)", (user_id, phone))

	conn.commit()
	cursor.close()


# 3
def update_data(name=None, surname=None, phone=None):
	conn = connect()
	cursor = conn.cursor()

	# First option: find by name and change their surname, phone
	cursor.execute("SELECT id FROM users WHERE name = %s", (name,))
	res = cursor.fetchone()
	if res: # right option
		user_id = res[0]
		cursor.execute("UPDATE users SET surname = %s WHERE id = %s", (surname, user_id))
		cursor.execute("UPDATE phonebook SET phone = %s WHERE user_id = %s", (phone, user_id))

	else:
		# Second option: find by surname and change their name, phone
		cursor.execute("SELECT id FROM users WHERE surname = %s", (surname,))
		res = cursor.fetchone()
		if res: # right option
			user_id = res[0]
			cursor.execute("UPDATE users SET name = %s WHERE id = %s", (name, user_id))
			cursor.execute("UPDATE phonebook SET phone = %s WHERE user_id = %s", (phone, user_id))

		else:
			# Third option: find by phone and change their name, surname
			cursor.execute("SELECT user_id FROM phonebook WHERE phone = %s", (phone,))
			res = cursor.fetchone()
			if res: # right option
				user_id = res[0]
				cursor.execute("UPDATE users SET name = %s, surname = %s WHERE id = %s", (name, surname, user_id))

	print(f"Updated with name={name}, surname={surname}, phone={phone}")
	conn.commit()
	cursor.close()
		

# 4
def query_data(name_filter=None, surname_filter=None, phone_filter=None, type="OR", output=False): # type is "OR" or "AND"
	if name_filter is None:
		name_filter = "%"
	if surname_filter is None:
		surname_filter = "%"
	if phone_filter is None:
		phone_filter = "%"

	conn = connect()
	cursor = conn.cursor()

	if type == "OR":
		cursor.execute(f"SELECT users.id, users.name, users.surname, phonebook.phone FROM users "
			f"JOIN phonebook ON users.id = phonebook.user_id "
			f"WHERE users.name ILIKE %s OR users.surname ILIKE %s OR phonebook.phone ILIKE %s"
			, (f"%{name_filter}%", f"%{surname_filter}%", f"%{phone_filter}%"))
	else:
		cursor.execute(f"SELECT users.id, users.name, users.surname, phonebook.phone FROM users "
			f"JOIN phonebook ON users.id = phonebook.user_id "
			f"WHERE users.name ILIKE %s AND users.surname ILIKE %s AND phonebook.phone ILIKE %s"
			, (f"%{name_filter}%", f"%{surname_filter}%", f"%{phone_filter}%"))
	res = cursor.fetchall()

	if output:
		for row in res:
			print(f"Name: {row[1]}, surname: {row[2]}, phone: {row[3]}")

	conn.commit()
	cursor.close()
	return res


# 5
def delete_data(name_filter=None, surname_filter=None, phone_filter=None, type="OR"): # type is "OR" or "AND"
	conn = connect()
	cursor = conn.cursor()

	res_list = query_data(name_filter, surname_filter, phone_filter, type)

	for row in res_list:
		user_id = row[0]
		print(f"Deleted: Name: {row[1]}, surname: {row[2]}, phone: {row[3]}")
		cursor.execute("DELETE FROM phonebook WHERE user_id = %s", (user_id,))
		cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))

	conn.commit()
	cursor.close()


if __name__ == "__main__":
	create_tables()
	upload_from_csv("data.csv")
	enter_name_phone()
	enter_name_phone("Lev", "Beloussov")
	update_data("Lev", "Beloussov", "0000")
	update_data("name", "surname", "0000")
	print(query_data(output=True))
	print(query_data("A", "B", "+77777777777", "AND", output=True))
	delete_data("Ex", "ample", 112, "AND")
	delete_data()