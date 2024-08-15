import sys
import joblib
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QDialog, QWidget
from welcome import Ui_layer_1
from depressiveness import Ui_layer_2

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        self.ui = Ui_layer_1()
        self.ui.setupUi(self)
        self.ui.ButtonToDepressiveness.clicked.connect(self.goToDepressiveness)
        
    def goToDepressiveness(self):
        depressive = Depressiveness()
        widget.addWidget(depressive)
        widget.setCurrentIndex(widget.currentIndex() +1)


class Depressiveness(QDialog):
    def __init__(self):
        super(Depressiveness, self).__init__()
        self.ui = Ui_layer_2()
        self.ui.setupUi(self)
        
        #linking the buttons
        self.ui.ButtonToWelcome.clicked.connect(self.goToWelcome)
        self.ui.pushButton_predict.clicked.connect(self.predict)
        
        # loading the model
        self.model = joblib.load("./models/best_model_depression.pkl")  
        
    def goToWelcome(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
        
    def getInputs(self):
        inputs = []
        
        # age
        inputs.append(float(self.ui.comboBox_0_1.currentText()))
        
        # gender
        inputs.append(0 if self.ui.comboBox_1_1.currentText() == "female" else 1)
        
        # bmi inlcuding the calculation 
        height = float(self.ui.comboBox_2_1.currentText())
        weight = float(self.ui.comboBox_3_1.currentText())
        bmi = weight / ((height / 100) ** 2)
        inputs.append(bmi)
        
        # epworth_score
        inputs.append(float(self.ui.comboBox_4_1.currentText()))  
                
        # gad_score
        inputs.append(float(self.ui.comboBox_2_3.currentText()))
        
        # depressiveness_awareness
        inputs.append(1 if self.ui.comboBox_3_3.currentText() == "yes" or self.ui.comboBox_4_3.currentText() == "yes"else 0)
        
        # anxiety_awareness
        inputs.append(1 if self.ui.comboBox_0_3.currentText() == "yes" or self.ui.comboBox_1_3.currentText() == "yes" else 0)  
                
        return inputs
    
    def predict(self):
        inputs = self.getInputs()
        prediction = self.model.predict([inputs])  # predicting
        self.ui.outputField.setText(f'Prediction: {prediction[0]}')  # Output 
        
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