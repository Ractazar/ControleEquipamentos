import mysql.connector
import pandas as pd

HOST="localhost"
PORT=3306 
USER="root"     
PASSWORD="Dsgkaa1996!"
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
            dataframe = pd.read_sql(f"SELECT 1 FROM usuarios where Email='{email}' and Senha='{senha}'", connection)
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
    
def create_user(nome,email,senha,file_path):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        try:
            with open(file_path, 'rb') as file:
                binary_data = file.read()
                header = binary_data[:4]
                if header != b'%PDF':
                    return 2
        except Exception:
            return 2
        sql = "INSERT INTO usuarios (Nome, Email, Senha, DataCriacao, DocumentoAssinado) VALUES (%s, %s, %s, now(), %s);"
        cursor.execute(sql,(nome,email,senha,binary_data))

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

def stock_status():
    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        sql = """SELECT 'Em Uso' as _Status, (SELECT COUNT(*) from Notebooks where _Status='Em Uso') as Notebooks, (SELECT COUNT(*) from Smartphones where _Status='Em Uso') as Smartphones
            union
            SELECT 'Estoque' as _Status, (SELECT COUNT(*) from Notebooks where _Status='Estoque') as Notebooks, (SELECT COUNT(*) from Smartphones where _Status='Estoque') as Smartphones
            union
            SELECT 'Manutenção' as _Status, (SELECT COUNT(*) from Notebooks where _Status='Manutenção') as Notebooks, (SELECT COUNT(*) from Smartphones where _Status='Manutenção') as Smartphones"""

        if connection.is_connected():
            dataframe = pd.read_sql(sql, connection)
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

def notebook_stock(email):
    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        if connection.is_connected():
            dataframe = pd.read_sql("SELECT Marca,Modelo,Processador,Memoria_ram,Sistema_operacional,Memoria_interna,Id_dispositivo,Id_produto,Serial_number,_Status,Observacoes,Criado_por,Modificado_por,Emprestado,Ultimo_comeco_manutencao,Ultimo_final_manutencao FROM Notebooks", connection)
            connection.close()
            dataframe['Emprestado'] = dataframe['Emprestado'].apply(lambda x: 'Sim' if (x != 'Não') and (x != email) else x)
            return dataframe
        else:
            return 0
    except mysql.connector.Error:
        try:
            connection.close()
        except:
            pass
        return 0
    
def smartphone_stock(email):
    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        if connection.is_connected():
            dataframe = pd.read_sql("SELECT Marca,Modelo,Numero_serie,Numero_chip,Imei_1,Imei_2,_Status,Capa_protetora,Carregador,Criado_por,Modificado_por,Emprestado,Ultimo_comeco_manutencao,Ultimo_final_manutencao FROM Smartphones", connection)
            connection.close()
            dataframe['Emprestado'] = dataframe['Emprestado'].apply(lambda x: 'Sim' if (x != 'Não') and (x != email) else x)
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
    
def update_notebook(column_name, column_value, id_value, email, was_maintenance):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        if (column_name=='_Status') and (was_maintenance):
            cursor.execute(f"UPDATE notebooks SET {column_name}='{column_value}', Modificado_por='{email}', Ultimo_final_manutencao=NOW() where Id_dispositivo = '{id_value}';")
        elif (column_name=='_Status') and (column_value=='Manutenção'):
            cursor.execute(f"UPDATE notebooks SET {column_name}='{column_value}', Modificado_por='{email}', Ultimo_comeco_manutencao=NOW() where Id_dispositivo = '{id_value}';")
        else:
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
    
def update_smartphone(column_name, column_value, serial_number, email, was_maintenance):

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

        if (column_name=='_Status') and (was_maintenance):
            cursor.execute(f"UPDATE smartphones SET {column_name}='{column_value}', Modificado_por='{email}', Ultimo_final_manutencao=NOW() where Numero_serie = '{serial_number}';")
        elif (column_name=='_Status') and (column_value=='Manutenção'):
            cursor.execute(f"UPDATE smartphones SET {column_name}='{column_value}', Modificado_por='{email}', Ultimo_comeco_manutencao=NOW() where Numero_serie = '{serial_number}';")
        else:
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

        if status=='Manutenção':
            cursor.execute(f"INSERT INTO Notebooks (Marca,Modelo,Processador,Memoria_ram,Sistema_operacional,Memoria_interna,Id_dispositivo,Id_produto,Serial_number,_Status,Observacoes,Criado_por,Ultimo_comeco_manutencao) VALUES ('{marca}','{modelo}','{processador}','{memoria_ram}','{sistema_operacional}','{memoria_interna}','{id_dispositivo}','{id_produto}','{serial_number}','{status}','{observacoes}','{email}',NOW());")
        else:
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

        if status=='Manutenção':
            cursor.execute(f"INSERT INTO Smartphones (Marca,Modelo,Numero_serie,Numero_chip,Imei_1,Imei_2,_Status,Capa_protetora,Carregador,Criado_por,Ultimo_comeco_manutencao) VALUES ('{marca}','{modelo}','{numero_serie}','{numero_chip}','{imei_1}','{imei_2}','{status}','{capa_protetora}','{carregador}','{email}',NOW());")
        else:
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
    
def check_office(email):
    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        if connection.is_connected():
            dataframe = pd.read_sql(f"select Email,Senha,Versao,Data_renovacao,CASE WHEN CURRENT_DATE<Data_renovacao THEN 'Ativado' ELSE 'Desativado' END as _Status from Office where Email='{email}';", connection)
            connection.close()
            dataframe['Data_renovacao'] = dataframe['Data_renovacao'].apply(lambda x: x.strftime('%d/%m/%Y'))
            return dataframe
        else:
            return 0
    except mysql.connector.Error:
        try:
            connection.close()
        except:
            pass
        return 0
    
def add_office(email,senha,versao,renovacao):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO Office (Email,Senha,Versao,Data_renovacao) VALUES ('{email}','{senha}','{versao}','{renovacao}');")

        connection.commit()
        cursor.close()
        connection.close()

        return 0

    except mysql.connector.Error:
        try:
            cursor.close()
        except:
            pass
        try:
            connection.close()
        except:
            pass
        return 1
    
def update_office(email,senha,versao,renovacao):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        cursor.execute(f"UPDATE Office SET Senha = '{senha}', Versao = '{versao}', Data_renovacao = '{renovacao}' where Email = '{email}';")

        connection.commit()
        cursor.close()
        connection.close()

        return 0

    except mysql.connector.Error:
        try:
            cursor.close()
        except:
            pass
        try:
            connection.close()
        except:
            pass
        return 1
    
def borrow_notebook(email, id_value):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        cursor.execute(f"UPDATE notebooks SET Emprestado = '{email}' where Id_dispositivo = '{id_value}';")

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
    
def borrow_smartphone(email, numero_serie):

    try:
        connection = mysql.connector.connect(
            host=HOST, 
            port=PORT,
            user=USER,     
            password=PASSWORD,  
            database=DATABASE 
        )

        cursor = connection.cursor()

        cursor.execute(f"UPDATE smartphones SET Emprestado = '{email}' where Numero_serie = '{numero_serie}';")

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