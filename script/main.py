import json
from mysql_class import Mysql as m
import os
from pprint import pprint

class ShopMysql(m):    
    def __init__(self, **mysql_user):
        super().__init__(**mysql_user)
    
    def create_custom_table(self, table_name):
        self.table = table_name.lower()
        self.execute_query(f"CREATE TABLE IF NOT EXISTS {self.table} (id INT AUTO_INCREMENT PRIMARY KEY, item VARCHAR(255), price FLOAT)")
        print(f'\t[INFO]: Table {self.table} was created')
    
    def create_shop(self, table_name):
        self.connect()
        #try:
        self.execute_query('CREATE DATABASE db_shop')
        #except ValueError:
        #    print('\t[INFO]: Database db_shop is exist.')
        #else:
            #print('\t[INFO]: Database db_shop was created.')
        self.execute_query('USE db_shop')
        print('\t[INFO]: Database db_shop was selected.')
        self.create_custom_table(str(table_name))
        
    def show_databases(self):
        return self.execute_query(f'SHOW databases')
        
        
    def add_item(self, item='', price='', path=''):
        """Method add_item - will add records to the "shop" table. Params: item, price"""
        if path:
            try:
                with open(path) as f:
                    shop_items = json.load(f)
                    for key, value in shop_items.items():
                        self.execute_query(f"INSERT INTO {self.table} (item, price) VALUES ('{str(key)}', {float(value)})")
            except FileNotFoundError:
                raise FileNotFoundError(f"\t[ERROR]: File {os.path.basename(path)} not found.")
        elif item and price:
            if ',' in str(price):
                price = price.replace(',','.')
            try:
                self.execute_query(f"INSERT INTO {self.table} (item, price) VALUES ('{item}', {float(price)})")
            except ValueError:
                raise ValueError('Failed on writing data (item, price) yo mysql DB.')
        else:
            print("Incorrect data or type of arguments. Please, check the input again.")
        print("\t[INFO]: In tables was added a new rows.")
    
    def show_table(self):
        print(f"Data in DB at this moment\n")
        pprint(self.execute_query(f'SELECT * FROM {self.table}'))
    
    def delete_item(self, *extra_items):
        """Method delete_item - will remove item from "shop" by name"""
        for item in extra_items if not None else Exception('A method delete_item wants 1 argument and more'):
            table_before = self.execute_query(f'SELECT COUNT(*) from {self.table}')
            self.execute_query(f'DELETE FROM {self.table} WHERE item = "{item}"')
            table_after = self.execute_query(f'SELECT COUNT(*) from {self.table}')
            if table_after == table_before:
                raise FileExistsError(f'This item doesnt exists on table {self.table}')
            else:
                print(f'\t[WARNING]: The item "{item}" was removed.')
    
    def delete_shop(self):
        """Method delete_shop - will drop "shop" table"""
        self.execute_query(f"DROP TABLE IF EXISTS {self.table}")
        print(f"\t[WARNING] Table {self.table} was deleted.")


CONNECT = {
    "host": os.environ.get("MYSQL_HOST", 'mysql'),
    "user": os.environ.get("MYSQL_USER", 'root'),
    "password": os.environ.get("MYSQL_PASSWORD", 'password')
}

if __name__ == '__main__':
    my_shop = ShopMysql(**CONNECT)
    my_shop.create_shop('shop')
    my_shop.add_item(item='Lucky me: A Memoir', price=22.31)
    my_shop.show_table()
    my_shop.add_item(path='items_and_price.json')

    my_shop.delete_item("Iron Flame", "The Way Forward")
    #my_shop.delete_shop()