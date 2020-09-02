from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout

def dialog():
    mbox = QMessageBox()

    mbox.setText("Your allegiance has been noted")
    #mbox.setDetailedText("You are now the best")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    mbox.exec_()

if __name__ == '__main__':
    import sys
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = QMainWindow()
    window.resize(250, 150)

    #appctxt.setStyle("Fusion")
    window = QWidget()
    window.resize(800, 600)
    window.setWindowTitle("BookAutomatic")

    label = QLabel(window)
    label.setText("Welcome to BookAutomatic! Go ahead and let us find an available site for you...")
    label.move(100, 100)
    label.show()

    websiteLabel = QLineEdit()
    usernameLabel = QLineEdit()
    passwordLabel = QLineEdit()

    # Search button
    searchBtn = QPushButton(window)
    searchBtn.setText("Search")
    searchBtn.move(300, 150)
    searchBtn.show()
    searchBtn.clicked.connect(dialog)

    vbox = QVBoxLayout(window)
    vbox.addWidget(websiteLabel)
    vbox.addWidget(usernameLabel)
    vbox.addWidget(passwordLabel)
    vbox.addWidget(searchBtn)
    
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)