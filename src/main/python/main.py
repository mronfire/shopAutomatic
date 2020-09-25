from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDateEdit, QMenuBar, QMenu, QStatusBar, QAction, QSizePolicy, QFormLayout, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, Qt, QCoreApplication, QMetaObject, QSize
from websites import amazon, ebay
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow) #Central window Widget
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(706, 474))
        self.centralwidget.setObjectName("centralwidget")

        self.formLayout = QFormLayout(self.centralwidget) #Form Layout
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(70, 70, 70, -1)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")

        self.titleLabel = QLabel(self.centralwidget) #Title Label to display
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.titleLabel)

        self.websiteSelect = QComboBox(self.centralwidget) #Website select input
        self.websiteSelect.addItem("Everywhere")
        self.websiteSelect.addItem("Amazon")
        self.websiteSelect.addItem("Ebay")
        self.websiteSelect.addItem("Craiglist")
        self.websiteSelect.setObjectName("websiteSelect")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.websiteSelect)

        self.itemInput = QLineEdit(self.centralwidget) #Item input
        self.itemInput.setObjectName("itemInput")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.itemInput)

        self.usernameInput = QLineEdit(self.centralwidget) #Username input
        self.usernameInput.setObjectName("usernameInput")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.usernameInput)

        self.passwordInput = QLineEdit(self.centralwidget) #Password input
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.passwordInput)

        font = QFont()
        font.setPointSize(11)
        self.websiteLabel = QLabel(self.centralwidget) #Website label
        self.websiteLabel.setFont(font)
        self.websiteLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.websiteLabel.setObjectName("websiteLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.websiteLabel)

        self.itemLabel = QLabel(self.centralwidget) #Item label
        self.itemLabel.setFont(font)
        self.itemLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.itemLabel.setObjectName("itemLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.itemLabel)

        self.usernameLabel = QLabel(self.centralwidget) #Username label
        self.usernameLabel.setFont(font)
        self.usernameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.usernameLabel)

        self.passwordLabel = QLabel(self.centralwidget) #Password label
        self.passwordLabel.setFont(font)
        self.passwordLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.passwordLabel)

        #TODO:
        # Provide the ability to have to login or not.
        # If user does not want to login, avoid the login and go straight to search

        self.searchButton = QPushButton(self.centralwidget) #Search button
        self.searchButton.setObjectName("searchButton")
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.searchButton)
        self.searchButton.clicked.connect(self.search)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow) #Menu bar widget for Contact
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.contactMenu = QMenu(self.menubar)
        self.contactMenu.setObjectName("contactMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionGitHub = QAction(MainWindow) #Action widget to direct to github page
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
        MainWindow.setWindowTitle(_translate("MainWindow", "ShopAutomatic"))
        self.titleLabel.setText(_translate("MainWindow", "Welcome to ShopAutomatic"))
        self.websiteLabel.setText(_translate("MainWindow", "Select site to search from:"))
        self.itemLabel.setText(_translate("MainWindow", "Item:"))
        self.usernameLabel.setText(_translate("MainWindow", "Username:"))
        self.passwordLabel.setText(_translate("MainWindow", "Password:"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.contactMenu.setTitle(_translate("MainWindow", "Contact Us"))
        self.actionGitHub.setText(_translate("MainWindow", "GitHub Page"))

    def contactPage(self):
        import webbrowser
        webbrowser.open("https://github.com/mronfire/bookAutomatic")

    def search(self):
        try:
            site = self.websiteSelect.currentText()
            s = None
            if site == "Amazon":
                s = amazon.SearchAmazon()
            elif site == "Ebay":
                s = ebay.SearchEbay()
            else:
                #TODO:
                # Need to implement a way to search for item in all websites
                # and just have it open tabs in same browser instead of opening
                # different drivers and browsers for each page
                s = None
            
            s.login()
            s.searchItem(self.itemInput.text())

        except Exception as e:
            s.closeDriver()
            print(e)

if __name__ == "__main__":
    import sys
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)