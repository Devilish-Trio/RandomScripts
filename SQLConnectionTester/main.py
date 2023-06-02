import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='<database name>',
                                         user='root',
                                         password='<password>')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM your_table LIMIT 10;")  # replace 'your_table' with the name of your table

        rows = cursor.fetchall()
        for row in rows:
            print(row)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
