import mysql.connector
import pandas as pd

HOST="localhost"
PORT=3306
USER="root"     
PASSWORD="Dsgkaa1996!"
DATABASE="controle_de_equipamentos"

def check_user(email, senha):
    connection = mysql.connector.connect(
        host=HOST, 
        port=PORT,
        user=USER,     
        password=PASSWORD,  
        database=DATABASE 
    )

    if connection.is_connected():
        dataframe = pd.read_sql(f"SELECT * FROM usuarios where Email='{email}' and Senha='{senha}'", connection)
        connection.close()
        if dataframe.empty:
            return 0
        else:
            return 1
    else:
        return 2
    
def check_email(email):
    connection = mysql.connector.connect(
        host=HOST, 
        port=PORT,
        user=USER,     
        password=PASSWORD,  
        database=DATABASE 
    )

    if connection.is_connected():
        dataframe = pd.read_sql(f"SELECT * FROM usuarios where Email='{email}'", connection)
        connection.close()
        if dataframe.empty:
            return 1
        else:
            return 0
    else:
        return 2
    
def create_user(nome,email,senha):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO usuarios (Nome, Email, Senha, DataCriacao) VALUES ('{nome}', '{email}', '{senha}', now());")

        connection.commit()
        cursor.close()
        connection.close()

        return 1

    except mysql.connector.Error:
        cursor.close()
        connection.close()
        return 0
