# Depression_Portfolio_2024
Project: Detection of Depression with Machine Learning and Power-BI-Tools

### Project Overview
Objective: The goal of the project is to detect depressivness based on different features, e.g., gender, bmi, depression severity etc.

Context: Based on the research data-set, which is given on [Kaggle: Depression and anxiety data ](https://www.kaggle.com/datasets/shahzadahmad0402/depression-and-anxiety-data), we developped a classification model to identify depressivness related distinctive symptoms, e.g., feelings of melancholy and emptiness, feelings of worry and disturbed sleep, as well as a general loss of initiative and interest in activities. We have to clean the dataset and find the correlations of the different features to predict such depressivness. Difficulties are to detect the correct features, which gave a good overview to the predit such a paramteter. We also saw, based on the data-set, that we also have a relation to suicidal and consider such a behaviour in our ML-methods.

Significance: It is important for parents, teachers, psycholicist to detect in an early stage such relations to depressiveness to start on an early stage a therapy. The benefit of the research allow us with a simple model based on the features: gender, phq_score (measure of the severity of symptoms, which are related to depression) and gad_score (measure, thatwe have a relation of the severity of generalized anxiety disorder) to detect a depressivness, see also the ideas in [Kaggle: Machine_learningproject](https://www.kaggle.com/code/geovaniwoll/machine-learningproject). Furthermore, we generalise the model to full modell with all the features in the dataset and could improve the prediction of such a simpler model.


Goal: The aim of th project was to improve standard models, we also consider a simple app to apply the ML-predictor.

## Team Members

- Team Member 1: [Jürgen Geiser](https://github.com/juergen-geiser)  
- Team Member 2: [Carsten Henkel](https://github.com/CarstenHankel)
- Team Member 3: [Alex Gafron](https://github.com/a-gafron) 
- Team Member 4: [Marcin Grzymowicz](https://github.com/M-Grzymowicz)

## Jupyter Notebooks

This project consists of different Jupyter Notebooks that serve different purposes:

1. **eda_model_depression.ipynb**: 
This notebook focuses on a complex classification of the depressiveness with all columns (features) and could be used as an improved predictve tool for the target: "depressiveness". It is done with RandomForest and gridsearch to improve the classification. We result in a prediction model of the best 10 feature-columns.

2. **interface_eda_model_depression_ML_GUI.ipynb**: 
This notebook focuses on an interface between the ML part given in the eda_model_depression.ipynb file and the GUI-interface. The file: model_depression.pkl has to be loaded, here are stored all the best model with the target "depressiveness" and we also gave the target and the names of the features, that could be used as a first multiple predictve tool. 

3. **method_model_depression.ipynb**: 
This notebook focuses on all possible models, e.g., decision tree, KNN, logistic regression, random forest, which are tested, we apply the results of the EDA in previous notebooks and concentrate on the important features. We could derive and optimal model, which is stored in best_model_depression.pkl, this can be used for the interface GUI or for the notebook interface_method_model_depression_ML_GUI.ipynb.

4. **interface_method_model_depression_ML_GUI.ipynb**: 
This notebook focuses on an interface between the ML part given in the method_model_depression.ipynb file and the GUI-interface. The file: best_model_depression.pkl has to be loaded, here are stored all the best model with the target "depressiveness" and we also gave the target and the names of the features, that could be used as a first multiple predictve tool. 

5. **method_model_anxiousness.ipynb**: 
This notebook focuses on all possible models, e.g., decision tree, KNN, logistic regression, random forest, which are tested, we apply the results of the EDA in previous notebooks and with the help of the PowerBI. We concentrate on the important features. We could derive and optimal model, which is stored in best_model_anxiousness.pkl, this can be used for the interface GUI or for the notebook interface_method_model_anxiousness_ML_GUI.ipynb.

6. **interface_method_model_anxiousness_ML_GUI.ipynb**: 
This notebook focuses on an interface between the ML part given in the method_model_anxiousness.ipynb file and the GUI-interface. The file: best_model_anxiousness.pkl has to be loaded, here are stored all the best model with the target "depressiveness" and we also gave the target and the names of the features, that could be used as a first multiple predictve tool. 


## Frontend

The files essentially define an application that allows the user to input data and receive predictions about the risk of depression and anxiety based on a predefined model. The application offers a simple user interface with clearly structured screens for different prediction purposes.

### 1. WelcomeScreen
This class creates the welcome screen of the application. The screen displays the title and description and offers two buttons that direct the user either to the depression prediction or the anxiety prediction screen.<br>
**Important Methods:**
- goToDepressiveness: Switches to the depression prediction screen.
- goToAnxiety: Switches to the anxiety prediction screen.

### 2. Depressiveness
This class represents the depression prediction screen. It loads a trained model and allows the user to input data and receive a prediction about the risk of depression.<br>
**Important Methods:**
- load_model: Loads the model and the required columns from a file.
- getInputs: Collects user inputs, calculates the BMI, and prepares the inputs for the model prediction.
- predict: Performs the prediction and displays the result as well as the probability.

### 3. Anxiety
This class represents the anxiety prediction screen. It works similarly to the depression screen but is specialized in anxiety.<br>
**Important Methods:**
- getInputs: Collects user inputs, calculates the BMI, and prepares the inputs for the model prediction.
- predict: Performs the prediction and displays the result as well as the probability.

### 4. updateWindowTitle
This function updates the window title based on the current screen being displayed (welcome, depression, or anxiety).

### 5. Welcome_layer
This class defines the layout and user interface of the welcome screen. It creates widgets such as labels and buttons and arranges them on the screen.

### 6. Depression_layer
This class defines the layout and user interface of the depression prediction screen. It includes fields for data input and buttons to make a prediction.

### 7. Anxiety_layer
This class defines the layout and user interface of the anxiety prediction screen. It also includes fields for data input and buttons to make a prediction.

### 8. Main Application Code
This is the main code of the application, which displays the welcome screen and starts the application. It also uses the QStackedWidget to switch between the different screens.

## Installation and Setup with requirements.txt

To set up the project locally, follow these steps:

1. Clone the repository:
```
git clone git@github.com:juergen-geiser/Depression_Portfolio_2024.git
```
2. Navigate to the project directory:
```
cd your-repository
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Download the modified dataset and place it in the project directory. The original dataset can be acquired from the link [Kaggle: Depression and anxiety data ](https://www.kaggle.com/datasets/shahzadahmad0402/depression-and-anxiety-data) and save it to the Directory: data

## Installation and Setup using conda and environment.yml

To set up the project locally, follow these steps:

1. Clone the repository:
```
git clone git@github.com:juergen-geiser/Depression_Portfolio_2024.git
```
2. Navigate to the project directory:
```
cd your-repository
```
3. Install the required environment (you will obtain a new environment called: portfolio_2024)

conda env create --file environment.yml

4. Activate your environment (portfolio_2024):
```
conda activate portfolio_2024

or use Visual Code and activate your enviroment portfolio_2024

```
5. Download the modified dataset and place it in the project directory. The original dataset can be acquired from the link [Kaggle: Depression and anxiety data ](https://www.kaggle.com/datasets/shahzadahmad0402/depression-and-anxiety-data) and save it to the Directory: data

**Note:** If any of the above files are missing, the corresponding functionality may not work as expected.

## Backend: Start of the programs in the folder notebooks/

Backend-programs:

Once the setup is complete, you start the juypter-Notebook and you can make predictions, e.g., on new data using the data-file: aim_test.csv, and you can save you optimal trained model:
If you apply:

eda_model_depression.ipynb, the model is saved in models/ as: eda_model_depression.pkl

method_model_depression.ipynb, the model is saved in models/ as: best_model_depression.pkl

method_model_anxiousness.ipynb,  the model is saved in models/ as: best_model_anxiousness.pkl


## Frontend: Start of the programs in the folder frontend/

Frontend-programs, based on PyQt (GUI), where we applied the backend-results(saved models fpr depressiveness and anxiousness)

Start the main.py in VC or in another Python-editor, be aware, that you switch to the environment: portfolio_2024

Then, you could start with your predictions.

