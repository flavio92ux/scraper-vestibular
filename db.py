import mysql.connector
from dotenv import dotenv_values

config = dotenv_values(".env")

def insert_into_database(data):
    db_name = config['DATABASE']
    db_host = config['HOST']
    db_user = config['USER']
    db_password = config['PASSWORD']


    print(f"Salvando no banco de dados {db_name}")
    aux = ""
    for i, item in enumerate(data):
        if i == len(data)-1:
            aux += str(item)
        else:
            aux += f"{str(item)}, "

    
    try:
        connection = mysql.connector.connect(host=db_host,
                                            user=db_user,
                                            password=db_password)
        
        cursor = connection.cursor()
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')

        connection = mysql.connector.connect(host=db_host,
                                            database=db_name,
                                            user=db_user,
                                            password=db_password)
        cursor = connection.cursor()

        stmt = "SHOW TABLES LIKE 'Candidates'"
        cursor.execute(stmt)
        result = cursor.fetchone()

        mySql_Create_Table_Query = """CREATE TABLE Candidates ( 
                             Id int(11) AUTO_INCREMENT NOT NULL,
                             Name varchar(250) NOT NULL,
                             Score varchar(250) NOT NULL,
                             PRIMARY KEY (Id)) """
        

        mySql_insert_query = f"""INSERT INTO Candidates (Name, Score) 
                            VALUES 
                            {aux}; """

        if not result:
            cursor.execute(mySql_Create_Table_Query)
        cursor.execute(mySql_insert_query)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Candidates table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Candidates table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
