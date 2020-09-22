from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDateEdit, QMenuBar, QMenu, QStatusBar, QAction, QSizePolicy, QFormLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, Qt, QCoreApplication, QMetaObject, QSize
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 520)

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
        #self.titleLabel.setGeometry(QRect(190, 50, 331, 51))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.titleLabel)

        self.websiteInput = QLineEdit(self.centralwidget) #Website input
        #self.websiteInput.setGeometry(QRect(290, 120, 181, 21))
        self.websiteInput.setObjectName("websiteInput")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.websiteInput)

        self.usernameInput = QLineEdit(self.centralwidget) #Username input
        #self.usernameInput.setGeometry(QRect(290, 150, 181, 21))
        self.usernameInput.setObjectName("usernameInput")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.usernameInput)

        self.passwordInput = QLineEdit(self.centralwidget) #Password input
        #self.passwordInput.setGeometry(QRect(290, 190, 181, 21))
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.passwordInput)

        font = QFont()
        font.setPointSize(11)
        self.websiteLabel = QLabel(self.centralwidget) #Website label
        #self.websiteLabel.setGeometry(QRect(200, 120, 81, 21))
        self.websiteLabel.setFont(font)
        self.websiteLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.websiteLabel.setObjectName("websiteLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.websiteLabel)

        self.usernameLabel = QLabel(self.centralwidget) #Username label
        #self.usernameLabel.setGeometry(QRect(200, 150, 81, 21))
        self.usernameLabel.setFont(font)
        self.usernameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.usernameLabel)

        self.passwordLabel = QLabel(self.centralwidget) #Password label
        #self.passwordLabel.setGeometry(QRect(200, 190, 81, 21))
        self.passwordLabel.setFont(font)
        self.passwordLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.passwordLabel)

        self.startDateEdit = QDateEdit(self.centralwidget) #Start date input
        #self.startDateEdit.setGeometry(QRect(360, 250, 110, 22))
        self.startDateEdit.setObjectName("startDateEdit")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.startDateEdit)

        self.endDateEdit = QDateEdit(self.centralwidget) #End date input
        #self.endDateEdit.setGeometry(QRect(360, 280, 110, 22))
        self.endDateEdit.setObjectName("endDateEdit")
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.endDateEdit)

        self.searchButton = QPushButton(self.centralwidget) #Search button
        #self.searchButton.setGeometry(QRect(320, 330, 101, 31))
        self.searchButton.setObjectName("searchButton")
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.searchButton)
        self.searchButton.clicked.connect(self.search)

        self.centralwidget.raise_()
        self.passwordLabel.raise_()
        self.passwordInput.raise_()
        self.titleLabel.raise_()
        self.usernameLabel.raise_()
        self.usernameInput.raise_()
        self.websiteLabel.raise_()
        self.startDateEdit.raise_()
        self.endDateEdit.raise_()
        self.searchButton.raise_()
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "BookAutomatic"))
        self.titleLabel.setText(_translate("MainWindow", "Welcome to BookAutomatic"))
        self.websiteLabel.setText(_translate("MainWindow", "Website:"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.contactMenu.setTitle(_translate("MainWindow", "Contact Us"))
        self.actionGitHub.setText(_translate("MainWindow", "GitHub Page"))

    def contactPage(self):
        import webbrowser
        webbrowser.open("https://github.com/mronfire/bookAutomatic")

    def search(self):
        mbox = QMessageBox()
        mbox.setText("Opening website for you...")
        mbox.setStandardButtons(QMessageBox.Ok)
        mbox.exec_()

        from search import Search
        try:
            s = Search()
            # s.login()
            # s.getToListings()
            # s.findMatch()
            # s.checkCart()
            # s.closeDriver()

        except Exception as e:
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