import sqlite3


class Client:
	def __init__(self, client_id=None, client_name=None):
		self.__table_name = "clients"
		self.__db_name = "shops_clients.db"
		self.__con = sqlite3.connect(self.__db_name)
		self.__con.row_factory = sqlite3.Row
		self.__cur = self.__con.cursor()

		self.client_id = client_id
		self.client_name = client_name

	def __repr__(self):
		return f"Client(id={self.client_id}, name={self.client_name})"

	@property
	def table_name(self):
		return self.__table_name

	def fetch_by_name(self, name):
		query = f"SELECT * FROM {self.__table_name} WHERE client_name = ?"
		self.__cur.execute(query, (name, ))
		row = self.__cur.fetchone()
		if row:
			return Client(**row)
		else:
			raise ValueError

	def add_client(self, name):
		query = (
			f"INSERT INTO {self.__table_name} "
			f"(client_name) VALUES (?);"
		)
		self.__cur.execute(query, (name,))
		self.__cur.connection.commit()

