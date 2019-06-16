from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import * #mport all from QtWidgets and make message box

app = QtWidgets.QApplication([])
dlg = uic.loadUi("note.ui")

def addItem():
    if not dlg.lineEdit_item.text()=="": #to avoid empty list
        dlg.listWidget.addItem(dlg.lineEdit_item.text())
    else:
        show_message("Warning!", "You should type at least one item") #if nothing whritten

    dlg.lineEdit_item.setText("") #after adding it's removed automatically

def show_message(title, message):
#QMessageBox.information(None,"Title","Message") # ex. name of box and message
    QMessageBox.information(None,title,message)

dlg.pushButton_addItem.clicked.connect(addItem) #button connected to addItem
dlg.lineEdit_item.returnPressed.connect(addItem)

dlg.show()
app.exec()
