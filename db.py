import mysql.connector

def insert_into_database(data):
    aux = ""
    for i, item in enumerate(data):
        if i == len(data)-1:
            aux += str(item)
        else:
            aux += f"{str(item)}, "
        
    print(aux)
    
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='Vestibular',
                                            user='flavio',
                                            password='')

        mySql_insert_query = f"""INSERT INTO Candidates (Name, Score) 
                            VALUES 
                            {aux}; """

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


data = [('AI for Marketing','2019-08-01'), ('ML for Sales','2019-05-15')]
insert_into_database(data)
