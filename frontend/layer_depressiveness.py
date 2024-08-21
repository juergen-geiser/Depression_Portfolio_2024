from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_layer_2(object):
    def setupUi(self, layer_2):
        """
        Set up the user interface for the 'layer_2' window.

        Parameters:
        layer_2 (QtWidgets.QWidget): The widget that acts as the parent for all other UI elements.
        """
        layer_2.setObjectName("layer_2")
        layer_2.resize(792, 572)
        
        # Set the background color with a gradient
        layer_2.setStyleSheet("QWidget#layer_2{\n"
                              "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(255, 255, 255, 255));\n"
                              "}\n"
                              "")
        
        # Widget to hold the grid layout
        self.layoutWidget = QtWidgets.QWidget(layer_2)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 70, 661, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        
        # Grid layout to organize labels and combo boxes
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # Initialize comboBoxes and add them to the grid layout
        self.comboBoxes = []
        self.create_comboBox_with_label("Age", [str(i) for i in range(15, 41)], 0, 0)
        self.create_comboBox_with_label("Gender", ["female", "male"], 1, 0)
        self.create_comboBox_with_label("Height in cm", [str(i) for i in range(140, 221)], 2, 0)
        self.create_comboBox_with_label("Weight in kg", [str(i) for i in range(40, 251)], 3, 0)
        self.create_comboBox_with_label("Sleepiness score (Epworth)", [f"{i:.1f}" for i in range(0, 25)], 4, 0)
        self.create_comboBox_with_label("Anxiety diagnosis", ["no", "yes"], 0, 2)
        self.create_comboBox_with_label("Anxiety treatment", ["no", "yes"], 1, 2)
        self.create_comboBox_with_label("Anxiety score (gad-7)", [str(i) for i in range(0, 22)], 2, 2)
        self.create_comboBox_with_label("Depressiveness diagnosis", ["no", "yes"], 3, 2)
        self.create_comboBox_with_label("Depressiveness treatment", ["no", "yes"], 4, 2)
       
        # Create a text area for output
        self.outputField = QtWidgets.QTextEdit(layer_2)
        self.outputField.setGeometry(QtCore.QRect(50, 390, 651, 121))
        self.outputField.setStyleSheet("""
                                       background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 202, 202, 255), stop:1 rgba(255, 255, 255, 255));
                                       border-radius: 10.0px;
                                       font: 14pt "MS Shell Dlg 2";
                                       """)
        self.outputField.setPlainText("Here comes the prediction...")
        self.outputField.setObjectName("outputField")
        
        # Create the headline label 
        self.headlineDepressiveness = QtWidgets.QLabel(layer_2)
        self.headlineDepressiveness.setGeometry(QtCore.QRect(90, 10, 571, 41))
        self.headlineDepressiveness.setStyleSheet("color:rgb(255, 255, 255);\n"
                                                  "font: 24pt \"MS Shell Dlg 2\";")
        self.headlineDepressiveness.setObjectName("headlineDepressiveness")
        
        # Create a frame to hold the buttons
        self.frame = QtWidgets.QFrame(layer_2)
        self.frame.setGeometry(QtCore.QRect(70, 260, 601, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        # Create the "Predict" button
        self.pushButton_predict = QtWidgets.QPushButton(self.frame)
        self.pushButton_predict.setGeometry(QtCore.QRect(90, 30, 141, 41))
        self.pushButton_predict.setStyleSheet("""
            QPushButton {
                background-color: rgb(223, 223, 223);
                color: rgb(54, 54, 54);
                border-radius: 10.0px;
                font: 14pt "MS Shell Dlg 2";
            }
            QPushButton:pressed {
                background-color: rgb(200, 200, 200); /* a bit darker if clicked */
                border: 2px solid rgb(100, 100, 100); /* a dark frame */
            }
        """)        
        self.pushButton_predict.setObjectName("pushButton_predict")
        
        # Create the "Return to Welcome" button
        self.ButtonToWelcome = QtWidgets.QPushButton(self.frame)
        self.ButtonToWelcome.setGeometry(QtCore.QRect(370, 30, 191, 41))
        self.ButtonToWelcome.setStyleSheet("""
            QPushButton {
                background-color: rgb(223, 223, 223);
                color: rgb(54, 54, 54);
                border-radius: 10.0px;
                font: 14pt "MS Shell Dlg 2";
            }
            QPushButton:pressed {
                background-color: rgb(200, 200, 200); /* a bit darker if clicked */
                border: 2px solid rgb(100, 100, 100); /* a dark frame */
            }
        """)
        self.ButtonToWelcome.setObjectName("ButtonToWelcome")

        # Retranslate the UI elements to set their text values
        self.retranslateUi(layer_2)
        QtCore.QMetaObject.connectSlotsByName(layer_2)
    
    
    def create_comboBox_with_label(self, label_text, items, row, col, placeholder=None):
        """
        Create a QLabel and QComboBox pair, and add them to the grid layout.

        Parameters:
        label_text (str): The text to be displayed on the QLabel.
        items (list): The items to be added to the QComboBox.
        row (int): The row position in the grid layout.
        col (int): The column position in the grid layout.
        """
        # Create and style the QLabel
        label = QtWidgets.QLabel(self.layoutWidget)
        label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        label.setText(label_text)
        self.gridLayout.addWidget(label, row, col, 1, 1)

        # Create and style the QComboBox
        comboBox = QtWidgets.QComboBox(self.layoutWidget)
        comboBox.setObjectName(f"comboBox_{row}_{col+1}")
        comboBox.addItems(items)
        self.gridLayout.addWidget(comboBox, row, col+1, 1, 1)
        
        # Append the comboBox to the list of comboBoxes
        self.comboBoxes.append(comboBox)

    def retranslateUi(self, layer_2):
            
        _translate = QtCore.QCoreApplication.translate
        
        layer_2.setWindowTitle(_translate("layer_2", "Form"))
        
        self.headlineDepressiveness.setText(_translate("layer_2", "Please insert the values of your dataset"))
        self.pushButton_predict.setText(_translate("layer_2", "Predict"))
        self.ButtonToWelcome.setText(_translate("layer_2", "return to Welcome"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    layer_2 = QtWidgets.QWidget()
    ui = Ui_layer_2()
    ui.setupUi(layer_2)
    layer_2.show()
    sys.exit(app.exec_())
