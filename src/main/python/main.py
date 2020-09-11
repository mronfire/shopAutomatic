from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDateEdit, QMenuBar, QMenu, QStatusBar, QAction
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, Qt, QCoreApplication, QMetaObject

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800,600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.titleLabel = QLabel(self.centralwidget) #Title Label to display
        self.titleLabel.setGeometry(QRect(210, 60, 381, 41))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
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
        self.searchButton.clicked.connect(self.dialog)

        self.startDateEdit = QDateEdit(self.centralwidget) #Start date input
        self.startDateEdit.setGeometry(QRect(400, 210, 110, 22))
        self.startDateEdit.setObjectName("startDateEdit")
        self.endDateEdit = QDateEdit(self.centralwidget) #End date input
        self.endDateEdit.setGeometry(QRect(400, 240, 110, 22))
        self.endDateEdit.setObjectName("endDateEdit")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow) #Menu bar widget for Contact
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.contactMenu = QMenu(self.menubar)
        self.contactMenu.setObjectName("contactMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionGitHub = QAction(MainWindow)
        self.actionGitHub.setObjectName("actionGitHub")
        self.contactMenu.addAction(self.actionGitHub)
        self.menubar.addAction(self.contactMenu.menuAction())
        self.actionGitHub.triggered.connect(self.contactPage)

        self.statusbar = QStatusBar(MainWindow) #Status bar widget
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BookAutomatic"))
        self.titleLabel.setText(_translate("MainWindow", "Welcome to BookAutomatic"))
        self.websiteLabel.setText(_translate("MainWindow", "Website:"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.contactMenu.setTitle(_translate("MainWindow", "Contact"))
        self.actionGitHub.setText(_translate("MainWindow", "GitHub"))

    def contactPage(self):
        import webbrowser
        webbrowser.open("https://github.com/mronfire/bookAutomatic")

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