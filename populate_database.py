import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Vestibular',
                                         user='flavio',
                                         password='')

    mySql_Create_Table_Query = """CREATE TABLE Candidates ( 
                             Id int(11) AUTO_INCREMENT NOT NULL,
                             Name varchar(250) NOT NULL,
                             Score varchar(250) NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")