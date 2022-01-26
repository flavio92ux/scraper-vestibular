import mysql.connector
import os
from dotenv import load_dotenv 

load_dotenv()

def insert_into_database(data):
    db_name = os.environ['MYSQL_DATABASE']
    db_host = os.environ['MYSQL_HOST']
    db_user = os.environ['MYSQL_USER']
    db_password = os.environ['MYSQL_PASSWORD']


    print(f"Salvando no banco de dados {db_name}")


    # Salva tuplas em formato de string com formatação
    # correta para introduzir query no mySQL

    candidates = ""

    for i, item in enumerate(data):
        if i == len(data)-1:
            candidates += str(item)
        else:
            candidates += f"{str(item)}, "

    
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
                             CPF varchar(250) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Score varchar(250) NOT NULL,
                             PRIMARY KEY (Id)) """
        

        mySql_insert_query = f"""INSERT INTO Candidates (CPF, Name, Score) 
                            VALUES 
                            {candidates}; """

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

