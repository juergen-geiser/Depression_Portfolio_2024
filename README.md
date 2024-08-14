# Depression_Portfolo_2024
Project: Detection of Depression with Machine Learning and Power-BI-Tools

### Project Overview
Objective: The goal of the project is to detect depressivness based on different features, e.g., gender, bmi, depression severity etc.

Context: Based on the research data-set, which is given on [Kaggle: Depression and anxiety data ](https://www.kaggle.com/datasets/shahzadahmad0402/depression-and-anxiety-data), we developped a classification model to identify depressivness related distinctive symptoms, e.g., feelings of melancholy and emptiness, feelings of worry and disturbed sleep, as well as a general loss of initiative and interest in activities. We have to clean the dataset and find the correlations of the different features to predict such depressivness. Difficulties are to detect the correct features, which gave a good overview to the predit such a paramteter. We also saw, based on the data-set, that we also have a relation to suicidal and consider such a behaviour in our ML-methods.

Significance: It is important for parents, teachers, psycholicist to detect in an early stage such relations to depressiveness to start on an early stage a therapy. The benefit of the research allow us with a simple model based on the features: gender, phq_score (measure of the severity of symptoms, which are related to depression) and gad_score (measure, thatwe have a relation of the severity of generalized anxiety disorder) to detect a depressivness, see also the ideas in [Kaggle: Machine_learningproject](https://www.kaggle.com/code/geovaniwoll/machine-learningproject). Furthermore, we generalise the model to full modell with all the features in the dataset and could improve the prediction of such a simpler model.


Goal: The aim of th project was to improve standard models, we also consider a simple app to apply the ML-predictor.

## Team Members

- Team Member 1: [Jürgen Geiser](https://github.com/juergen-geiser)
- Team Member 2: [Carsten Henkel](https://github.com/xxx)
- Team Member 3: [Alex Gafran](https://github.com/xxx)
- Team Member 4: [Marcin Grzymowicz](https://github.com/xxx)

## Jupyter Notebooks

This project consists of different Jupyter Notebooks that serve different purposes:

1. **simple_model_depression.ipynb**: 
This notebook focuses on a simple classification of the depressiveness with 3 columns (features) and could be used as a first predictve tool. It is done a simple Exploratory Data Analysis (EDA) and training with a logistic regression model. 

2. **interface_simple_ML_GUI.ipynb**: 
This notebook focuses on an interface between the ML part given in the simple_model_depression.ipynb file and the GUI-interface. The file: model.pkl has to be loaded, here are stored all the simple classification of the depressiveness with 3 columns (features), that could be used as a first predictve tool. It is done a simple Exploratory Data Analysis (EDA) and training with a logistic regression model. 

3. **multiple_simple_model_depression.ipynb**: 
This notebook focuses on a simple classification, but we apply 4 different targets: 'anxiousness', 'depressiveness', 'treatment_status', 'suicidal'. All the 4 different targets ar trained with different features, in a first approach, we deal only with the numerical features. The 4 models are trained with a logistic regression model and stored in the pickle file: models.pkl. 

4. **interface_multiple_simple_ML_GUI.ipynb**: 
This notebook focuses on an interface between the ML part given in the multiple_simple_model_depression.ipynb file and the GUI-interface. The file: models.pkl has to be loaded, here are stored all the 4 models of the multiple simple classification with the 4 different targets and the related features, that could be used as a first multiple predictve tool. 

More detailed models (Detailed EDA and detailed models with Gridsearch)

5. **eda_model_depression.ipynb**: 
This notebook focuses on a complex classification of the depressiveness with all columns (features) and could be used as an improved predictve tool for the target: "depressiveness". It is done with RandomForest and gridsearch to improve the classification. We result in a prediction model of the best 10 feature-columns.

6. **interface_eda_model_depression_ML_GUI.ipynb**: 
This notebook focuses on an interface between the ML part given in the eda_model_depression.ipynb file and the GUI-interface. The file: model_depression.pkl has to be loaded, here are stored all the best model with the target "depressiveness" and we also gave the target and the names of the features, that could be used as a first multiple predictve tool. 


5. **method_model_depression.ipynb**: 
This notebook focuses on all possible models, e.g., decision tree, KNN, logistic regression, random forest, which are tested, we apply the results of the EDA in previous notebooks and concentrate on the important features. We could derive and optimal model, which is stored in best_model_depression.pkl, this can be used for the interface GUI or for the notebook interface_eda_model_depression_ML_GUI.ipynb.




## Installation and Setup

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
4. Download the modified dataset and place it in the project directory. The original dataset can be acquired from the link [Kaggle: Depression and anxiety data ](https://www.kaggle.com/datasets/shahzadahmad0402/depression-and-anxiety-data).


**Note:** If any of the above files are missing, the corresponding functionality may not work as expected.

Once the setup is complete, you start the juypter-Notebook and you can make predictions on new data using the data-file: aim_test.csv.
