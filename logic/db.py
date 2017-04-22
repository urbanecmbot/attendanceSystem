import oursql

def connect():
	conn = oursql.connect(host="localhost", user="attendanceSystem", passwd="somerandomgiberlish", db="attendanceSystem", charset="utf8", use_unicode=True)
	return conn

def read():
	conn = connect()
	cur = conn.cursor()
	with cur:
		cur.execute("select id, name, card_id, time from users;")
		data = cur.fetchall()
		print(data)

def write(name, card_id, time):
	conn = connect()
	cur = conn.cursor()
	with cur:
		#cur.execute("insert into users (id, name, card_id, time) values (NULL, 'Lukas Valec', 1342210118, '12:59:59');")
		cur.execute('insert into users (id, name, card_id, time) values (NULL, "' + name + '", "' + card_id + '", "' + time + '");', plain_query=True)

write('test', '31313', '12:59')
#read()
