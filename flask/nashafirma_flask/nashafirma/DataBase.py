import sqlite3
import time
import math
import re
from flask import url_for, flash


class DataBase:
    def __init__(self, db, menu):
        self.__db = db
        self.__cur = db.cursor()
        self.menu = menu

    def getMenu(self):
        return self.menu

    def allProducts(self):
        try:
            self.__cur.execute('SELECT * FROM products_list')
            contacts = self.__cur.fetchall()
            if contacts:
                return contacts
        except sqlite3.Error as e:
            print("Error got product dor DB " + str(e))
        return True

    def addProduct(self, product, price, note):
        try:
            self.__cur.execute('SELECT product FROM products_list WHERE product = ?', (product,))
            existing_product = self.__cur.fetchone()
            if existing_product:
                flash(f'Error: Product "{product}" already exists')
            elif len(product) <= 2:
                flash('Product name must be at least 3 characters long')
            else:
                self.__cur.execute('INSERT INTO products_list (product, price, note) VALUES (?, ?, ?)',
                                   (product, price, note))
                self.__db.commit()

        except sqlite3.Error as e:
            print("Error added product dor DB " + str(e))
            return False
        return True

    def delProduct(self, product):
        try:
            self.__cur.execute('DELETE FROM products_list WHERE product = ?', (product,))
            self.__cur.fetchone()
            self.__db.commit()

        except sqlite3.Error as e:
            print("Error delete product dor DB " + str(e))
            return False
        return True

    def editProduct(self, new_product, new_price, new_note, product):
        try:
            # Check if the new product name already exists in the database
            self.__cur.execute('SELECT product FROM products_list WHERE product = ?', (new_product,))
            existing_product = self.__cur.fetchone()
            if existing_product and existing_product['product'] != product:
                flash(f'Error: Product "{new_product}" already exists')
            elif len(new_product) <= 2:
                flash('Product name must be at least 3 characters long')
            else:
                self.__cur.execute('UPDATE products_list SET product = ?, price = ?, note = ? WHERE product = ?',
                                   (new_product, new_price, new_note, product))
                self.__db.commit()

        except sqlite3.Error as e:
            print("Error editing product in DB " + str(e))
            return False
        return True

    def allOrders(self):
        try:
            self.__cur.execute('SELECT * FROM orders_list')
            orders = self.__cur.fetchall()
            if orders:
                return orders
        except sqlite3.Error as e:
            print("Error got product dor DB " + str(e))
        return True

    def addUser(self, name, email, hpsw):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Пользователь с таким email уже существует")
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, NULL, ?)", (name, email, hpsw, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления пользователя в БД " + str(e))
            return False

        return True

    def getProduct(self, product):
        try:
            self.__cur.execute('SELECT product, price, note FROM products_list WHERE product = ?', (product,))
            product = self.__cur.fetchone()
            if not product:
                print("Пользователь не найден")
                return False

            return product
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))

        return False

    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))

        return False

    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))

        return False

    def updateUserAvatar(self, avatar, user_id):
        if not avatar:
            return False

        try:
            binary = sqlite3.Binary(avatar)
            self.__cur.execute(f"UPDATE users SET avatar = ? WHERE id = ?", (binary, user_id))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка обновления аватара в БД: " + str(e))
            return False
        return True