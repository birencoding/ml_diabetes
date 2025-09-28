import pickle
import streamlit as st


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# page title
st.title('Diabetes Prediction using ML')

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.number_input("Number of Pregnancies",
    min_value=0,
    max_value=20,
    value=0,
    step=1,
    placeholder="Enter a number between 0 and 20")
    
with col2:
    Glucose = st.number_input('Glucose Level',
    min_value=0,
    max_value=200,
    value=0,
    step=1,
    placeholder="Enter a number between 0 and 200")

with col3:
    BloodPressure = st.number_input('Blood Pressure value',
    min_value=0,
    max_value=200,
    value=0,
    step=1,
    placeholder="Enter a number between 0 and 200")

with col1:
    SkinThickness = st.number_input('Skin Thickness value',
    min_value=0,
    max_value=200,
    value=0,
    step=1,
    placeholder="Enter a number between 0 and 200")

with col2:
    Insulin = st.number_input('Insulin Level',
    min_value=0,
    max_value=1000,
    value=0,
    step=1,
    placeholder="Enter a number between 0 and 1000")

with col3:
    BMI = st.number_input('BMI value',
    min_value=0,
    max_value=100,
    value=0,
    step=1,
    placeholder="Enter a number between 0 and 100")
    

with col1:
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value',
    min_value=0,
    max_value=5,
    value=0,
    step=1,
    placeholder="Enter a number between 0 and 5")

with col2:
    Age = st.number_input('Age of the Person',
    min_value=1,
    max_value=120,
    value=1,
    step=1,
    placeholder="Enter a number between 1 and 120")


# code for Prediction
diab_diagnosis = ''

# creating a button for Prediction

if st.button('Diabetes Test Result'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if (diab_prediction[0] == 1):
        diab_diagnosis = 'The person has diabetic'
    else:
        diab_diagnosis = 'The person does not have diabetic'
if diab_diagnosis:
    st.success(diab_diagnosis)
