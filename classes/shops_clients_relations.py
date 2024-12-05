import sqlite3


class ShopsClientsRelations:
	def __init__(self, id=None, client_id=None, shop_id=None):
		self.__table_name = "shops_clients_relations"
		self.__db_name = "shops_clients.db"
		self.__con = sqlite3.connect(self.__db_name)
		self.__con.row_factory = sqlite3.Row
		self.__cur = self.__con.cursor()

		self.id = id
		self.client_id = client_id
		self.shop_id = shop_id

	@property
	def table_name(self):
		return self.__table_name



