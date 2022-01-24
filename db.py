import mysql.connector

def insert_into_database(data):
    print("Salvando no banco de dados")
    aux = ""
    for i, item in enumerate(data):
        if i == len(data)-1:
            aux += str(item)
        else:
            aux += f"{str(item)}, "

    
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='Vestibular',
                                            user='flavio',
                                            password='')
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
