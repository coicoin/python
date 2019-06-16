from PyQt5 import QtWidgets, uic

def Convert():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text())*65.3))    #be sure about LineEdit, check in Obj Inspector
#dlg стартует каждый элемент в ui
def Convert_2():
    dlg.lineEdit_3.setText(str(float(dlg.lineEdit_4.text())/65.3))
def Convert_3():
    dlg.lineEdit_5.setText(str(float(dlg.lineEdit_6.text())*73.2))
def Convert_4():
    dlg.lineEdit_8.setText(str(float(dlg.lineEdit_7.text())/73.2))
    
app = QtWidgets.QApplication([]) #initialized user interface
dlg = uic.loadUi("converter.ui") #attach our ui

dlg.lineEdit.setFocus() #set color when clicked
dlg.lineEdit.setPlaceholderText("$") #temporary title intil enter
dlg.lineEdit_2.setPlaceholderText("₽") #temporary title intil enter
dlg.lineEdit_4.setFocus()
dlg.lineEdit_4.setPlaceholderText("₽") #temporary title intil enter
dlg.lineEdit_3.setPlaceholderText("$") #temporary title intil enter
dlg.lineEdit_6.setFocus()
dlg.lineEdit_6.setPlaceholderText("€") #temporary title intil enter
dlg.lineEdit_5.setPlaceholderText("₽") #temporary title intil enter
dlg.lineEdit_7.setFocus()
dlg.lineEdit_7.setPlaceholderText("₽") #temporary title intil enter
dlg.lineEdit_8.setPlaceholderText("€") #temporary title intil enter

dlg.pushButton.clicked.connect(Convert) #when button was pressed
dlg.pushButton_2.clicked.connect(Convert_2)
dlg.pushButton_3.clicked.connect(Convert_3)
dlg.pushButton_4.clicked.connect(Convert_4)


dlg.lineEdit_2.setReadOnly(True) #set ro for button 2, avoid enter
dlg.lineEdit_3.setReadOnly(True)
dlg.lineEdit_5.setReadOnly(True)
dlg.lineEdit_8.setReadOnly(True)
dlg.lineEdit.returnPressed.connect(Convert) #receive enter

dlg.show() #user int. will be shown when program start
app.exec()
