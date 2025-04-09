import connector
import UserLogin
import LoanControl
from PyQt5 import QtCore, QtWidgets
QAbstractTableModel = QtCore.QAbstractTableModel
Qt = QtCore.Qt
QModelIndex = QtCore.QModelIndex
pyqtSignal = QtCore.pyqtSignal
import pandas as pd
import pdfkit

def welcome_screen(self):
    self.dataframe = connector.stock_status()
    self.dataframe2 = self.dataframe.copy()
    if isinstance(self.dataframe,int):
        
        self.w = UserLogin.MissingConnection()
        self.w.show()
        
        self.setObjectName("Sem conexão")
        self.setWindowTitle("Sem conexão")
        self.setFixedSize(320, 100)
        self.center_on_screen()

        self.nome_label = QtWidgets.QLabel(self)
        self.nome_label.setGeometry(QtCore.QRect(10, 5, 300, 50))
        self.nome_label.setText("                       Sem acesso ao banco de dados.")
        self.nome_label.show()

        self.push_button = QtWidgets.QPushButton(self)
        self.push_button.setGeometry(QtCore.QRect(10, 50, 300, 40))
        self.push_button.setObjectName("pushButton")
        self.push_button.setText("Tentar Novamente")
        self.push_button.clicked.connect(self.notebook_data)
        self.push_button.show()
         
        QtCore.QMetaObject.connectSlotsByName(self)
    else:
        self.setObjectName("Hardware Status")
        self.setWindowTitle("Hardware Status")
        self.setFixedSize(270, 200)
        self.center_on_screen()

        self.nome_label = QtWidgets.QLabel(self)
        self.nome_label.setGeometry(QtCore.QRect(10, 10, 300, 20))
        self.nome_label.setText("            Number of hardwares for each Status")
        self.nome_label.show()

        self.table_view = QtWidgets.QTableView(self)
        self.table_view.setGeometry(QtCore.QRect(10, 40, 250, 115))
        self.table_view.setObjectName("tableView")
        self.model = LoanControl.PandasModel2(self.dataframe)
        self.table_view.setModel(self.model)
        self.table_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_view.resizeColumnsToContents()
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.table_view.show()

        self.push_button = QtWidgets.QPushButton(self)
        self.push_button.setGeometry(QtCore.QRect(70, 165, 120, 22))
        self.push_button.setObjectName("pushButton")
        self.push_button.setText("Continue")
        self.push_button.clicked.connect(self.notebook_data)
        self.push_button.show()

