from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

def dialog():
    mbox = QMessageBox()

    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now the best")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    mbox.exec_()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(600, 500)
    w.setWindowTitle("BookAutomatic")

    label = QLabel(w)
    label.setText("Behold, Mario")
    label.move(100, 130)
    label.show()

    btn = QPushButton(w)
    btn.setText("Beheld")
    btn.move(110, 150)
    btn.show()
    btn.clicked.connect(dialog)

    w.show()
    sys.exit(app.exec_())