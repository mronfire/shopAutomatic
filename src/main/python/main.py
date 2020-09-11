from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDateEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, Qt, QCoreApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800,600)
        MainWindow.setWindowTitle("BookAutomatic")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.titleLabel = QLabel(self.centralwidget) #Title Label to display
        self.titleLabel.setGeometry(QRect(210, 60, 381, 41))
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.websiteInput = QLineEdit(self.centralwidget) #Website name input
        self.websiteInput.setGeometry(QRect(300, 170, 211, 31))
        self.websiteInput.setObjectName("websiteInput")

        font = QFont()
        font.setPointSize(10)
        self.websiteLabel = QLabel(self.centralwidget) #Website name label
        self.websiteLabel.setGeometry(QRect(240, 170, 51, 31))
        self.websiteLabel.setFont(font)
        self.websiteLabel.setAlignment(Qt.AlignCenter)
        self.websiteLabel.setObjectName("websiteLabel")

        self.searchButton = QPushButton(self.centralwidget) #Search button
        self.searchButton.setGeometry(QRect(360, 290, 91, 31))
        self.searchButton.setObjectName("searchButton")

        self.startDateEdit = QDateEdit(self.centralwidget) #Start date input
        self.startDateEdit.setGeometry(QRect(400, 210, 110, 22))
        self.startDateEdit.setObjectName("startDateEdit")
        self.endDateEdit = QDateEdit(self.centralwidget) #End date input
        self.endDateEdit.setGeometry(QRect(400, 240, 110, 22))
        self.endDateEdit.setObjectName("endDateEdit")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Welcome to BookAutomatic"))
        self.websiteLabel.setText(_translate("MainWindow", "Website:"))
        self.searchButton.setText(_translate("MainWindow", "SEARCH"))

    def dialog(self):
        mbox = QMessageBox()

        mbox.setText("Opening website for you...")
        mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        mbox.exec_()

if __name__ == "__main__":
    import sys
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)