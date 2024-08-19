from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_DepressivenessScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DepressivenessScreen")
        MainWindow.resize(792, 572)
        MainWindow.setStyleSheet("QWidget#DepressivenessScreen{"
                                "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(255, 255, 255, 255));"
                                "}")
        
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 70, 661, 181))
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        self.comboBoxes = []
        self.create_comboBox_with_label("Age", [str(i) for i in range(15, 41)], 0, 0)
        self.create_comboBox_with_label("Gender", ["female", "male"], 2, 0)
        self.create_comboBox_with_label("Height in cm", [str(i) for i in range(140, 221)], 3, 0)
        self.create_comboBox_with_label("Weight in kg", [str(i) for i in range(40, 251)], 4, 0)
        self.create_comboBox_with_label("Sleepiness score (Epworth)", [f"{i:.1f}" for i in np.arange(0, 32.1, 0.1)], 5, 0)
        self.create_comboBox_with_label("Anxiety diagnosis", ["no", "yes"], 0, 2)
        self.create_comboBox_with_label("Anxiety treatment", ["no", "yes"], 2, 2)
        self.create_comboBox_with_label("Anxiety score (gad-7)", [str(i) for i in range(0, 21)], 3, 2)
        self.create_comboBox_with_label("Depressiveness diagnosis", ["no", "yes"], 4, 2)
        self.create_comboBox_with_label("Depressiveness treatment", ["no", "yes"], 5, 2)
        
        self.outputField = QtWidgets.QTextEdit(MainWindow)
        self.outputField.setGeometry(QtCore.QRect(50, 390, 651, 121))
        self.outputField.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 202, 202, 255), stop:1 rgba(255, 255, 255, 255));"
                                       "border-radius: 10.0px;")
        
        self.headlineDepressiveness = QtWidgets.QLabel(MainWindow)
        self.headlineDepressiveness.setGeometry(QtCore.QRect(90, 10, 571, 41))
        self.headlineDepressiveness.setStyleSheet("color:rgb(255, 255, 255); font: 24pt \"MS Shell Dlg 2\";")
        
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(70, 260, 601, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.pushButton_predict = QtWidgets.QPushButton(self.frame)
        self.pushButton_predict.setGeometry(QtCore.QRect(90, 30, 141, 41))
        self.pushButton_predict.setStyleSheet("""
            QPushButton { background-color: rgb(223, 223, 223); color: rgb(54, 54, 54); border-radius: 10.0px; font: 14pt "MS Shell Dlg 2"; }
            QPushButton:pressed { background-color: rgb(200, 200, 200); border: 2px solid rgb(100, 100, 100); }
        """)
        
        self.ButtonToWelcome = QtWidgets.QPushButton(self.frame)
        self.ButtonToWelcome.setGeometry(QtCore.QRect(370, 30, 191, 41))
        self.ButtonToWelcome.setStyleSheet("""
            QPushButton { background-color: rgb(223, 223, 223); color: rgb(54, 54, 54); border-radius: 10.0px; font: 14pt "MS Shell Dlg 2"; }
            QPushButton:pressed { background-color: rgb(200, 200, 200); border: 2px solid rgb(100, 100, 100); }
        """)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def create_comboBox_with_label(self, label_text, items, row, col):
        label = QtWidgets.QLabel(self.layoutWidget)
        label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: white;")
        label.setText(label_text)
        self.gridLayout.addWidget(label, row, col)
        
        comboBox = QtWidgets.QComboBox(self.layoutWidget)
        comboBox.addItems(items)
        self.gridLayout.addWidget(comboBox, row, col + 1)
        self.comboBoxes.append(comboBox)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DepressivenessScreen", "Depressiveness Prediction"))
        self.headlineDepressiveness.setText(_translate("DepressivenessScreen", "Depressiveness Prediction"))
        self.pushButton_predict.setText(_translate("DepressivenessScreen", "Predict"))
        self.ButtonToWelcome.setText(_translate("DepressivenessScreen", "Back to Welcome"))
