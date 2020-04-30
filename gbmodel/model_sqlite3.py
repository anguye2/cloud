"""
This is the sqlite database for the Food Carts flask app
+-----------+--------------+-----------+--------+-----------+----------------+---------------+-----------+
| Name      | address      |  city     | state  |  zipcode  | hours          |    phone      |  rating  |
+===========+==============+===========+========+===========+================+===============+===========+
| Esan Thai | 13551 SE     | Portland  |  OR    |   97051   |  11 AM - 8 PM  | 971 350 9867  | 5         |
+-----------+--------------+-----------+--------+-----------+----------------+---------------+-----------+
"""

from .Model import Model
import sqlite3
DB_FILE = 'foodcart.db'

class model(Model):
    def __init__(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from foodcart")
        except sqlite3.OperationalError:
            cursor.execute("create table foodcart (name, address, city, state, zipcode, hour, phone, rating)")
        cursor.close()
    
    def select(self):
        """
        Get all rows from the food cart database
        Each row contains: name, address, city, state, zipcode, hour, phone, rating
        :return List of lists containg all row of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM foodcart")
        return cursor.fetchall()
    
    def insert(self, name, address, city, state, zipcode, hour, phone, rating):
        """
        Insert data into the database
        :param name: String
        :param address: String
        :param city: String
        :param state: String
        :param zipcode: String
        :param hour: String
        :param phone: String
        :param rating: String
        :return: True
        :raises: Database errors on connection and insertion
        """
    
        params = {'name': name, 'address': address, 'city': city, 'state': state, 'zipcode': zipcode, 'hour': hour, 'phone': phone, 'rating': rating }
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into foodcart (name, address, city, state, zipcode, hour, phone, rating) VALUES (:name, :address, :city, :state, :zipcode, :hour, :phone, :rating)", params)

        connection.commit()
        cursor.close()
        return True
    
