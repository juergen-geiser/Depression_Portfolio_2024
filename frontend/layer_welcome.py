from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WelcomeScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("WelcomeScreen")
        MainWindow.resize(792, 572)
        MainWindow.setStyleSheet("QWidget#WelcomeScreen{"
                                "background-color:qlineargradient(spread:pad, x1:0.147727, y1:0.17, x2:1, y2:1, stop:0 rgba(71, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));"
                                "}")
        
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setGeometry(QtCore.QRect(0, -40, 792, 572))
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.centralLayout.setSpacing(30)
        self.centralLayout.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setStyleSheet("color:rgb(255, 255, 255); font: 36pt \"MS Shell Dlg 2\";")
        self.centralLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: white;")
        self.centralLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        
        self.ButtonToDepressiveness = QtWidgets.QPushButton(self.centralWidget)
        self.ButtonToDepressiveness.setStyleSheet("""
            QPushButton { background-color: rgb(223, 223, 223); color: rgb(54, 54, 54); border-radius: 10.0px; font: 14pt "MS Shell Dlg 2"; }
            QPushButton:pressed { background-color: rgb(200, 200, 200); border: 2px solid rgb(100, 100, 100); }
        """)
        self.ButtonToDepressiveness.setFixedSize(171, 41)
        self.centralLayout.addWidget(self.ButtonToDepressiveness, 0, QtCore.Qt.AlignHCenter)
        
        self.ButtonToAnxiety = QtWidgets.QPushButton(self.centralWidget)
        self.ButtonToAnxiety.setStyleSheet("""
            QPushButton { background-color: rgb(223, 223, 223); color: rgb(54, 54, 54); border-radius: 10.0px; font: 14pt "MS Shell Dlg 2"; }
            QPushButton:pressed { background-color: rgb(200, 200, 200); border: 2px solid rgb(100, 100, 100); }
        """)
        self.ButtonToAnxiety.setFixedSize(171, 41)
        self.centralLayout.addWidget(self.ButtonToAnxiety, 0, QtCore.Qt.AlignHCenter)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("WelcomeScreen", "Welcome"))
        self.label.setText(_translate("WelcomeScreen", "Welcome"))
        self.label_2.setText(_translate("WelcomeScreen", "Please select a target you want to predict"))
        self.ButtonToDepressiveness.setText(_translate("WelcomeScreen", "Depressiveness"))
        self.ButtonToAnxiety.setText(_translate("WelcomeScreen", "Anxiety"))