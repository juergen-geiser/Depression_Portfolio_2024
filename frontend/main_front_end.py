import sys
import joblib
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QDialog, QWidget

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi('Welcome.ui', self)
        self.ButtonToDepressiveness.clicked.connect(self.goToDepressiveness)
        
    def goToDepressiveness(self):
        depressive = Depressiveness()
        widget.addWidget(depressive)
        widget.setCurrentIndex(widget.currentIndex() +1)


class Depressiveness(QDialog):
    def __init__(self):
        super(Depressiveness, self).__init__()
        loadUi('Depressiveness.ui', self)
        self.ButtonToWelcome.clicked.connect(self.goToWelcome)
        self.pushButton_predict.clicked.connect(self.predict)
        self.model = joblib.load('simple_model.pkl')  # loading the model
        
    def goToWelcome(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
        
    def getInputs(self):
        inputs = []
        inputs.append(float(self.lineEdit_1.text()))  # age
        inputs.append(float(self.lineEdit_2.text()))  # gender
        inputs.append(float(self.lineEdit_3.text()))  # bmi
        inputs.append(float(self.lineEdit_4.text()))  # gad-score
        inputs.append(float(self.lineEdit_5.text()))  # anxiety_diagnosis
        inputs.append(float(self.lineEdit_6.text()))  # epworth_score
        inputs.append(float(self.lineEdit_7.text()))  # who-bmi
        return inputs
    
    def predict(self):
        inputs = self.getInputs()
        prediction = self.model.predict([inputs])  # predicting
        self.textEdit.setText(f'Prediction: {prediction[0]}')  # Output 
        
#main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(500)
widget.setFixedWidth(750)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print('Existing')