from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_layer_1(object):
    def setupUi(self, layer_1):
        layer_1.setObjectName("layer_1")
        layer_1.resize(750, 500)
        layer_1.setStyleSheet("QWidget#layer_1{\n"
                             "\n"
                             "background-color:qlineargradient(spread:pad, x1:0.147727, y1:0.17, x2:1, y2:1, stop:0 rgba(71, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
                             "}\n"
                             "")
        
        self.label = QtWidgets.QLabel(layer_1)
        self.label.setGeometry(QtCore.QRect(270, 100, 231, 61))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
                                 "font: 36pt \"MS Shell Dlg 2\";")        
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(layer_1)
        self.label_2.setGeometry(QtCore.QRect(200, 180, 371, 51))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: white;\n"
                                   "")  
        self.label_2.setObjectName("label_2")
        
        self.ButtonToDepressiveness = QtWidgets.QPushButton(layer_1)
        self.ButtonToDepressiveness.setGeometry(QtCore.QRect(280, 270, 171, 41))
        self.ButtonToDepressiveness.setStyleSheet("""
            QPushButton {
                background-color: rgb(223, 223, 223);
                color: rgb(54, 54, 54);
                border-radius: 10.0px;
                font: 14pt "MS Shell Dlg 2";
            }
            QPushButton:pressed {
                background-color: rgb(200, 200, 200); /* Etwas dunkler bei Klick */
                border: 2px solid rgb(100, 100, 100); /* Dunklerer Rahmen */
            }
        """)
        self.ButtonToDepressiveness.setObjectName("ButtonToDepressiveness")

        self.retranslateUi(layer_1)
        QtCore.QMetaObject.connectSlotsByName(layer_1)

    def retranslateUi(self, layer_1):
        _translate = QtCore.QCoreApplication.translate
        layer_1.setWindowTitle(_translate("layer_1", "Form"))
        self.label.setText(_translate("layer_1", "Welcome"))
        self.label_2.setText(_translate("layer_1", "Please select a target you want to predict"))
        self.ButtonToDepressiveness.setText(_translate("layer_1", "Depressiveness"))


    
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    layer_1 = QtWidgets.QMainWindow() 
    ui = Ui_layer_1()
    ui.setupUi(layer_1)
    layer_1.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
