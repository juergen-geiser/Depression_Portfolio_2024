import sys
from PyQt5 import QtWidgets
from layer_welcome import Ui_WelcomeScreen
from layer_depressiveness import Ui_DepressivenessScreen
from layer_anxiety import Ui_AnxietyScreen

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Initialize screens
        self.welcome_screen = QtWidgets.QWidget()
        self.depressiveness_screen = QtWidgets.QWidget()
        self.anxiety_screen = QtWidgets.QWidget()
        
        self.setup_welcome_screen()
        self.setup_depressiveness_screen()
        self.setup_anxiety_screen()
        
        # Setup stacked widget
        self.stacked_widget.addWidget(self.welcome_screen)
        self.stacked_widget.addWidget(self.depressiveness_screen)
        self.stacked_widget.addWidget(self.anxiety_screen)
        
        self.setWindowTitle("Mental Health Predictor")
        self.resize(800, 600)
    
    def setup_welcome_screen(self):
        self.ui_welcome = Ui_WelcomeScreen()
        self.ui_welcome.setupUi(self.welcome_screen)
        
        # Connect buttons
        self.ui_welcome.ButtonToDepressiveness.clicked.connect(self.show_depressiveness_screen)
        self.ui_welcome.ButtonToAnxiety.clicked.connect(self.show_anxiety_screen)
    
    def setup_depressiveness_screen(self):
        self.ui_depressiveness = Ui_DepressivenessScreen()
        self.ui_depressiveness.setupUi(self.depressiveness_screen)
        
        # Connect buttons
        self.ui_depressiveness.pushButton_predict.clicked.connect(self.predict_depressiveness)
        self.ui_depressiveness.ButtonToWelcome.clicked.connect(self.show_welcome_screen)
    
    def setup_anxiety_screen(self):
        self.ui_anxiety = Ui_AnxietyScreen()
        self.ui_anxiety.setupUi(self.anxiety_screen)
        
        # Connect buttons
        self.ui_anxiety.pushButton_predict.clicked.connect(self.predict_anxiety)
        self.ui_anxiety.ButtonToWelcome.clicked.connect(self.show_welcome_screen)
    
    def show_welcome_screen(self):
        self.stacked_widget.setCurrentWidget(self.welcome_screen)
    
    def show_depressiveness_screen(self):
        self.stacked_widget.setCurrentWidget(self.depressiveness_screen)
    
    def show_anxiety_screen(self):
        self.stacked_widget.setCurrentWidget(self.anxiety_screen)
    
    def predict_depressiveness(self):
        # Add prediction logic here
        pass
    
    def predict_anxiety(self):
        # Add prediction logic here
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
