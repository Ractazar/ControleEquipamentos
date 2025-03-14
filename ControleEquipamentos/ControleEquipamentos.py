import connector
import sys
from PyQt5 import QtCore, QtWidgets
QAbstractTableModel = QtCore.QAbstractTableModel
Qt = QtCore.Qt
QModelIndex = QtCore.QModelIndex
pyqtSignal = QtCore.pyqtSignal
from sys import exit

UC = "Unable to connect to database"

class main_window(object):
    def setup_ui(self, dialog):

        dialog.setObjectName("Login")
        dialog.setWindowTitle("Login")
        dialog.setFixedSize(220, 180)

        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(50, 0, 50, 20))
        self.label.setObjectName("label")
        self.label.setText("Email")
     
        self.email = QtWidgets.QLineEdit(dialog)
        self.email.setGeometry(QtCore.QRect(50, 20, 120, 20))
        self.email.setObjectName("Email")

        self.label2 = QtWidgets.QLabel(dialog)
        self.label2.setGeometry(QtCore.QRect(50, 40, 50, 20))
        self.label2.setObjectName("label")
        self.label2.setText("Senha")

        self.senha = QtWidgets.QLineEdit(dialog)
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha.setGeometry(QtCore.QRect(50, 60, 120, 20))
        self.senha.setObjectName("Senha")

        self.push_button = QtWidgets.QPushButton(dialog)
        self.push_button.setGeometry(QtCore.QRect(50, 100, 120, 20))
        self.push_button.setObjectName("pushButton")
        self.push_button.setText("Login")
        self.push_button.clicked.connect(self.login)

        self.push_button2 = QtWidgets.QPushButton(dialog)
        self.push_button2.setGeometry(QtCore.QRect(50, 140, 120, 20))
        self.push_button2.setObjectName("pushButton")
        self.push_button2.setText("Criar Conta")
        self.push_button2.clicked.connect(self.create_user)

        QtCore.QMetaObject.connectSlotsByName(dialog)

    def login(self):
        email=self.email.text()
        senha=self.senha.text()
        if (len(email)==0 or len(senha)==0):
            self.w = MissingData()
            self.w.show()
        else:
            entrar = connector.check_user(email,senha)
            if entrar == 0:
                self.w = MissingUser()
                self.w.show()
            elif entrar == 2:
                self.w = MissingConnection()
                self.w.show()
            else:
                self.login()

    def create_user(self):
        self.w = CreateUser()
        self.w.show()
        self.w.open_signal.connect(self.login)
    
    def login(self):
        self.w = Login()
        self.w.show()
    
class Login(QtWidgets.QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Tela de Login")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)

        self.nome_label = QtWidgets.QLabel("                            Você está conectado.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)  

class MissingData(QtWidgets.QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Dados Faltando")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)

        self.nome_label = QtWidgets.QLabel("               Por favor, preencha todos os campos.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)   

class MissingUser(QtWidgets.QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Dados Incorretos")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)

        self.nome_label = QtWidgets.QLabel("                      E-mail ou senha incorretos.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout)   

class MissingConnection(QtWidgets.QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Falha na Conexão")
        layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(300, 100)

        self.nome_label = QtWidgets.QLabel("               Não foi possível conectar com o banco de dados.")
        layout.addWidget(self.nome_label)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.close)

        layout.addWidget(self.pushButton)

        self.setLayout(layout) 

class CreateUser(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    open_signal = pyqtSignal()

    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Criação de Conta")
        layout = QtWidgets.QGridLayout()

        self.name_label = QtWidgets.QLabel("Nome")
        layout.addWidget(self.name_label,0,0)
        
        self.name = QtWidgets.QLineEdit()
        self.name.setObjectName("Nome")
        layout.addWidget(self.name,0,1,1,25)

        self.email_label = QtWidgets.QLabel("Email")
        layout.addWidget(self.email_label,1,0)
        
        self.email = QtWidgets.QLineEdit()
        self.email.setObjectName("Email")
        layout.addWidget(self.email,1,1,1,25)

        self.password_label = QtWidgets.QLabel("Senha")
        layout.addWidget(self.password_label,2,0)
        
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("Senha")
        layout.addWidget(self.password,2,1,1,25)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Criar Conta")
        self.pushButton.clicked.connect(self.add_entry)

        layout.addWidget(self.pushButton,3,12)

        self.setLayout(layout)
    
    def add_entry(self):
        nome=self.name.text()
        email=self.email.text()
        senha=self.password.text()
        if (len(nome)==0 or len(email)==0 or len(senha)==0):
            self.w = MissingData()
            self.w.show()
        else:
            criar = connector.create_user(nome,email,senha)
            if criar == 0:
                self.w = MissingConnection()
                self.w.show()
            else:
                self.open_signal.emit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    _exit = exit
    Dialog.closeEvent = _exit
    ui = main_window()
    ui.setup_ui(Dialog)
    Dialog.show()

    sys.exit(app.exec_())
