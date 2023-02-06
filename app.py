import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import pandas as pd

lung_model = pickle.load(open('lung_model.pkl', 'rb'))
stroke_model = pickle.load(open('stroke_model.pkl', 'rb'))


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction',
                           ['Lung Cancer Prediction',
                            'Stroke Prediction'],
                           default_index=0)

if selected == 'Lung Cancer Prediction':
    st.title('Lung Cancer Prediction')
    col1,  col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox('Your Gender', ['Male', 'Female'])
    with col2:
        age = st.number_input('Enter Your Age')
    with col3:
        smoking = st.selectbox('Do You Smoke', ['Yes', 'No'])
    with col1:
        yellow_finger = st.selectbox('Is Your Finger Yellow', ['Yes', 'No'])
    with col2:
        anxiety = st.selectbox('Do You feeling Anxiety', ['Yes', 'No'])
    with col3:
        peer_pressure = st.selectbox('Do You feel Peer Pressure', ['Yes', 'No'])
    with col1:
        chronic_disease = st.selectbox('Do you Have any Chronic Disease', ['Yes', 'No'])
    with col2:
        fatigue = st.selectbox('Do you feel Fatigue', ['Yes', 'No'])
    with col3:
        allergy = st.selectbox('Do you have any allergy', ['Yes', 'No'])
    with col1:
        wheezing = st.selectbox('Do you Wheeze', ['Yes', 'No'])
    with col2:
        alcohol = st.selectbox('Do You Drink Alcohol', ['Yes', 'No'])
    with col3:
        cough = st.selectbox('Dou You Cough', ['Yes', 'No'])
    with col1:
        short_breath = st.selectbox('Do You Have shortness of Breath', ['Yes', 'No'])
    with col2:
        swallowing = st.selectbox('Do You have Swallowing Difficulty', ['Yes', 'No'])
    with col3:
        chest_pain =st.selectbox('Do You have Chest Pain', ['Yes', 'No'])

    input_df = (pd.DataFrame({'GENDER': gender, 'AGE': age, 'SMOKING': smoking, 'YELLOW_FINGERS': yellow_finger,
                             'ANXIETY': anxiety,
                            'PEER_PRESSURE': peer_pressure,
                            'CHRONIC DISEASE': chronic_disease, 'FATIGUE ': fatigue, 'ALLERGY ':allergy, 'WHEEZING': wheezing,
                            'ALCOHOL CONSUMING': alcohol, 'COUGHING': cough,
                             'SHORTNESS OF BREATH': short_breath, 'SWALLOWING DIFFICULTY': swallowing, 'CHEST PAIN':
                                 chest_pain}, index=[0]))
    input_df['GENDER'] = input_df['GENDER'].map({'Male': 1, 'Female': 0})
    input_df = input_df.replace({'Yes': 1, 'No': 0})
    # Here I changed the Yes to 1 and No to 0
    if st.button('Predict of Lung Cancer'):
        if age == 0.00:
            st.success('Please full Details Correctly')
        else:
            result = lung_model.predict(input_df)
            if result[0] == 'YES':
                st.success('You have chance of Lung Cancer. Please Take care of Yourself and Consult you Doctor '
                           'Immediately')
            if result[0] == 'NO':
                st.success('Congratulation 🥳 You have No chance of Lung Cancer But Take care of Yourself')



if selected == 'Stroke Prediction':
    st.title('Stroke Prediction')

    col1,  col2, col3 = st.columns(3)
    with col1:
        gender2 = st.selectbox('Your Gender', ['Male', 'Female'])
    with col2:
        age2 = st.number_input('Enter Your Age')
    with col3:
        hypertension = st.selectbox('Do You have Hypertension', ['Yes', 'No'])
    with col1:
        heart_disease = st.selectbox('Do You have any Heart Disease', ['Yes', 'No'])
    with col2:
        ever_married = st.selectbox('Are You Married', ['Yes', 'No'])
    with col3:
        work_type = st.selectbox('What is Type of Your Work', ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
    with col1:
        residence_type = st.selectbox('Where Do You Live', ['Urban', 'Rural'])
    with col2:
        avg_glucose_level = st.number_input('Average Glucose Level')
    with col3:
        bmi = st.number_input('Type Your BMI')
    with col1:
        smoking_status = st.selectbox('What is Your Smoking Type', ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])
    input_df2 = pd.DataFrame({'gender': gender2, 'age': age2, 'hypertension': hypertension, 'heart_disease':
        heart_disease,
                 'ever_married': ever_married, 'work_type': work_type, 'Residence_type': residence_type,
                 'avg_glucose_level': avg_glucose_level, 'bmi': bmi, 'smoking_status': smoking_status}, index = [0])
    input_df2['hypertension'] = input_df2['hypertension'].map({'Yes': 1, 'No': 0})
    input_df2['heart_disease'] = input_df2['heart_disease'].map({'Yes': 1, 'No': 0})
    if st.button('Predict of Stroke'):
        if age2 == 0.00 or avg_glucose_level == 0.00 or bmi ==0.00:
            st.success('Please Enter full Details Correctly')
        else:

            prediction = stroke_model.predict(input_df2)
            if prediction[0] == 1:
                st.success('You have chance of Stroke. Please Take care of Yourself and Consult Your Doctor Immediately')
            else:
                st.success("Congratulation🥳 You don't have Chance of Stroke but Take care of Yourself")