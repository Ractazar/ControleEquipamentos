import mysql.connector
import pandas as pd

HOST="localhost"
PORT=3306 
USER="root"     
PASSWORD="SuaSenha"
DATABASE="controle_de_equipamentos"

def check_user(email, senha):
    try:
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
    except mysql.connector.Error:
        try:
            connection.close()
        except:
            pass
        return 2
    
def check_email(email):

    try:
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
    except mysql.connector.Error:
        try:
            connection.close()
        except:
            pass
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
        try:
            cursor.close()
        except:
            pass
        try:
            connection.close()
        except:
            pass
        return 0

def notebook_stock():
    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        if connection.is_connected():
            dataframe = pd.read_sql("SELECT Marca,Modelo,Processador,Memoria_ram,Sistema_operacional,Memoria_interna,Id_dispositivo,Id_produto,Serial_number,_Status,Observacoes FROM Notebooks", connection)
            connection.close()
            return dataframe
        else:
            return 0
    except mysql.connector.Error:
        try:
            connection.close()
        except:
            pass
        return 0
    
def smartphone_stock():
    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        if connection.is_connected():
            dataframe = pd.read_sql("SELECT Marca,Modelo,Numero_serie,Numero_chip,Imei_1,Imei_2,_Status,Capa_protetora,Carregador FROM Smartphones", connection)
            connection.close()
            dataframe['Capa_protetora'] = dataframe['Capa_protetora'].apply(lambda x: 'Sim' if x == 1 else 'Não')
            dataframe['Carregador'] = dataframe['Carregador'].apply(lambda x: 'Sim' if x == 1 else 'Não')
            return dataframe
        else:
            return 0
    except mysql.connector.Error:
        try:
            connection.close()
        except:
            pass
        return 0
    
def update_notebook(column_name, column_value, id_value, email):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        cursor.execute(f"UPDATE notebooks SET {column_name}='{column_value}', Modificado_por='{email}' where Id_dispositivo = '{id_value}';")

        connection.commit()
        cursor.close()
        connection.close()

        return 1

    except mysql.connector.Error:
        try:
            cursor.close()
        except:
            pass
        try:
            connection.close()
        except:
            pass
        return 0
    
def update_smartphone(column_name, column_value, serial_number, email):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )


        if column_name=='Capa_protetora' or column_name=='Carregador':
            if column_value == 'Sim':
                column_value = 1
            else:
                column_value = 0
        cursor = connection.cursor()
        cursor.execute(f"UPDATE smartphones SET {column_name}='{column_value}', Modificado_por='{email}' where Numero_serie = '{serial_number}';")

        connection.commit()
        cursor.close()
        connection.close()

        return 1

    except mysql.connector.Error:
        try:
            cursor.close()
        except:
            pass
        try:
            connection.close()
        except:
            pass
        return 0
    
def add_notebook(marca,modelo,processador,memoria_ram,sistema_operacional,memoria_interna,id_dispositivo,id_produto,serial_number,status,observacoes,email):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO Notebooks (Marca,Modelo,Processador,Memoria_ram,Sistema_operacional,Memoria_interna,Id_dispositivo,Id_produto,Serial_number,_Status,Observacoes,Criado_por) VALUES ('{marca}','{modelo}','{processador}','{memoria_ram}','{sistema_operacional}','{memoria_interna}','{id_dispositivo}','{id_produto}','{serial_number}','{status}','{observacoes}','{email}');")

        connection.commit()
        cursor.close()
        connection.close()

        return 1

    except mysql.connector.Error:
        try:
            cursor.close()
        except:
            pass
        try:
            connection.close()
        except:
            pass
        return 0
    
def add_smartphone(marca,modelo,numero_serie,numero_chip,imei_1,imei_2,status,capa_protetora,carregador,email):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO Smartphones (Marca,Modelo,Numero_serie,Numero_chip,Imei_1,Imei_2,_Status,Capa_protetora,Carregador,Criado_por) VALUES ('{marca}','{modelo}','{numero_serie}','{numero_chip}','{imei_1}','{imei_2}','{status}','{capa_protetora}','{carregador}','{email}');")

        connection.commit()
        cursor.close()
        connection.close()

        return 1

    except mysql.connector.Error:
        try:
            cursor.close()
        except:
            pass
        try:
            connection.close()
        except:
            pass
        return 0
    
def delete_notebook(id_dispositivo):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        cursor.execute(f"DELETE FROM Notebooks WHERE Id_dispositivo = '{id_dispositivo}';")
        cursor.fetchall()
        success = cursor.rowcount
        connection.commit()
        cursor.close()
        connection.close()

        return success

    except mysql.connector.Error:
        try:
            cursor.close()
        except:
            pass
        try:
            connection.close()
        except:
            pass
        return ''
    
def delete_smartphone(numero_serie):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        cursor.execute(f"DELETE FROM Smartphones WHERE Numero_serie = '{numero_serie}';")
        cursor.fetchall()
        success = cursor.rowcount
        connection.commit()
        cursor.close()
        connection.close()

        return success

    except mysql.connector.Error:
        try:
            cursor.close()
        except:
            pass
        try:
            connection.close()
        except:
            pass
        return ''