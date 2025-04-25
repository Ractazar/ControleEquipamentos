import connector
import UserLogin
import StockControl
from PyQt5 import QtCore, QtWidgets
QAbstractTableModel = QtCore.QAbstractTableModel
Qt = QtCore.Qt
QModelIndex = QtCore.QModelIndex
pyqtSignal = QtCore.pyqtSignal
import pandas as pd
import datetime

class ControlOffice(QtWidgets.QDialog):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.sds
    """
    def __init__(self,parent=None):
        
        self.parent = parent
        super().__init__()
        self.setWindowTitle("Empréstimo Office")
        layout = QtWidgets.QGridLayout()
        self.setModal(True)

        email = self.parent.logged_email
        self.office = connector.check_office(email)
        if isinstance(self.office,int):
            self.w = UserLogin.MissingConnection(self)

        self.table_view2 = QtWidgets.QTableView(self)
        self.table_view2.setObjectName("tableView")
        self.model2 = PandasModel2(self.office)
        self.table_view2.setModel(self.model2)
        self.table_view2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_view2.resizeColumnsToContents()
        self.table_view2.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table_view2,0,0,1,5)
        
        self.senha_label = QtWidgets.QLabel("Senha")
        layout.addWidget(self.senha_label,1,0)
        
        self.senha = QtWidgets.QLineEdit()
        self.senha.setObjectName("Senha")
        layout.addWidget(self.senha,1,1,1,5)

        self.versao_label = QtWidgets.QLabel("Versao")
        layout.addWidget(self.versao_label,2,0)
        
        self.versao = QtWidgets.QLineEdit()
        self.versao.setObjectName("Versao")
        layout.addWidget(self.versao,2,1,1,5)

        self.date_label = QtWidgets.QLabel("Vencimento")
        layout.addWidget(self.date_label,3,0)

        # Add a QDateEdit widget
        self.date_edit = QtWidgets.QDateEdit(self)
        self.date_edit.setDisplayFormat("dd-MM-yyyy")  # Customize the date format
        self.date_edit.setCalendarPopup(True)  # Allows a calendar popup for easier selection
        self.date_edit.setDate(QtCore .QDate.currentDate().addDays(30))
        layout.addWidget(self.date_edit,3,2,1,3)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Emprestar Office")
        self.pushButton.clicked.connect(self.add_office)

        layout.addWidget(self.pushButton,4,3)

        self.setLayout(layout)
        self.adjustSize()

    def add_office(self):

        senha = self.senha.text()
        versao = self.versao.text()
        date_edit = datetime.datetime.strptime(self.date_edit.text(), "%d-%m-%Y")
        
        if (len(senha)==0 or len(versao)==0):
            self.w = StockControl.InvalidWindow()
            self.w.show()
        else:
            if self.office.empty:
                success = connector.add_office(self.parent.logged_email,senha,versao,date_edit)
                if success == 0:
                    self.office = connector.check_office(self.parent.logged_email)
                    self.model2 = StockControl.PandasModel(self.office)
                    self.table_view2.setModel(self.model2)
                else:
                    self.w = UserLogin.MissingConnection()
                    self.w.show()
            else:
                success = connector.update_office(self.parent.logged_email,senha,versao,date_edit)
                if success == 0:
                    self.office = connector.check_office(self.parent.logged_email)
                    self.model2 = StockControl.PandasModel(self.office)
                    self.table_view2.setModel(self.model2)
                else:
                    self.w = UserLogin.MissingConnection()
                    self.w.show()

class PandasModel2(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """

    def __init__(self, dataframe: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe

    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._dataframe.iloc[index.row(), index.column()])

        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._dataframe.columns[section])

            if orientation == Qt.Vertical:
                return str(self._dataframe.index[section])

        return None