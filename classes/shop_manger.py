import sqlite3

from classes.client import Client
from classes.shop import Shop
from classes.shops_clients_relations import ShopsClientsRelations


class ShopManager:
	def __init__(self, shop_name):
		self.__db_name = "shops_clients.db"
		self.__con = sqlite3.connect(self.__db_name)
		self.__con.row_factory = sqlite3.Row
		self.__cur = self.__con.cursor()
		self.clients = Client()
		shop = Shop()
		self.shop = shop.fetch_by_name(shop_name)
		self.relations = ShopsClientsRelations()

	def get_all_clients(self):
		query = (
			f"SELECT clients.client_id, clients.client_name FROM {self.clients.table_name} "
			f"LEFT JOIN {self.relations.table_name} as relations "
			f"ON clients.client_id = relations.client_id "
			f"LEFT JOIN {self.shop.table_name} "
			f"ON relations.shop_id = shops.shop_id "
			f"WHERE shops.shop_id = ?"
		)

		self.__cur.execute(query, (self.shop.shop_id,))
		clients_found = []
		for row in self.__cur.fetchall():
			clients_found.append(Client(**row))
		return clients_found

	def count_clients(self):
		return len(self.get_all_clients())

	def add_client(self, name):
		try:
			client_found = self.clients.fetch_by_name(name)
		except ValueError:
			self.clients.add_client(name)
			client_found = self.clients.fetch_by_name(name)

		for client in self.get_all_clients():
			if client.client_id == client_found.client_id:
				return print("У вас уже есть такой клиент")

		query = (
			f"INSERT INTO {self.relations.table_name} "
			f"(client_id, shop_id) "
			f"VALUES (?, ?)"
		)
		self.__cur.execute(query, (client_found.client_id, self.shop.shop_id))
		self.__cur.connection.commit()

	def del_client_from_relations(self, name):
		client_found = self.clients.fetch_by_name(name)
		query = (
			f"DELETE FROM {self.relations.table_name} "
			f"WHERE client_id = ?;"
		)
		self.__cur.execute(query, (client_found.client_id,))
		self.__cur.connection.commit()

