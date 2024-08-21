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
        self.ui.ButtonToAnxiety.clicked.connect(self.goToAnxiety)
        
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
        widget.setCurrentIndex(widget.currentIndex() +2)

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
        
        # Load the model
        self.load_model()
        
    def load_model(self):
        """
        Load the model and its associated feature columns and target columns.
        """
        with open('./models/best_model_depression.pkl', 'rb') as file:
            self.model = pickle.load(file)  # Load the model
            self.target_col = pickle.load(file)   # Load status_names
            self.feature_cols = pickle.load(file)    # Load feature_cols
        
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
        predicted_class = prediction[0]
        
        # Get the probability for both classes
        probabilities = self.model.predict_proba(X_aim)
        prob_class_0 = probabilities[:, 0] # Probability for class 0
        prob_class_1 = probabilities[:, 1]  # Probability for class 1
        
        # Print the predicted class and corresponding probability
        if predicted_class == 0:
            self.ui.outputField.setText(f"Predicted Class: Not Depressive, Probability = {prob_class_0[0]:.2f}")
        else:
            self.ui.outputField.setText(f"Predicted Class: Depressive, Probability = {prob_class_1[0]:.2f}") 
        
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
        with open('./models/best_model_anxiousness.pkl', 'rb') as file:
            self.model = pickle.load(file)  # Load the models first (as they were saved first)
            self.target_col = pickle.load(file)   # Load status_names second
            self.feature_cols = pickle.load(file)    # Load target_cols third
        
    def goToWelcome(self):
        """
        Transition back to the Welcome screen.
        """
        widget.setCurrentIndex(widget.currentIndex() - 2)
        
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
        
        # PHQ score
        inputs.append(float(self.ui.comboBoxes[4].currentText()))
        
        # Epworth score
        inputs.append(float(self.ui.comboBoxes[5].currentText()))
        
        # Calculate BMI using height and weight
        height = float(self.ui.comboBoxes[9].currentText())
        weight = float(self.ui.comboBoxes[10].currentText())
        bmi = weight / ((height / 100) ** 2)
        inputs.append(bmi)
                
        # Depressiveness awareness (1 if either diagnosis or treatment is "yes")
        depressiveness_awareness = (1 if self.ui.comboBoxes[2].currentText() == "yes" or self.ui.comboBoxes[3].currentText() == "yes" else 0)
        inputs.append(depressiveness_awareness)
        
        # Anxiety awareness (1 if either diagnosis or treatment is "yes")
        anxiety_awareness = (1 if self.ui.comboBoxes[7].currentText() == "yes" or self.ui.comboBoxes[8].currentText() == "yes" else 0)
        inputs.append(anxiety_awareness)
        
        # Suicidal
        inputs.append(1 if self.ui.comboBoxes[6].currentText() == "yes" else 0)
                
        return inputs
    
    def predict(self):
        """
        Perform prediction using the collected inputs and update the output field with the result.
        """
        inputs = self.getInputs()
        X_aim = pd.DataFrame([inputs], columns=self.feature_cols)
        prediction = self.model.predict(X_aim)  # predicting
        predicted_class = prediction[0]
        
        # Get the probability for both classes
        probabilities = self.model.predict_proba(X_aim)
        prob_class_0 = probabilities[:, 0] # Probability for class 0
        prob_class_1 = probabilities[:, 1]  # Probability for class 1
        
        # Print the predicted class and corresponding probability
        if predicted_class == 0:
            self.ui.outputField.setText(f"Predicted Class: Non-Anxious, Probability = {prob_class_0[0]:.2f}")
        else:
            self.ui.outputField.setText(f"Predicted Class: Anxious, Probability = {prob_class_1[0]:.2f}") 
        
        
        
        
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