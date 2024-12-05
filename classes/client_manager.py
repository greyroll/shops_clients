import sqlite3

from classes.client import Client
from classes.shop import Shop
from classes.shops_clients_relations import ShopsClientsRelations


class ClientManager:
	def __init__(self, client_name):
		self.__db_name = "shops_clients.db"
		self.__con = sqlite3.connect(self.__db_name)
		self.__con.row_factory = sqlite3.Row
		self.__cur = self.__con.cursor()
		self.shops = Shop()
		client = Client()
		self.client = client.fetch_by_name(client_name)
		self.relations = ShopsClientsRelations()

	def get_all_shops(self):

		query = (
			f"SELECT shops.shop_id, shops.shop_name, shops.shop_address FROM {self.shops.table_name} "
			f"LEFT JOIN {self.relations.table_name} as relations "
			f"ON shops.shop_id = relations.shop_id "
			f"LEFT JOIN {self.client.table_name} "
			f"ON relations.client_id = clients.client_id "
			f"WHERE clients.client_id = ?"
		)

		self.__cur.execute(query, (self.client.client_id,))
		shops_found = []
		for row in self.__cur.fetchall():
			shops_found.append(Shop(**row))
		return shops_found

	def get_last_added_shop(self):
		query = (
			f"SELECT shops.shop_id, shops.shop_name, shops.shop_address FROM {self.shops.table_name} " 
			f"LEFT JOIN {self.relations.table_name} as relations "
			f"ON shops.shop_id = relations.shop_id "
			f"LEFT JOIN {self.client.table_name} "
			f"ON relations.client_id = clients.client_id "
			f"WHERE clients.client_id = ? "
			f"ORDER BY shops.shop_id DESC LIMIT 1"
		)

		self.__cur.execute(query, (self.client.client_id, ))
		last_record = self.__cur.fetchone()
		if last_record:
			return Shop(**last_record)