def stock_control_notebooks(self):
    
    self.dataframe = connector.notebook_stock(self.logged_email)
    self.dataframe2 = self.dataframe.copy()
    if isinstance(self.dataframe,int):
        
        self.w = UserLogin.MissingConnection()
        self.w.show()
        
        self.setObjectName("Sem conexão")
        self.setWindowTitle("Sem conexão")
        self.setFixedSize(320, 100)
        self.center_on_screen()

        self.nome_label = QtWidgets.QLabel(self)
        self.nome_label.setGeometry(QtCore.QRect(10, 5, 300, 50))
        self.nome_label.setText("                       Sem acesso ao banco de dados.")
        self.nome_label.show()

        self.push_button = QtWidgets.QPushButton(self)
        self.push_button.setGeometry(QtCore.QRect(10, 50, 300, 40))
        self.push_button.setObjectName("pushButton")
        self.push_button.setText("Tentar Novamente")
        self.push_button.clicked.connect(self.notebook_data)
        self.push_button.show()
         
        QtCore.QMetaObject.connectSlotsByName(self)
    else:
        self.setObjectName("Notebooks")
        self.setWindowTitle("Notebooks")
        self.setFixedSize(1200, 550)
        self.center_on_screen()

        self.table_view = QtWidgets.QTableView(self)
        self.table_view.setGeometry(QtCore.QRect(140, 40, 1040, 500))
        self.table_view.setObjectName("tableView")
        self.model = PandasModel(self.dataframe)
        self.table_view.setModel(self.model)
        self.delegate = ComboBoxDelegate(["Estoque", "Manutenção" , "Em Uso"])
        self.table_view.setItemDelegateForColumn(9, self.delegate)
        self.table_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_view.resizeColumnsToContents()
        self.table_view.setColumnWidth(9, 100)
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.table_view.show()

        self.push_button = QtWidgets.QPushButton(self)
        self.push_button.setGeometry(QtCore.QRect(10, 500, 120, 20))
        self.push_button.setObjectName("pushButton_1")
        self.push_button.setStyleSheet("background-color: purple;border-style: outset;border-color: beige;")
        self.push_button.setText("Smartphones")
        self.push_button.clicked.connect(self.smartphone_data)
        self.push_button.show()

        self.push_button2 = QtWidgets.QPushButton(self)
        self.push_button2.setGeometry(QtCore.QRect(10, 300, 120, 20))
        self.push_button2.setObjectName("pushButton_2")
        self.push_button2.setText("Cadastrar Notebook")
        self.push_button2.clicked.connect(lambda: add_notebook(self))
        self.push_button2.show()

        self.del_or_borrow_id = QtWidgets.QLineEdit(self)
        self.del_or_borrow_id.setGeometry(QtCore.QRect(10, 10, 200, 20))
        self.del_or_borrow_id.setObjectName("Texto Deleção/Empréstimo")
        self.del_or_borrow_id.setStyleSheet("background-color: lightblue;border-style: outset;border-color: beige;")
        self.del_or_borrow_id.setPlaceholderText("Insira ID do dispositivo")
        self.del_or_borrow_id.show()

        self.push_button3 = QtWidgets.QPushButton(self)
        self.push_button3.setGeometry(QtCore.QRect(220, 10, 120, 20))
        self.push_button3.setObjectName("pushButton_3")
        self.push_button3.setStyleSheet("background-color: red;border-style: outset;border-color: beige;")
        self.push_button3.setText("Deletar Notebook")
        self.push_button3.clicked.connect(lambda: delete_notebook(self,self.del_or_borrow_id.text()))
        self.push_button3.show()

        self.push_button4 = QtWidgets.QPushButton(self)
        self.push_button4.setGeometry(QtCore.QRect(10, 400, 120, 20))
        self.push_button4.setObjectName("pushButton_4")
        self.push_button4.setText("Baixar PDF")
        self.push_button4.clicked.connect(lambda: save_as_pdf(self))
        self.push_button4.show()

        self.push_button5 = QtWidgets.QPushButton(self)
        self.push_button5.setGeometry(QtCore.QRect(10, 200, 120, 20))
        self.push_button5.setObjectName("pushButton_5")
        self.push_button5.setText("Empréstimo Office")
        self.push_button5.clicked.connect(lambda: self.office_loan())
        self.push_button5.show()

        self.push_button6 = QtWidgets.QPushButton(self)
        self.push_button6.setGeometry(QtCore.QRect(10, 40, 120, 20))
        self.push_button6.setObjectName("pushButton_6")
        self.push_button6.setText("Emprestar Notebook")
        self.push_button6.setStyleSheet("background-color: green;border-style: outset;border-color: beige;")
        self.push_button6.clicked.connect(lambda: borrow_notebook(self,self.del_or_borrow_id.text()))
        self.push_button6.show()

        self.label_0 = QtWidgets.QLabel(self)
        self.label_0.setGeometry(QtCore.QRect(370, 10, 100, 20))
        self.label_0.setObjectName("label")
        self.label_0.setText("Filtros da Tabela:")
        self.label_0.show()

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(480, 10, 50, 20))
        self.label.setObjectName("label")
        self.label.setText("Marca")
        self.label.show()

        self.combo_box = QtWidgets.QComboBox(self)
        self.combo_box.setGeometry(QtCore.QRect(540, 10, 90, 20))
        self.combo_box.setObjectName("comboBox")
        self.combo_box.addItem("Tudo")
        for i in self.dataframe.Marca.unique():
            self.combo_box.addItem(i)
        self.combo_box.show()

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(660, 10, 50, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Modelo")
        self.label_2.show()

        self.combo_box_2 = QtWidgets.QComboBox(self)
        self.combo_box_2.setGeometry(QtCore.QRect(720, 10, 90, 20))
        self.combo_box_2.setObjectName("comboBox_2")
        self.combo_box_2.addItem("Tudo")
        for i in self.dataframe.Modelo.unique():
            self.combo_box_2.addItem(i)
        self.combo_box_2.show()

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(840, 10, 50, 20))
        self.label_3.setObjectName("label_2")
        self.label_3.setText("Status")
        self.label_3.show()

        self.combo_box_3 = QtWidgets.QComboBox(self)
        self.combo_box_3.setGeometry(QtCore.QRect(900, 10, 90, 20))
        self.combo_box_3.setObjectName("comboBox_2")
        self.combo_box_3.addItem("Tudo")
        self.combo_box_3.addItem("Estoque")
        self.combo_box_3.addItem("Manutenção")
        self.combo_box_3.addItem("Em Uso")
        self.combo_box_3.show()

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(1020, 10, 60, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Emprestado")
        self.label_4.show()

        self.combo_box_4 = QtWidgets.QComboBox(self)
        self.combo_box_4.setGeometry(QtCore.QRect(1090, 10, 90, 20))
        self.combo_box_4.setObjectName("comboBox_4")
        self.combo_box_4.addItem("Tudo")
        for i in self.dataframe.Emprestado.unique():
            self.combo_box_4.addItem(i)
        self.combo_box_4.show()

        QtCore.QMetaObject.connectSlotsByName(self)

        self.combo_box.currentTextChanged.connect(lambda: filter(self))
        self.combo_box_2.currentTextChanged.connect(lambda: filter(self))
        self.combo_box_3.currentTextChanged.connect(lambda: filter(self))
        self.combo_box_4.currentTextChanged.connect(lambda: filter(self))
        self.model.dataChanged.connect(lambda topLeft, bottomRight, roles: updated_notebook(self,self.model.headerData(topLeft.column(), Qt.Horizontal, Qt.DisplayRole),self.model.data(topLeft, Qt.DisplayRole),self.model.data(self.model.index(topLeft.row(), 6,parent=QModelIndex()),Qt.DisplayRole),self.dataframe2.loc[topLeft.row(),'_Status']))

def stock_control_smartphones(self):

    self.dataframe = connector.smartphone_stock(self.logged_email)
    if isinstance(self.dataframe,int):
        self.w = UserLogin.MissingConnection()
        self.w.show()
        
        self.setObjectName("Sem conexão")
        self.setWindowTitle("Sem conexão")
        self.setFixedSize(320, 100)
        self.center_on_screen()

        self.nome_label = QtWidgets.QLabel(self)
        self.nome_label.setGeometry(QtCore.QRect(10, 5, 300, 50))
        self.nome_label.setText("                       Sem acesso ao banco de dados.")
        self.nome_label.show()

        self.push_button = QtWidgets.QPushButton(self)
        self.push_button.setGeometry(QtCore.QRect(10, 50, 300, 40))
        self.push_button.setObjectName("pushButton")
        self.push_button.setText("Tentar Novamente")
        self.push_button.clicked.connect(self.smartphone_data)
        self.push_button.show()
         
        QtCore.QMetaObject.connectSlotsByName(self) 
    else:
        self.setObjectName("Smartphones")
        self.setWindowTitle("Smartphones")
        self.setFixedSize(1200, 550)
        self.center_on_screen()

        self.table_view = QtWidgets.QTableView(self)
        self.table_view.setGeometry(QtCore.QRect(140, 40, 1040, 500))
        self.table_view.setObjectName("tableView")
        self.model = PandasModel(self.dataframe)
        self.table_view.setModel(self.model)
        self.delegate = ComboBoxDelegate(["Estoque", "Manutenção" , "Em Uso"])
        self.table_view.setItemDelegateForColumn(6, self.delegate)
        self.delegate2 = ComboBoxDelegate(["Sim","Não"])
        self.table_view.setItemDelegateForColumn(7, self.delegate2)
        self.delegate3 = ComboBoxDelegate(["Sim","Não"])
        self.table_view.setItemDelegateForColumn(8, self.delegate3)
        self.table_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_view.resizeColumnsToContents()
        self.table_view.setColumnWidth(6, 100)
        self.table_view.setColumnWidth(7, 100)
        self.table_view.setColumnWidth(8, 100)
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.table_view.show()

        self.push_button = QtWidgets.QPushButton(self)
        self.push_button.setGeometry(QtCore.QRect(10, 500, 120, 20))
        self.push_button.setObjectName("pushButton_1")
        self.push_button.setStyleSheet("background-color: purple;border-style: outset;border-color: beige;")
        self.push_button.setText("Notebooks")
        self.push_button.clicked.connect(self.notebook_data)
        self.push_button.show()

        self.push_button2 = QtWidgets.QPushButton(self)
        self.push_button2.setGeometry(QtCore.QRect(10, 300, 120, 20))
        self.push_button2.setObjectName("pushButton_2")
        self.push_button2.setText("Cadastrar Smartphone")
        self.push_button2.clicked.connect(lambda: add_smartphone(self))
        self.push_button2.show()

        self.del_or_borrow_serial = QtWidgets.QLineEdit(self)
        self.del_or_borrow_serial.setGeometry(QtCore.QRect(10, 10, 200, 20))
        self.del_or_borrow_serial.setObjectName("Texto Deleção/Empréstimo")
        self.del_or_borrow_serial.setStyleSheet("background-color: lightblue;border-style: outset;border-color: beige;")
        self.del_or_borrow_serial.setPlaceholderText("Insira nº de série do dispositivo")
        self.del_or_borrow_serial.show()

        self.push_button3 = QtWidgets.QPushButton(self)
        self.push_button3.setGeometry(QtCore.QRect(220, 10, 120, 20))
        self.push_button3.setObjectName("pushButton_3")
        self.push_button3.setText("Deletar Smartphone")
        self.push_button3.setStyleSheet("background-color: red;border-style: outset;border-color: beige;")
        self.push_button3.clicked.connect(lambda: delete_smartphone(self,self.del_or_borrow_serial.text()))
        self.push_button3.show()

        self.push_button4 = QtWidgets.QPushButton(self)
        self.push_button4.setGeometry(QtCore.QRect(10, 400, 120, 20))
        self.push_button4.setObjectName("pushButton_4")
        self.push_button4.setText("Baixar PDF")
        self.push_button4.clicked.connect(lambda: save_as_pdf(self))
        self.push_button4.show()

        self.push_button5 = QtWidgets.QPushButton(self)
        self.push_button5.setGeometry(QtCore.QRect(10, 200, 120, 20))
        self.push_button5.setObjectName("pushButton_5")
        self.push_button5.setText("Empréstimo Office")
        self.push_button5.clicked.connect(lambda: self.office_loan())
        self.push_button5.show()

        self.push_button6 = QtWidgets.QPushButton(self)
        self.push_button6.setGeometry(QtCore.QRect(10, 40, 120, 20))
        self.push_button6.setObjectName("pushButton_6")
        self.push_button6.setText("Emprestar Smartphone")
        self.push_button6.setStyleSheet("background-color: green;border-style: outset;border-color: beige;")
        self.push_button6.clicked.connect(lambda: borrow_smartphone(self,self.del_or_borrow_serial.text()))
        self.push_button6.show()

        self.label_0 = QtWidgets.QLabel(self)
        self.label_0.setGeometry(QtCore.QRect(370, 10, 100, 20))
        self.label_0.setObjectName("label")
        self.label_0.setText("Filtros da Tabela:")
        self.label_0.show()

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(480, 10, 50, 20))
        self.label.setObjectName("label")
        self.label.setText("Marca")
        self.label.show()

        self.combo_box = QtWidgets.QComboBox(self)
        self.combo_box.setGeometry(QtCore.QRect(540, 10, 90, 20))
        self.combo_box.setObjectName("comboBox")
        self.combo_box.addItem("Tudo")
        for i in self.dataframe.Marca.unique():
            self.combo_box.addItem(i)
        self.combo_box.show()

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(660, 10, 50, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Modelo")
        self.label_2.show()

        self.combo_box_2 = QtWidgets.QComboBox(self)
        self.combo_box_2.setGeometry(QtCore.QRect(720, 10, 90, 20))
        self.combo_box_2.setObjectName("comboBox_2")
        self.combo_box_2.addItem("Tudo")
        for i in self.dataframe.Modelo.unique():
            self.combo_box_2.addItem(i)
        self.combo_box_2.show()

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(840, 10, 50, 20))
        self.label_3.setObjectName("label_2")
        self.label_3.setText("Status")
        self.label_3.show()

        self.combo_box_3 = QtWidgets.QComboBox(self)
        self.combo_box_3.setGeometry(QtCore.QRect(900, 10, 90, 20))
        self.combo_box_3.setObjectName("comboBox_2")
        self.combo_box_3.addItem("Tudo")
        self.combo_box_3.addItem("Estoque")
        self.combo_box_3.addItem("Manutenção")
        self.combo_box_3.addItem("Em Uso")
        self.combo_box_3.show()

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(1020, 10, 60, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Emprestado")
        self.label_4.show()

        self.combo_box_4 = QtWidgets.QComboBox(self)
        self.combo_box_4.setGeometry(QtCore.QRect(1090, 10, 90, 20))
        self.combo_box_4.setObjectName("comboBox_4")
        self.combo_box_4.addItem("Tudo")
        for i in self.dataframe.Emprestado.unique():
            self.combo_box_4.addItem(i)
        self.combo_box_4.show()

        QtCore.QMetaObject.connectSlotsByName(self)

        self.combo_box.currentTextChanged.connect(lambda: filter(self))
        self.combo_box_2.currentTextChanged.connect(lambda: filter(self))
        self.combo_box_3.currentTextChanged.connect(lambda: filter(self))
        self.combo_box_4.currentTextChanged.connect(lambda: filter(self))
        self.model.dataChanged.connect(lambda topLeft, bottomRight, roles: updated_smartphone(self,self.model.headerData(topLeft.column(), Qt.Horizontal, Qt.DisplayRole),self.model.data(topLeft, Qt.DisplayRole),self.model.data(self.model.index(topLeft.row(), 2,parent=QModelIndex()),Qt.DisplayRole),self.dataframe2.loc[topLeft.row(),'_Status']))

def filter(self):  # PEP8: `lower_case_name` for functions

    if self.combo_box.currentText() != "Tudo":
        self.dataframe = self.dataframe.loc[self.dataframe.Marca == self.combo_box.currentText()] 
    if self.combo_box_2.currentText() != "Tudo":
        self.dataframe = self.dataframe.loc[self.dataframe.Modelo == self.combo_box_2.currentText()] 
    if self.combo_box_3.currentText() != "Tudo":
        self.dataframe = self.dataframe.loc[self.dataframe._Status == self.combo_box_3.currentText()]  
    if self.combo_box_4.currentText() != "Tudo":
        self.dataframe = self.dataframe.loc[self.dataframe.Emprestado == self.combo_box_4.currentText()]  
    self.dataframe2 = self.dataframe.copy()
    self.model = PandasModel(self.dataframe)
    self.table_view.setModel(self.model)
    if self.windowTitle()=="Notebooks":
        self.model.dataChanged.connect(lambda topLeft, bottomRight, roles: updated_notebook(self,self.model.headerData(topLeft.column(), Qt.Horizontal, Qt.DisplayRole),self.model.data(topLeft, Qt.DisplayRole),self.model.data(self.model.index(topLeft.row(), 6 ,parent=QModelIndex()),Qt.DisplayRole),self.dataframe2.loc[topLeft.row(),'_Status']))
    else:
        self.model.dataChanged.connect(lambda topLeft, bottomRight, roles: updated_smartphone(self,self.model.headerData(topLeft.column(), Qt.Horizontal, Qt.DisplayRole),self.model.data(topLeft, Qt.DisplayRole),self.model.data(self.model.index(topLeft.row(), 2 ,parent=QModelIndex()),Qt.DisplayRole),self.dataframe2.loc[topLeft.row(),'_Status']))

def updated_notebook(self,column_name,column_value,id_value,was_maintenance):

    was_maintenance = was_maintenance=='Manutenção'
    if(connector.update_notebook(column_name,column_value,id_value,self.logged_email,was_maintenance))==1:
        self.dataframe = connector.notebook_stock(self.logged_email)
        filter(self)
    else:
        self.model = PandasModel(self.dataframe)
        self.table_view.setModel(self.model)
        self.model.dataChanged.connect(lambda topLeft, bottomRight, roles: updated_notebook(self,self.model.headerData(topLeft.column(), Qt.Horizontal, Qt.DisplayRole),self.model.data(topLeft, Qt.DisplayRole),self.model.data(self.model.index(topLeft.row(), 6 ,parent=QModelIndex()),Qt.DisplayRole),self.dataframe2.loc[topLeft.row(),'_Status']))
        self.w = UserLogin.MissingConnection()
        self.w.show()

def updated_smartphone(self,column_name,column_value,serial_number,was_maintenance):

    was_maintenance = was_maintenance=='Manutenção'
    if(connector.update_smartphone(column_name,column_value,serial_number,self.logged_email,was_maintenance))==1:
        self.dataframe = connector.smartphone_stock(self.logged_email)
        filter(self)
    else:
        self.model = PandasModel(self.dataframe)
        self.table_view.setModel(self.model)
        self.model.dataChanged.connect(lambda topLeft, bottomRight, roles: updated_smartphone(self,self.model.headerData(topLeft.column(), Qt.Horizontal, Qt.DisplayRole),self.model.data(topLeft, Qt.DisplayRole),self.model.data(self.model.index(topLeft.row(), 2 ,parent=QModelIndex()),Qt.DisplayRole),self.dataframe2.loc[topLeft.row(),'_Status']))
        self.w = UserLogin.MissingConnection()
        self.w.show()

def add_notebook(self):
    self.w = AddNotebook(self)
    self.w.show()

def add_smartphone(self):
    self.w = AddSmartphone(self)
    self.w.show()

def unique_used(self,column):
    self.w = UniqueUsed(column)
    self.w.show()

def delete_notebook(self,id_dispositivo):
    if id_dispositivo == '':
        return
    self.del_or_borrow_id.clear()
    success = connector.delete_notebook(id_dispositivo)
    if(success)==1:
        self.dataframe = connector.notebook_stock(self.logged_email)
        self.model = PandasModel(self.dataframe)
        filter(self)
        self.w = NotebookDeleted()
        self.w.show()
    elif success == 0:
        self.w = InvalidNotebookID()
        self.w.show()
    else:
        self.w = UserLogin.MissingConnection()
        self.w.show()

def delete_smartphone(self,numero_serie):
    if numero_serie == '':
        return
    self.del_or_borrow_serial.clear()
    success = connector.delete_smartphone(numero_serie)
    if(success)==1:
        self.dataframe = connector.smartphone_stock(self.logged_email)
        self.model = PandasModel(self.dataframe)
        filter(self)
        self.w = SmartphoneDeleted()
        self.w.show()
    elif success == 0:
        self.w = InvalidSmartphoneSerialNumber()
        self.w.show()
    else:
        self.w = UserLogin.MissingConnection()
        self.w.show()

def save_as_pdf(self):
    # Convert DataFrame to HTML
    html = self.dataframe.to_html()

    # Save HTML as PDF
    pdfkit.from_string(html, f"{self.windowTitle()}.pdf")

    self.w = PDFDownloaded()
    self.w.show()

def borrow_notebook(self,id_dispositivo):
    if id_dispositivo == '':
        return
    self.del_or_borrow_id.clear()
    dataframe_with_id = self.dataframe.loc[(self.dataframe['Id_dispositivo']==id_dispositivo)]
    if dataframe_with_id.empty:
        self.w = InvalidNotebookID()
        self.w.show()
    elif dataframe_with_id.loc[(dataframe_with_id['Emprestado']=='Não')].empty or not dataframe_with_id.loc[(dataframe_with_id['_Status']=='Em Uso')].empty:
        self.w = NotebookAlreadyBorrowed()
        self.w.show()
    elif not dataframe_with_id.loc[(dataframe_with_id['_Status']=='Manutenção')].empty:
        self.w = NotebookInMaintenance()
        self.w.show()
    else:
        if connector.borrow_notebook(self.logged_email,id_dispositivo)==1:
            self.dataframe = connector.notebook_stock(self.logged_email)
            self.model = PandasModel(self.dataframe)
            filter(self)
            self.w = NotebookBorrowed()
            self.w.show()
        else:
            self.w = UserLogin.MissingConnection()
            self.w.show()

def borrow_smartphone(self,numero_serie):
    if numero_serie == '':
        return
    self.del_or_borrow_serial.clear()
    dataframe_with_id = self.dataframe.loc[(self.dataframe['Numero_serie']==numero_serie)]
    if dataframe_with_id.empty:
        self.w = InvalidSmartphoneSerialNumber()
        self.w.show()
    elif dataframe_with_id.loc[(dataframe_with_id['Emprestado']=='Não')].empty or not dataframe_with_id.loc[(dataframe_with_id['_Status']=='Em Uso')].empty:
        self.w = SmartphoneAlreadyBorrowed()
        self.w.show()
    elif not dataframe_with_id.loc[(dataframe_with_id['_Status']=='Manutenção')].empty:
        self.w = SmartphoneInMaintenance()
        self.w.show()
    else:
        if connector.borrow_smartphone(self.logged_email,numero_serie)==1:
            self.dataframe = connector.smartphone_stock(self.logged_email)
            self.model = PandasModel(self.dataframe)
            filter(self)
            self.w = SmartphoneBorrowed()
            self.w.show()
        else:
            self.w = UserLogin.MissingConnection()
            self.w.show()

class InvalidNotebookID(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("ID inválido")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel("                Não existe um notebook com esse ID.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)   

class InvalidSmartphoneSerialNumber(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Número de série inválido")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel("   Não existe um smartphone com esse número de série.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)   

class UniqueUsed(QtWidgets.QDialog):
    def __init__(self,column):
        
        super().__init__()
        self.setWindowTitle("Dado Único")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(330, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel(f"O dado {column} é único. O valor escolhido já está em uso.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)   

class NotebookAlreadyBorrowed(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Notebook já emprestado")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel("           O notebook com esse ID já está emprestado.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)   

class SmartphoneAlreadyBorrowed(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Smartphone já emprestado")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(330, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel("O smartphone com esse número de série já está emprestado.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)   

class NotebookInMaintenance(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Notebook em manutenção")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel("           O notebook com esse ID está em manutenção.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)   

class SmartphoneInMaintenance(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Smartphone em manutenção")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(330, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel("O smartphone com esse número de série está em manutenção.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout) 

class PDFDownloaded(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("PDF baixado")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(380, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel("O PDF foi gerado com sucesso. Está na mesma pasta que este aplicativo.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)   

class NotebookDeleted(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Notebook Deletado")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel("               O notebook foi deletado com sucesso.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)  

class SmartphoneDeleted(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Smartphone Deletado")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel("               O smartphone foi deletado com sucesso.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)  

class NotebookBorrowed(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Notebook Emprestado")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel("               O notebook foi emprestado com sucesso.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)  

class SmartphoneBorrowed(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Smartphone Emprestado")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)
        self.setModal(True)

        self.nome_label = QtWidgets.QLabel("               O smartphone foi emprestado com sucesso.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)  

class ComboBoxDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.items = items  # The options for the dropdown

    def createEditor(self, parent, option, index):
        # Create a QComboBox as the editor
        combo_box = QtWidgets.QComboBox(parent)
        combo_box.addItems(self.items)
        return combo_box

    def setEditorData(self, editor, index):
        # Set the current value of the editor (dropdown)
        current_text = index.model().data(index, Qt.EditRole)
        current_index = editor.findText(current_text)
        if current_index >= 0:
            editor.setCurrentIndex(current_index)

    def setModelData(self, editor, model, index):
        # Update the model with the selected value
        model.setData(index, editor.currentText(), Qt.EditRole) 

class AddNotebook(QtWidgets.QDialog):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self,parent=None):
        
        self.parent = parent
        super().__init__()
        self.setWindowTitle("Janela de Adição de Notebook")
        layout = QtWidgets.QGridLayout()
        self.setModal(True)
        
        self.marca_label = QtWidgets.QLabel("Marca")
        layout.addWidget(self.marca_label,0,0)
        
        self.marca = QtWidgets.QLineEdit()
        self.marca.setObjectName("Marca")
        layout.addWidget(self.marca,0,1,1,20)

        self.modelo_label = QtWidgets.QLabel("Modelo")
        layout.addWidget(self.modelo_label,1,0)
        
        self.modelo = QtWidgets.QLineEdit()
        self.modelo.setObjectName("Modelo")
        layout.addWidget(self.modelo,1,1,1,20)

        self.processador_label = QtWidgets.QLabel("Processador")
        layout.addWidget(self.processador_label,2,0)
        
        self.processador = QtWidgets.QLineEdit()
        self.processador.setObjectName("Processador")
        layout.addWidget(self.processador,2,1,1,20)

        self.memoria_ram_label = QtWidgets.QLabel("Memoria Ram")
        layout.addWidget(self.memoria_ram_label,3,0)
        
        self.memoria_ram = QtWidgets.QLineEdit()
        self.memoria_ram.setObjectName("Memoria Ram")
        layout.addWidget(self.memoria_ram,3,1,1,20)

        self.sistema_operacional_label = QtWidgets.QLabel("Sistema Operacional")
        layout.addWidget(self.sistema_operacional_label,4,0)
        
        self.sistema_operacional = QtWidgets.QLineEdit()
        self.sistema_operacional.setObjectName("Sistema Operacional")
        layout.addWidget(self.sistema_operacional,4,1,1,20)

        self.memoria_interna_label = QtWidgets.QLabel("Memoria Interna")
        layout.addWidget(self.memoria_interna_label,5,0)
        
        self.memoria_interna = QtWidgets.QLineEdit()
        self.memoria_interna.setObjectName("Memoria Interna")
        layout.addWidget(self.memoria_interna,5,1,1,20)

        self.id_dispositivo_label = QtWidgets.QLabel("ID Dispositivo")
        layout.addWidget(self.id_dispositivo_label,6,0)
        
        self.id_dispositivo = QtWidgets.QLineEdit()
        self.id_dispositivo.setObjectName("ID Dispositivo")
        layout.addWidget(self.id_dispositivo,6,1,1,20)

        self.id_produto_label = QtWidgets.QLabel("ID Produto")
        layout.addWidget(self.id_produto_label,7,0)
        
        self.id_produto = QtWidgets.QLineEdit()
        self.id_produto.setObjectName("ID Produto")
        layout.addWidget(self.id_produto,7,1,1,20)

        self.serial_number_label = QtWidgets.QLabel("Serial Number")
        layout.addWidget(self.serial_number_label,8,0)
        
        self.serial_number = QtWidgets.QLineEdit()
        self.serial_number.setObjectName("Serial Number")
        layout.addWidget(self.serial_number,8,1,1,20)

        self.status_label = QtWidgets.QLabel("Status")
        layout.addWidget(self.status_label,9,0)
        
        self.status = QtWidgets.QComboBox()
        self.status.setObjectName("Status")
        self.status.addItem("Estoque")
        self.status.addItem("Manutenção")
        self.status.addItem("Em Uso")
        layout.addWidget(self.status,9,1,1,3)

        self.observacoes_label = QtWidgets.QLabel("Observações")
        layout.addWidget(self.observacoes_label,10,0)
        
        self.observacoes = QtWidgets.QLineEdit()
        self.observacoes.setObjectName("Observações")
        layout.addWidget(self.observacoes,10,1,1,20)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Adicionar Notebook")
        self.pushButton.clicked.connect(self.add_entry)

        layout.addWidget(self.pushButton,11,3)

        self.setLayout(layout)
        self.adjustSize()
    
    def add_entry(self):

        marca = self.marca.text()
        modelo = self.modelo.text()
        processador = self.processador.text()
        memoria_ram = self.memoria_ram.text()
        sistema_operacional = self.sistema_operacional.text()
        memoria_interna = self.memoria_interna.text()
        id_dispositivo = self.id_dispositivo.text()
        id_produto = self.id_produto.text()
        serial_number = self.serial_number.text()
        status = self.status.currentText()
        observacoes = self.observacoes.text()
        
        if (len(marca)==0 or len(modelo)==0 or len(processador)==0 or len(memoria_ram)==0 or len(sistema_operacional)==0 or len(memoria_interna)==0 or len(id_dispositivo)==0 or len(id_produto)==0 or len(serial_number)==0):
            self.w = InvalidWindow()
            self.w.show()
        elif self.parent.dataframe['Id_dispositivo'].str.contains(id_dispositivo).any():
            unique_used(self,'Id_dispositivo')
        elif self.parent.dataframe['Serial_number'].str.contains(serial_number).any():
            unique_used(self,'Serial_number')
        else:
            self.added_notebook(marca,modelo,processador,memoria_ram,sistema_operacional,memoria_interna,id_dispositivo,id_produto,serial_number,status,observacoes)

    def added_notebook(self,marca,modelo,processador,memoria_ram,sistema_operacional,memoria_interna,id_dispositivo,id_produto,serial_number,status,observacoes):

        if(connector.add_notebook(marca,modelo,processador,memoria_ram,sistema_operacional,memoria_interna,id_dispositivo,id_produto,serial_number,status,observacoes,self.parent.logged_email))==1:
            self.parent.dataframe = connector.notebook_stock(self.parent.logged_email)
            self.parent.model = PandasModel(self.parent.dataframe)
            filter(self.parent)
            self.close()
        else:
            self.parent.model = PandasModel(self.parent.dataframe)
            self.w = UserLogin.MissingConnection()
            self.w.show()

class AddSmartphone(QtWidgets.QDialog):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self,parent=None):
        
        self.parent = parent
        super().__init__()
        self.setWindowTitle("Janela de Adição de Smartphone")
        layout = QtWidgets.QGridLayout()
        self.setModal(True)
        
        self.marca_label = QtWidgets.QLabel("Marca")
        layout.addWidget(self.marca_label,0,0)
        
        self.marca = QtWidgets.QLineEdit()
        self.marca.setObjectName("Marca")
        layout.addWidget(self.marca,0,1,1,20)

        self.modelo_label = QtWidgets.QLabel("Modelo")
        layout.addWidget(self.modelo_label,1,0)
        
        self.modelo = QtWidgets.QLineEdit()
        self.modelo.setObjectName("Modelo")
        layout.addWidget(self.modelo,1,1,1,20)

        self.numero_serie_label = QtWidgets.QLabel("Número Série")
        layout.addWidget(self.numero_serie_label,2,0)
        
        self.numero_serie = QtWidgets.QLineEdit()
        self.numero_serie.setObjectName("Número Série")
        layout.addWidget(self.numero_serie,2,1,1,20)

        self.numero_chip_label = QtWidgets.QLabel("Número Chip")
        layout.addWidget(self.numero_chip_label,3,0)
        
        self.numero_chip = QtWidgets.QLineEdit()
        self.numero_chip.setObjectName("Número Chip")
        layout.addWidget(self.numero_chip,3,1,1,20)

        self.imei_1_label = QtWidgets.QLabel("Imei 1")
        layout.addWidget(self.imei_1_label,4,0)
        
        self.imei_1 = QtWidgets.QLineEdit()
        self.imei_1.setObjectName("Imei 1")
        layout.addWidget(self.imei_1,4,1,1,20)

        self.imei_2_label = QtWidgets.QLabel("Imei 2")
        layout.addWidget(self.imei_2_label,5,0)
        
        self.imei_2 = QtWidgets.QLineEdit()
        self.imei_2.setObjectName("Imei 2")
        layout.addWidget(self.imei_2,5,1,1,20)

        self.status_label = QtWidgets.QLabel("Status")
        layout.addWidget(self.status_label,6,0)
        
        self.status = QtWidgets.QComboBox()
        self.status.setObjectName("Status")
        self.status.addItem("Estoque")
        self.status.addItem("Manutenção")
        self.status.addItem("Em Uso")
        layout.addWidget(self.status,6,1,1,3)

        self.capa_protetora_label = QtWidgets.QLabel("Capa Protetora")
        layout.addWidget(self.capa_protetora_label,7,0)
        
        self.capa_protetora = QtWidgets.QComboBox()
        self.capa_protetora.setObjectName("Capa Protetora")
        self.capa_protetora.addItem("Sim")
        self.capa_protetora.addItem("Não")
        layout.addWidget(self.capa_protetora,7,1,1,3)

        self.carregador_label = QtWidgets.QLabel("Carregador")
        layout.addWidget(self.carregador_label,8,0)
        
        self.carregador = QtWidgets.QComboBox()
        self.carregador.setObjectName("Carregador")
        self.carregador.addItem("Sim")
        self.carregador.addItem("Não")
        layout.addWidget(self.carregador,8,1,1,3)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Adicionar Notebook")
        self.pushButton.clicked.connect(self.add_entry)

        layout.addWidget(self.pushButton,9,3)

        self.setLayout(layout)
        self.adjustSize()
    
    def add_entry(self):

        marca = self.marca.text()
        modelo = self.modelo.text()
        numero_serie = self.numero_serie.text()
        numero_chip = self.numero_chip.text()
        imei_1 = self.imei_1.text()
        imei_2 = self.imei_2.text()
        status = self.status.currentText()
        if self.capa_protetora.currentText() == "Sim":
            capa_protetora = 1
        else:
            capa_protetora = 0
        if self.carregador.currentText() == "Sim":
            carregador = 1
        else:
            carregador = 0
        if (len(marca)==0 or len(modelo)==0 or len(numero_serie)==0 or len(imei_1)==0):
            self.w = InvalidWindow()
            self.w.show()
        elif self.parent.dataframe['Numero_serie'].str.contains(numero_serie).any():
            unique_used(self,'Id_dispositivo')
        elif self.parent.dataframe['Imei_1'].str.contains(imei_1).any():
            unique_used(self,'Serial_number')
        else:
            self.added_smartphone(marca,modelo,numero_serie,numero_chip,imei_1,imei_2,status,capa_protetora,carregador)

    def added_smartphone(self,marca,modelo,numero_serie,numero_chip,imei_1,imei_2,status,capa_protetora,carregador):

        if(connector.add_smartphone(marca,modelo,numero_serie,numero_chip,imei_1,imei_2,status,capa_protetora,carregador,self.parent.logged_email))==1:
            self.parent.dataframe = connector.smartphone_stock(self.parent.logged_email)
            self.parent.model = PandasModel(self.parent.dataframe)
            filter(self.parent)
            self.close()
        else:
            self.parent.model = PandasModel(self.parent.dataframe)
            self.w = UserLogin.MissingConnection()
            self.w.show()

class InvalidWindow(QtWidgets.QDialog):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Entrada Inválida")
        self.setModal(True)
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(210, 100)

        self.nome_label = QtWidgets.QLabel("   Um dos parâmetros está faltando.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)  

class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """

    def __init__(self, dataframe: pd.DataFrame, parent=None):
        super().__init__(parent)
        self._dataframe = dataframe

    def rowCount(self, parent=QModelIndex()) -> int:
        if parent == QModelIndex():
            return len(self._dataframe)
        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            return str(self._dataframe.iloc[index.row(), index.column()])
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._dataframe.columns[section])
            if orientation == Qt.Vertical:
                return str(self._dataframe.index[section])
        return None

    def setData(self, index: QModelIndex, value, role=Qt.ItemDataRole) -> bool:
        """Override method from QAbstractTableModel

        Update the DataFrame with the edited value
        """
        if role == Qt.ItemDataRole.EditRole:
            self._dataframe.iloc[index.row(), index.column()] = value
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole])
            return True
        return False

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:

        if not index.isValid():
            return Qt.NoItemFlags

        # Get column name for the current index
        column_name = self._dataframe.columns[index.column()]

        # Define the columns that are not editable
        non_editable_columns = ["Id_dispositivo", "Serial_number", "Numero_serie", "Imei_1", "Emprestado", "Ultimo_comeco_manutencao", "Ultimo_final_manutencao"]  # Replace with your column names

        if column_name in non_editable_columns:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled  # Remove Qt.ItemIsEditable

        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable