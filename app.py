import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, MARITAL_STATUS, APPLICATION_MODE, COURSE, DAYTIME_EVENING_ATTENDANCE, PREVIOUS_QUALIFICATION, NACIONALITY, QUALIFICATION, OCCUPATION, DISPLACED, EDUCATIONAL_SPECIAL_NEEDS, DEBTOR, TUITION_FEES_UP_TO_DATE, GENDER, SCHOLARSHIP_HOLDER, INTERNATIONAL
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Student Performance App (Prototype)')

data = pd.DataFrame()

col1, col2 = st.columns([1,3])
 
with col1:
    Marital_status = st.selectbox(label='Marital_status', options=MARITAL_STATUS, index=0)
    data["Marital_status"] = [Marital_status]

with col2:
    Application_mode = st.selectbox(label='Application_mode', options=APPLICATION_MODE, index=0)
    data["Application_mode"] = [Application_mode]

col1, col2 = st.columns([4,3])
 
with col1:
    Course = st.selectbox(label='Course', options=COURSE, index=11)
    data["Course"] = [Course]

with col2:
    Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=DAYTIME_EVENING_ATTENDANCE, index=1)
    data["Daytime_evening_attendance"] = [Daytime_evening_attendance]


col1, col2 = st.columns([4,3])
 
with col1:
    Previous_qualification = st.selectbox(label='Previous_qualification', options=PREVIOUS_QUALIFICATION, index=0)
    data["Previous_qualification"] = [Previous_qualification]

with col2:
    Nacionality = st.selectbox(label='Nacionality', options=NACIONALITY, index=0)
    data["Nacionality"] = [Nacionality]

col1, col2 = st.columns(2)
 
with col1:
    Mothers_qualification = st.selectbox(label='Mothers_qualification', options=QUALIFICATION, index=0)
    data["Mothers_qualification"] = [Mothers_qualification]

with col2:
    Mothers_occupation = st.selectbox(label='Mothers_occupation', options=OCCUPATION, index=0)
    data["Mothers_occupation"] = [Mothers_occupation]

col1, col2 = st.columns(2)
 
with col1:
    Fathers_qualification = st.selectbox(label='Fathers_qualification', options=QUALIFICATION, index=1)
    data["Fathers_qualification"] = [Fathers_qualification]

with col2:
    Fathers_occupation = st.selectbox(label='Fathers_occupation', options=OCCUPATION, index=1)
    data["Fathers_occupation"] = [Fathers_occupation]

col1, col2, col3, col4 = st.columns(4)
with col1:
    Displaced = st.selectbox(label='Displaced', options=DISPLACED, index=1)
    data["Displaced"] = [Displaced]

with col2:
    Educational_special_needs = st.selectbox(label='Educational_special_needs', options=EDUCATIONAL_SPECIAL_NEEDS, index=1)
    data["Educational_special_needs"] = [Educational_special_needs]

with col3:
    Debtor = st.selectbox(label='Debtor', options=DEBTOR, index=1)
    data["Debtor"] = [Debtor]

with col4:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition_fees_up_to_date', options=TUITION_FEES_UP_TO_DATE, index=1)
    data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]

col1, col2, col3 = st.columns(3)
with col1:
    Gender = st.selectbox(label='Gender', options=GENDER, index=1)
    data["Gender"] = [Gender]

with col2:
    Scholarship_holder = st.selectbox(label='Scholarship_holder', options=SCHOLARSHIP_HOLDER, index=1)
    data["Scholarship_holder"] = [Scholarship_holder]

with col3:
    International = st.selectbox(label='International', options=INTERNATIONAL, index=1)
    data["International"] = [International]

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Application_order = int(st.number_input(label='Application_order', value=2))
    data["Application_order"] = Application_order
 
with col2:
    Previous_qualification_grade = int(st.number_input(label='Previous_qualification_grade', value=135))
    data["Previous_qualification_grade"] = Previous_qualification_grade
 
with col3:
    Admission_grade = int(st.number_input(label='Admission_grade', value=125))
    data["Admission_grade"] = Admission_grade
 
with col4:
    Age_at_enrollment = float(st.number_input(label='Age_at_enrollment', value=20))
    data["Age_at_enrollment"] = Age_at_enrollment
 
col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Curricular_units_1st_sem_credited = float(st.number_input(label='Curricular_units_1st_sem_credited', value=5))
    data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited
 
with col2:
    Curricular_units_1st_sem_enrolled = float(st.number_input(label='Curricular_units_1st_sem_enrolled', value=8))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled
 
with col3:
    Curricular_units_1st_sem_evaluations = float(st.number_input(label='Curricular_units_1st_sem_evaluations', value=8))
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations
 
with col4:
    Curricular_units_1st_sem_approved = float(st.number_input(label='Curricular_units_1st_sem_approved', value=5))
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Curricular_units_1st_sem_grade = float(st.number_input(label='Curricular_units_1st_sem_grade', value=12))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade
 
with col2:
    Curricular_units_1st_sem_without_evaluations = float(st.number_input(label='Curricular_units_1st_sem_without_evaluations', value=2))
    data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations
 
with col3:
    Curricular_units_2nd_sem_credited = float(st.number_input(label='Curricular_units_2nd_sem_credited', value=5))
    data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited
 
with col4:
    Curricular_units_2nd_sem_enrolled = float(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=7))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled


col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Curricular_units_2nd_sem_evaluations = float(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=5))
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations
 
with col2:
    Curricular_units_2nd_sem_approved = float(st.number_input(label='Curricular_units_2nd_sem_approved', value=5))
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved
 
with col3:
    Curricular_units_2nd_sem_grade = float(st.number_input(label='Curricular_units_2nd_sem_grade', value=12))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade
 
with col4:
    Curricular_units_2nd_sem_without_evaluations = float(st.number_input(label='Curricular_units_2nd_sem_without_evaluations', value=2))
    data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations

col1, col2, col3 = st.columns(3)
 
with col1:
    Unemployment_rate = float(st.number_input(label='Unemployment_rate', value=11))
    data["Unemployment_rate"] = Unemployment_rate
 
with col2:
    Inflation_rate = float(st.number_input(label='Inflation_rate', value=1.3))
    data["Inflation_rate"] = Inflation_rate
 
with col3:
    GDP = float(st.number_input(label='GDP', value=0.2))
    data["GDP"] = GDP


if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Student Performance: {}".format(prediction(new_data)))

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)