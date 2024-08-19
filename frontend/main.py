import sys
import pickle
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QDialog, QWidget
from layer_welcome import Ui_layer_1
from layer_depressiveness import Ui_layer_2
from layer_anxiety import Ui_layer_3

class WelcomeScreen(QDialog):
    def __init__(self):
        """
        Initialize the WelcomeScreen with the UI from layer_welcome and connect the button to transition to Depressiveness screen.
        """
        super(WelcomeScreen, self).__init__()
        self.ui = Ui_layer_1()
        self.ui.setupUi(self)
        self.ui.ButtonToDepressiveness.clicked.connect(self.goToDepressiveness)
        
    def goToDepressiveness(self):
        """
        Transition to the Depressiveness screen.
        """
        depressive = Depressiveness()
        widget.addWidget(depressive)
        widget.setCurrentIndex(widget.currentIndex() +1)

    def goToAnxiety(self):
        """
        Transition to the Anxiety screen.
        """
        anxious = Anxiety()
        widget.addWidget(anxious)
        widget.setCurrentIndex(widget.currentIndex() +1)

class Depressiveness(QDialog):
    def __init__(self):
        """
        Initialize the Depressiveness screen with the UI from layer_depressiveness.
        Load the model and its required feature columns and target columns.
        """
        super(Depressiveness, self).__init__()
        self.ui = Ui_layer_2()
        self.ui.setupUi(self)
        
        #linking the buttons
        self.ui.ButtonToWelcome.clicked.connect(self.goToWelcome)
        self.ui.pushButton_predict.clicked.connect(self.predict)
        
        # loading the model
        with open('./models/best_model_depression.pkl', 'rb') as file:
            self.model = pickle.load(file)  # Load the models first (as they were saved first)
            self.target_col = pickle.load(file)   # Load status_names second
            self.feature_cols = pickle.load(file)    # Load target_cols third
        
    def goToWelcome(self):
        """
        Transition back to the Welcome screen.
        """
        widget.setCurrentIndex(widget.currentIndex() - 1)
        
    def getInputs(self):
        """
        Collect the input values from the combo boxes, calculate BMI, and format them for model prediction.

        Returns:
        list: A list of input values formatted for prediction.
        """
        inputs = []
        
        # Age
        inputs.append(float(self.ui.comboBoxes[0].currentText()))
        
        # Gender (0 for female, 1 for male)
        inputs.append(0 if self.ui.comboBoxes[1].currentText() == "female" else 1)
        
        # Calculate BMI using height and weight
        height = float(self.ui.comboBoxes[2].currentText())
        weight = float(self.ui.comboBoxes[3].currentText())
        bmi = weight / ((height / 100) ** 2)
        inputs.append(bmi)
        
        # Epworth score
        inputs.append(float(self.ui.comboBoxes[4].currentText()))
        
        # GAD score
        inputs.append(float(self.ui.comboBoxes[7].currentText()))
        
        # Depressiveness awareness (1 if either diagnosis or treatment is "yes")
        depressiveness_awareness = (1 if self.ui.comboBoxes[8].currentText() == "yes" or self.ui.comboBoxes[9].currentText() == "yes" else 0)
        inputs.append(depressiveness_awareness)
        
        # Anxiety awareness (1 if either diagnosis or treatment is "yes")
        anxiety_awareness = (1 if self.ui.comboBoxes[5].currentText() == "yes" or self.ui.comboBoxes[6].currentText() == "yes" else 0)
        inputs.append(anxiety_awareness)
                
        return inputs
    
    def predict(self):
        """
        Perform prediction using the collected inputs and update the output field with the result.
        """
        inputs = self.getInputs()
        X_aim = pd.DataFrame([inputs], columns=self.feature_cols)
        prediction = self.model.predict(X_aim)  # predicting
        self.ui.outputField.setText(f'Prediction: {prediction[0]}')  # Output 
        
class Anxiety(QDialog):
    def __init__(self):
        """
        Initialize the Anxiety screen with the UI from layer_anxiety.
        Load the model and its required feature columns and target columns.
        """
        super(Anxiety, self).__init__()
        self.ui = Ui_layer_3()
        self.ui.setupUi(self)
        
        #linking the buttons
        self.ui.ButtonToWelcome.clicked.connect(self.goToWelcome)
        self.ui.pushButton_predict.clicked.connect(self.predict)
        
        # loading the model
        with open('./models/best_model_depression.pkl', 'rb') as file:
            self.model = pickle.load(file)  # Load the models first (as they were saved first)
            self.target_col = pickle.load(file)   # Load status_names second
            self.feature_cols = pickle.load(file)    # Load target_cols third
        
    def goToWelcome(self):
        """
        Transition back to the Welcome screen.
        """
        widget.setCurrentIndex(widget.currentIndex() - 1)
        
    def getInputs(self):
        """
        Collect the input values from the combo boxes, calculate BMI, and format them for model prediction.

        Returns:
        list: A list of input values formatted for prediction.
        """
        inputs = []
        
        # Age
        inputs.append(float(self.ui.comboBoxes[0].currentText()))
        
        # Gender (0 for female, 1 for male)
        inputs.append(0 if self.ui.comboBoxes[1].currentText() == "female" else 1)
        
        # Calculate BMI using height and weight
        height = float(self.ui.comboBoxes[2].currentText())
        weight = float(self.ui.comboBoxes[3].currentText())
        bmi = weight / ((height / 100) ** 2)
        inputs.append(bmi)
        
        # Epworth score
        inputs.append(float(self.ui.comboBoxes[4].currentText()))
        
        # GAD score
        inputs.append(float(self.ui.comboBoxes[7].currentText()))
        
        # Depressiveness awareness (1 if either diagnosis or treatment is "yes")
        depressiveness_awareness = (1 if self.ui.comboBoxes[8].currentText() == "yes" or self.ui.comboBoxes[9].currentText() == "yes" else 0)
        inputs.append(depressiveness_awareness)
        
        # Anxiety awareness (1 if either diagnosis or treatment is "yes")
        anxiety_awareness = (1 if self.ui.comboBoxes[5].currentText() == "yes" or self.ui.comboBoxes[6].currentText() == "yes" else 0)
        inputs.append(anxiety_awareness)
                
        return inputs
    
    def predict(self):
        """
        Perform prediction using the collected inputs and update the output field with the result.
        """
        inputs = self.getInputs()
        X_aim = pd.DataFrame([inputs], columns=self.feature_cols)
        prediction = self.model.predict(X_aim)  # predicting
        self.ui.outputField.setText(f'Prediction: {prediction[0]}')  # Output 
        
#main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(572)
widget.setFixedWidth(792)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print('Existing')