import unittest
import connector
import LoanControl
import StockControl
import UserLogin
import pandas
import datetime
import mysql.connector

class TestConnectorMethodsUnableConnect(unittest.TestCase):

    def setUp(self):
        connector.PASSWORD = "random"

    def test_check_user(self):
        self.assertEqual(connector.check_user('teste@gmail.com', 'senha'), 2)

    def test_check_email(self):
        self.assertEqual(connector.check_email('teste@gmail.com'), 2)

    def test_create_user(self):
        self.assertEqual(connector.create_user('Teste1','teste1@gmail.com','senha','C:/Users/Guto/Downloads/Gustavo Krueger- Termo de Responsabilidade.pdf'), 0)

    def test_notebook_stock(self):
        self.assertEqual(connector.notebook_stock('t@gmail.com'), 0)  

    def test_smartphone_stock(self):
        self.assertEqual(connector.smartphone_stock('t@gmail.com'), 0)  

    def test_update_notebook(self):
        self.assertEqual(connector.update_notebook('_Status', 'Estoque', 'teste2', 'teste@gmail.com', False), 0)  

    def test_update_smartphone(self):
        self.assertEqual(connector.update_smartphone('_Status', 'Estoque', 'teste', 'teste@gmail.com', False), 0) 

    def test_delete_notebook(self):
        self.assertEqual(connector.delete_notebook('id_dispositivo'), '')    

    def test_add_notebook(self):
        self.assertEqual(connector.add_notebook('marca','modelo','processador','memoria_ram','sistema_operacional','memoria_interna','id_dispositivo','id_produto','serial_number','Estoque','observacoes','teste@gmail.com'), 0) 

    def test_delete_smartphone(self):
        self.assertEqual(connector.delete_smartphone('numero_serie'), '') 

    def test_add_smartphone(self):
        self.assertEqual(connector.add_smartphone('marca','modelo','numero_serie','numero_chip','imei_1','imei_2','status',0,0,'teste@gmail.com'), 0) 

    def test_check_office(self):
        self.assertEqual(connector.check_office('teste@gmail.com'), 0)  

    def test_update_office(self):
        self.assertEqual(connector.update_office('teste@gmail.com','1234','2.0',datetime.datetime.now()), 1)  

    def test_borrow_notebook(self):
        self.assertEqual(connector.borrow_notebook('teste@gmail.com','id_dispositivo'), 0)  

    def test_borrow_smartphone(self):
        self.assertEqual(connector.borrow_smartphone('teste@gmail.com','numero_serie'), 0)  

    def tearDown(self):
        connector.PASSWORD = "Dsgkaa1996!"
    
class TestConnectorMethods(unittest.TestCase):

    def test_check_user_returns_dataframe(self):
        self.assertEqual(connector.check_user('teste@gmail.com', 'senha'), 1)

    def test_check_user_returns_empty_dataframe(self):
        self.assertEqual(connector.check_user('abcd@gmail.com', 'abcd'), 0)

    def test_check_email_returns_dataframe(self):
        self.assertEqual(connector.check_email('teste@gmail.com'), 0)

    def test_check_email_returns_empty_dataframe(self):
        self.assertEqual(connector.check_email('abcd@gmail.com'), 1)

    def test_create_user_returns_pdf(self):
        delete_user()
        self.assertEqual(connector.create_user('Teste1','teste1@gmail.com','senha','C:/Users/Guto/Downloads/Gustavo Krueger- Termo de Responsabilidade.pdf'), 1)

    def test_create_user_returns_invalid_file(self):
        self.assertEqual(connector.create_user('Teste','teste@gmail.com','senha','C:/Users'), 2)

    def test_notebook_stock_returns_dataframe(self):
        self.assertIsInstance(connector.notebook_stock('t@gmail.com'), pandas.DataFrame)  

    def test_smartphone_stock_returns_dataframe(self):
        self.assertIsInstance(connector.smartphone_stock('t@gmail.com'), pandas.DataFrame)  

    def test_update_notebook_successful(self):
        self.assertEqual(connector.update_notebook('_Status', 'Estoque', 'teste2', 'teste@gmail.com', False), 1)  

    def test_update_smartphone_successful(self):
        self.assertEqual(connector.update_smartphone('_Status', 'Estoque', 'teste', 'teste@gmail.com', False), 1) 

    def test_delete_notebook_in_database(self):
        self.assertEqual(connector.delete_notebook('id_dispositivo'), 1)    

    def test_add_notebook_returns_dataframe(self):
        self.assertEqual(connector.add_notebook('marca','modelo','processador','memoria_ram','sistema_operacional','memoria_interna','id_dispositivo','id_produto','serial_number','Estoque','observacoes','teste@gmail.com'), 1) 

    def test_delete_notebook_not_in_database(self):
        self.assertEqual(connector.delete_notebook('nonsense'), 0) 

    def test_delete_smartphone_in_database(self):
        self.assertEqual(connector.delete_smartphone('numero_serie'), 1) 

    def test_add_smartphone_returns_dataframe(self):
        self.assertEqual(connector.add_smartphone('marca','modelo','numero_serie','numero_chip','imei_1','imei_2','status',0,0,'teste@gmail.com'), 1) 

    def test_delete_smartphone_not_in_database(self):
        self.assertEqual(connector.delete_smartphone('nonsense'), 0) 

    def test_check_office_returns_dataframe(self):
        self.assertIsInstance(connector.check_office('teste@gmail.com'), pandas.DataFrame)  

    def test_add_office_returns_dataframe(self):
        delete_office()
        self.assertEqual(connector.add_office('teste1@gmail.com','1234','1.0',datetime.datetime.now()), 0)  

    def test_update_office_successful(self):
        self.assertEqual(connector.update_office('teste@gmail.com','1234','2.0',datetime.datetime.now()), 0)  

    def test_borrow_notebook_successful(self):
        self.assertEqual(connector.borrow_notebook('teste@gmail.com','id_dispositivo'), 1)  

    def test_borrow_smartphone_successful(self):
        self.assertEqual(connector.borrow_smartphone('teste@gmail.com','numero_serie'), 1)  

def delete_user():

    try:
        connection = mysql.connector.connect(
            host="localhost", 
            port=3306,
            user="root" ,     
            password="Dsgkaa1996!",  
            database="controle_de_equipamentos" 
        )

        cursor = connection.cursor()

        cursor.execute("DELETE FROM usuarios WHERE Email = 'teste1@gmail.com';")
        cursor.fetchall()
        success = cursor.rowcount
        connection.commit()
        cursor.close()
        connection.close()

        return success

    except mysql.connector.Error:
        try:
            cursor.close()
        except Exception:
            pass
        try:
            connection.close()
        except Exception:
            pass
        return ''
    
def delete_office():

    try:
        connection = mysql.connector.connect(
            host="localhost", 
            port=3306,
            user="root" ,     
            password="Dsgkaa1996!",  
            database="controle_de_equipamentos" 
        )

        cursor = connection.cursor()

        cursor.execute("DELETE FROM office WHERE Email = 'teste1@gmail.com';")
        cursor.fetchall()
        success = cursor.rowcount
        connection.commit()
        cursor.close()
        connection.close()

        return success

    except mysql.connector.Error:
        try:
            cursor.close()
        except Exception:
            pass
        try:
            connection.close()
        except Exception:
            pass
        return ''

if __name__ == '__main__':
    unittest.main()