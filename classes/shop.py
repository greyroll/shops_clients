import sqlite3


class Shop:
	def __init__(self, shop_id=None, shop_name=None, shop_address=None):
		self.__table_name = "shops"
		self.__db_name = "shops_clients.db"
		self.__con = sqlite3.connect(self.__db_name)
		self.__con.row_factory = sqlite3.Row
		self.__cur = self.__con.cursor()

		self.shop_id = shop_id
		self.shop_name = shop_name
		self.shop_address = shop_address

	def __repr__(self):
		return f"Shop(id={self.shop_id}, name={self.shop_name}, address={self.shop_address})"

	@property
	def table_name(self):
		return self.__table_name

	def fetch_all(self):
		query = f"SELECT * FROM {self.__table_name}"
		self.__cur.execute(query)
		all_shops = []
		for row in self.__cur.fetchall():
			all_shops.append(Shop(**row))
		return all_shops

	def fetch_by_id(self, shop_id):
		query = f"SELECT * FROM {self.__table_name} WHERE shop_id = ?"
		self.__cur.execute(query, (shop_id, ))
		row = self.__cur.fetchone()
		if row:
			return Shop(**row)
		else:
			return "Запись не найдена"

	def fetch_by_name(self, name):
		query = f"SELECT * FROM {self.__table_name} WHERE shop_name = ?"
		self.__cur.execute(query, (name, ))
		row = self.__cur.fetchone()
		if row:
			return Shop(**row)
		else:
			raise ValueError



