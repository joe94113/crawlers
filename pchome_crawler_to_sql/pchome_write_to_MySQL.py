import requests
import mysql.connector
from mysql.connector import errorcode
import time

DB_NAME = 'pchome'

try:
    cnx = mysql.connector.connect(user='root', password='joe94113', host='127.0.0.1')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print('successfully connected to MySQL server')

cursor = cnx.cursor()


# create database if not exist
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

# creating table

TABLES = {}
TABLES['products'] = (
    "CREATE TABLE `products` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(50) NOT NULL,"
    "  `price` int NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

add_product = ("INSERT INTO products "
               "(name, price) "
               "VALUES (%s, %s)")

for i in range(1, 100):
    SONYSOUND_PCHOME_URL = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=sony%E9%9F%B3%E9%9F%BF&page={}&sort=sale/dc'.format(
        i)
    reqs = requests.get(SONYSOUND_PCHOME_URL)
    if reqs.status_code == requests.codes.ok:
        data = reqs.json()
        for product in data['prods']:
            name = product['name']
            if len(name) > 50:
                name = name[0:50]
            price = product['price']
            print(name)
            print(price)
            data_product = (name, price)
            # Insert new employee
            cursor.execute(add_product, data_product)
            time.sleep(3)

# Make sure data is committed to the database        
cnx.commit()
print('closing')

cursor.close()
cnx.close()
