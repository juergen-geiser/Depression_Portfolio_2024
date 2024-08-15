from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_layer_2(object):
    def setupUi(self, layer_2):
        layer_2.setObjectName("layer_2")
        layer_2.resize(792, 572)
        layer_2.setStyleSheet("QWidget#layer_2{\n"
                              "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(255, 255, 255, 255));\n"
                              "}\n"
                              "")
        
        self.layoutWidget = QtWidgets.QWidget(layer_2)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 70, 661, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        #labels and comboBoxes for Inputs
        #input age column
        self.label_0_0 = QtWidgets.QLabel(self.layoutWidget)
        self.label_0_0.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_0_0.setObjectName("label_0_0")
        self.label_0_0.setText("age")
        self.gridLayout.addWidget(self.label_0_0, 0, 0, 1, 1)
        
        self.comboBox_0_1 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_0_1.setObjectName("comboBox_0_1")
        self.gridLayout.addWidget(self.comboBox_0_1, 0, 1, 1, 1)
        
        #filling the box with items
        age_dropdown_items = [str(i) for i in range(15,41)]
        self.comboBox_0_1.addItems(age_dropdown_items)
        
                
        #input gender column
        self.label_1_0 = QtWidgets.QLabel(self.layoutWidget)
        self.label_1_0.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_1_0.setObjectName("label_1_0")
        self.label_1_0.setText("gender")
        self.gridLayout.addWidget(self.label_1_0, 2, 0, 1, 1)
        
        self.comboBox_1_1 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_1_1.setStyleSheet("")
        self.comboBox_1_1.setObjectName("comboBox_1_1")
        self.gridLayout.addWidget(self.comboBox_1_1, 2, 1, 1, 1)
        
        #filling the box with items
        gender_dropdown_items = ["female", "male"]
        self.comboBox_1_1.addItems(gender_dropdown_items)

        
        #input height, 1/2 of the bmi column
        self.label_2_0 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2_0.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2_0.setObjectName("label_2_0")
        self.label_2_0.setText("height in cm")
        self.gridLayout.addWidget(self.label_2_0, 3, 0, 1, 1)
        
        self.comboBox_2_1 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2_1.setObjectName("comboBox_2_1")
        self.gridLayout.addWidget(self.comboBox_2_1, 3, 1, 1, 1)
        
        #filling the box
        height_dropdown_items = [str(i) for i in range(140,221)]
        self.comboBox_2_1.addItems(height_dropdown_items)
        
        
        #input weight, 2/2 of the bmi column
        self.label_3_0 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3_0.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3_0.setObjectName("label_3_0")
        self.label_3_0.setText("weight in kg")
        self.gridLayout.addWidget(self.label_3_0, 4, 0, 1, 1)
               
        self.comboBox_3_1 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3_1.setObjectName("comboBox_3_1")
        self.gridLayout.addWidget(self.comboBox_3_1, 4, 1, 1, 1)
        
        #filling the box
        weight_dropdown_items = [str(i) for i in range(40,251)]
        self.comboBox_2_1.addItems(weight_dropdown_items)
        
        #input epworth_score
        self.label_4_0 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4_0.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4_0.setObjectName("label_4_0")
        self.label_4_0.setText("epworth_score")
        self.gridLayout.addWidget(self.label_4_0, 5, 0, 1, 1)
        
        self.comboBox_4_1 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_4_1.setObjectName("comboBox_4_1")
        self.gridLayout.addWidget(self.comboBox_4_1, 5, 1, 1, 1)
        
        #filling the box
        epworth_score_dropdown_items = [str(i) for i in np.arange(0,32.1,0.1)]
        self.comboBox_2_1.addItems(epworth_score_dropdown_items)
        
        
        #input anxiety_diagnosis       
        self.label_0_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_0_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_0_2.setObjectName("label_0_2")
        self.label_0_2.setText("anxiety_diagnosis")
        self.gridLayout.addWidget(self.label_0_2, 0, 2, 1, 1)
        
        self.comboBox_0_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_0_3.setObjectName("comboBox_0_3")
        self.gridLayout.addWidget(self.comboBox_0_3, 0, 3, 1, 1)
        
        
        #input anxiety_treatment
        self.label_1_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_1_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_1_2.setObjectName("label_1_2")
        self.label_1_2.setText("anxiety_treatment")
        self.gridLayout.addWidget(self.label_1_2, 2, 2, 1, 1)
        
        self.comboBox_1_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_1_3.setObjectName("comboBox_1_3")
        self.gridLayout.addWidget(self.comboBox_1_3, 2, 3, 1, 1)
        
        
        #input gad_score
        self.label_2_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2_2.setObjectName("label_2_2")
        self.label_2_2.setText("gad_score")
        self.gridLayout.addWidget(self.label_2_2, 3, 2, 1, 1)
        
        self.comboBox_2_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2_3.setObjectName("comboBox_2_3")
        self.gridLayout.addWidget(self.comboBox_2_3, 3, 3, 1, 1)
        
        
        #input depressiveness_diagnosis
        self.label_3_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3_2.setObjectName("label_3_2")
        self.label_3_2.setText("depressiveness_diagnosis")
        self.gridLayout.addWidget(self.label_3_2, 4, 2, 1, 1)
        
        self.comboBox_3_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3_3.setObjectName("comboBox_3_3")
        self.gridLayout.addWidget(self.comboBox_3_3, 4, 3, 1, 1)
        
        
        #input depressiveness_treatment
        self.label_4_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4_2.setObjectName("label_4_2")
        self.label_4_2.setText("depressiveness_treatment")
        self.gridLayout.addWidget(self.label_4_2, 5, 2, 1, 1)
        
        self.comboBox_4_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_4_3.setObjectName("comboBox_4_3")
        self.gridLayout.addWidget(self.comboBox_4_3, 5, 3, 1, 1)
       
       
        #output
        self.outputField = QtWidgets.QTextEdit(layer_2)
        self.outputField.setGeometry(QtCore.QRect(50, 390, 651, 121))
        self.outputField.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 202, 202, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                       "border-radius: 10.0px;\n"
                                       "")
        self.outputField.setObjectName("outputField")
        
        #headline 
        self.headlineDepressiveness = QtWidgets.QLabel(layer_2)
        self.headlineDepressiveness.setGeometry(QtCore.QRect(90, 10, 571, 41))
        self.headlineDepressiveness.setStyleSheet("color:rgb(255, 255, 255);\n"
                                                  "font: 24pt \"MS Shell Dlg 2\";")
        self.headlineDepressiveness.setObjectName("headlineDepressiveness")
        
        self.frame = QtWidgets.QFrame(layer_2)
        self.frame.setGeometry(QtCore.QRect(70, 260, 601, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        #buttons
        #predict
        self.pushButton_predict = QtWidgets.QPushButton(self.frame)
        self.pushButton_predict.setGeometry(QtCore.QRect(90, 30, 141, 41))
        self.pushButton_predict.setStyleSheet("background-color:rgb(223, 223, 223);\n"
                                              "color: rgb(54, 54, 54);\n"
                                              "border-radius:10.0px;\n"
                                              "font: 14pt \"MS Shell Dlg 2\";\n"
                                              "")        
        self.pushButton_predict.setObjectName("pushButton_predict")
        
        #home- back to welcome page
        self.ButtonToWelcome = QtWidgets.QPushButton(self.frame)
        self.ButtonToWelcome.setGeometry(QtCore.QRect(370, 30, 191, 41))
        self.ButtonToWelcome.setStyleSheet("background-color:rgb(223, 223, 223);\n"
                                           "color: rgb(54, 54, 54);\n"
                                           "border-radius:10.0px;\n"
                                           "font: 14pt \"MS Shell Dlg 2\";")
        self.ButtonToWelcome.setObjectName("ButtonToWelcome")

        self.retranslateUi(layer_2)
        QtCore.QMetaObject.connectSlotsByName(layer_2)

    def retranslateUi(self, layer_2):
            
        _translate = QtCore.QCoreApplication.translate
        
        layer_2.setWindowTitle(_translate("layer_2", "Form"))
                
        self.outputField.setHtml(_translate("layer_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/EC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here comes the prediction...</p></body></html>"))
        
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
