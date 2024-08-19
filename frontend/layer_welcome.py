from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_layer_1(object):
    def setupUi(self, layer_1):
        """
        Set up the user interface for the Welcome screen.
        
        This method creates and arranges the widgets on the welcome screen, including the welcome label, 
        description label, and button to transition to the Depressiveness screen. It also applies styles 
        and layouts to ensure the content is centered.
        
        Args:
            layer_1 (QMainWindow): The main window where the UI components will be placed.
        """
        layer_1.setObjectName("layer_1")
        layer_1.resize(792, 572) # Set the size of the window
        layer_1.setStyleSheet("QWidget#layer_1{\n"
                             "\n"
                             "background-color:qlineargradient(spread:pad, x1:0.147727, y1:0.17, x2:1, y2:1, stop:0 rgba(71, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
                             "}\n"
                             "")
        
        # Create a central widget with a vertical layout to center the content
        self.centralWidget = QtWidgets.QWidget(layer_1)
        self.centralWidget.setGeometry(QtCore.QRect(0, -40, 792, 572))  # Full size of the window
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)  # No margins around the layout
        self.centralLayout.setSpacing(30)  # Spacing between widgets
        self.centralLayout.setAlignment(QtCore.Qt.AlignCenter)  # Center the widgets within the layout
        
        # Add the welcome label to the layout, centered horizontally
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
                                 "font: 36pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.centralLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        
        # Add the description label to the layout, centered horizontally
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; color: white;\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.centralLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        
        # Add the button to the layout, centered horizontally
        self.ButtonToDepressiveness = QtWidgets.QPushButton(self.centralWidget)
        self.ButtonToDepressiveness.setStyleSheet("""
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
        self.ButtonToDepressiveness.setObjectName("ButtonToDepressiveness")
        self.ButtonToDepressiveness.setFixedSize(171, 41)
        self.centralLayout.addWidget(self.ButtonToDepressiveness, 0, QtCore.Qt.AlignHCenter)
        
        # Add the button to the layout, centered horizontally
        self.ButtonToAnxiety = QtWidgets.QPushButton(self.centralWidget)
        self.ButtonToAnxiety.setStyleSheet("""
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
        self.ButtonToAnxiety.setObjectName("ButtonToAnxiety")
        self.ButtonToAnxiety.setFixedSize(171, 41)
        self.centralLayout.addWidget(self.ButtonToAnxiety, 0, QtCore.Qt.AlignHCenter)
        
        # Handle text translation for widgets
        self.retranslateUi(layer_1)
        QtCore.QMetaObject.connectSlotsByName(layer_1)

    def retranslateUi(self, layer_1):
        """
        Set the text for the widgets on the Welcome screen.
        
        This method handles the translation of widget text, allowing for internationalization. It sets the 
        window title and the text for the welcome label, description label, and the button.
        
        Args:
            layer_1 (QMainWindow): The main window whose text components will be set.
        """
        _translate = QtCore.QCoreApplication.translate
        layer_1.setWindowTitle(_translate("layer_1", "Welcome"))
        self.label.setText(_translate("layer_1", "Welcome"))
        self.label_2.setText(_translate("layer_1", "Please select a target you want to predict"))
        self.ButtonToDepressiveness.setText(_translate("layer_1", "Depressiveness"))
        self.ButtonToAnxiety.setText(_translate("layer_1", "Anxiety"))


    
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
