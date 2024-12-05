from classes.client_manager import ClientManager
from classes.shop_manger import ShopManager


# Тесты на client_manger
def test_client_get_all_shops():
	client_manger = ClientManager("Иванов С.А.")
	print(client_manger.get_all_shops())


def test_client_last_added_shop():
	client_manger = ClientManager("Иванов С.А.")
	print(client_manger.get_last_added_shop())


# Тесты на shop_manger
def test_shop_manager_get_all_clients():
	shop_manager = ShopManager("Домашний уют")
	print(shop_manager.get_all_clients())


def test_shop_manger_count_clients():
	shop_manager = ShopManager("Домашний уют")
	print(shop_manager.count_clients())


def test_shop_manger_add_client():
	shop_manager = ShopManager("Домашний уют")
	shop_manager.add_client("Иванова И.Я.")


def test_shop_manger_del_client():
	shop_manager = ShopManager("Домашний уют")
	shop_manager.del_client_from_relations("Иванова И.Я.")