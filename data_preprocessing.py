import joblib
import numpy as np
import pandas as pd

pca_1 = joblib.load("./model/pca_1.joblib")
scaler_application_order = joblib.load('./model/scaler_Application_order.joblib')
scaler_previous_qualification_grade = joblib.load('./model/scaler_Previous_qualification_grade.joblib')
scaler_admission_grade = joblib.load('./model/scaler_Admission_grade.joblib')
scaler_age_at_enrollment = joblib.load('./model/scaler_Age_at_enrollment.joblib')
scaler_curricular_units_1st_sem_credited = joblib.load('./model/scaler_Curricular_units_1st_sem_credited.joblib')
scaler_curricular_units_1st_sem_enrolled = joblib.load('./model/scaler_Curricular_units_1st_sem_enrolled.joblib')
scaler_curricular_units_1st_sem_evaluations = joblib.load('./model/scaler_Curricular_units_1st_sem_evaluations.joblib')
scaler_curricular_units_1st_sem_approved = joblib.load('./model/scaler_Curricular_units_1st_sem_approved.joblib')
scaler_curricular_units_1st_sem_grade = joblib.load('./model/scaler_Curricular_units_1st_sem_grade.joblib')
scaler_curricular_units_1st_sem_without_evaluations = joblib.load('./model/scaler_Curricular_units_1st_sem_without_evaluations.joblib')
scaler_curricular_units_2nd_sem_credited = joblib.load('./model/scaler_Curricular_units_2nd_sem_credited.joblib')
scaler_curricular_units_2nd_sem_enrolled = joblib.load('./model/scaler_Curricular_units_2nd_sem_enrolled.joblib')
scaler_curricular_units_2nd_sem_evaluations = joblib.load('./model/scaler_Curricular_units_2nd_sem_evaluations.joblib')
scaler_curricular_units_2nd_sem_approved = joblib.load('./model/scaler_Curricular_units_2nd_sem_approved.joblib')
scaler_curricular_units_2nd_sem_grade = joblib.load('./model/scaler_Curricular_units_2nd_sem_grade.joblib')
scaler_curricular_units_2nd_sem_without_evaluations = joblib.load('./model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib')
scaler_unemployment_rate = joblib.load('./model/scaler_Unemployment_rate.joblib')
scaler_unemployment_rate = joblib.load('./model/scaler_Unemployment_rate.joblib')
scaler_inflation_rate = joblib.load('./model/scaler_Inflation_rate.joblib')
scaler_gdp = joblib.load('./model/scaler_GDP.joblib')

MARITAL_STATUS = {
    'Single': 1,
    'Married': 2,
    'Widower': 3,
    'Divorced': 4,
    'Facto Union': 5,
    'Legally Separated': 6
}

APPLICATION_MODE = {
    "1st phase - general contingent": 1,
    "Ordinance No. 612/93": 2,
    "1st phase - special contingent (Azores Island)": 5,
    "Holders of other higher courses": 7,
    "Ordinance No. 854-B/99": 10,
    "International student (bachelor)": 15,
    "1st phase - special contingent (Madeira Island)": 16,
    "2nd phase - general contingent": 17,
    "3rd phase - general contingent": 18,
    "Ordinance No. 533-A/99, item b2 (Different Plan)": 26,
    "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
    "Over 23 years old": 39,
    "Transfer": 42,
    "Change of course": 43,
    "Technological specialization diploma holders": 44,
    "Change of institution/course": 51,
    "Short cycle diploma holders": 53,
    "Change of institution/course (International)": 57
}

COURSE = {
    "Biofuel Production Technologies": 33,
    "Animation and Multimedia Design": 171,
    "Social Service (evening attendance)": 8014,
    "Agronomy": 9003,
    "Communication Design": 9070,
    "Veterinary Nursing": 9085,
    "Informatics Engineering": 9119,
    "Equinculture": 9130,
    "Management": 9147,
    "Social Service": 9238,
    "Tourism": 9254,
    "Nursing": 9500,
    "Oral Hygiene": 9556,
    "Advertising and Marketing Management": 9670,
    "Journalism and Communication": 9773,
    "Basic Education": 9853,
    "Management (evening attendance)": 9991
}

DAYTIME_EVENING_ATTENDANCE = {
    "Daytime": 1,
    "Evening": 0
}

PREVIOUS_QUALIFICATION = {
    "Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
    "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}

NACIONALITY = {
    "Portuguese": 1,
    "German": 2,
    "Spanish": 6,
    "Italian": 11,
    "Dutch": 13,
    "English": 14,
    "Lithuanian": 17,
    "Angolan": 21,
    "Cape Verdean": 22,
    "Guinean": 24,
    "Mozambican": 25,
    "Santomean": 26,
    "Turkish": 32,
    "Brazilian": 41,
    "Romanian": 62,
    "Moldova (Republic of)": 100,
    "Mexican": 101,
    "Ukrainian": 103,
    "Russian": 105,
    "Cuban": 108,
    "Colombian": 109,
}

QUALIFICATION = {
    "Secondary Education - 12th Year of Schooling or Eq.": 1,
    "Higher Education - Bachelor's Degree": 2,
    "Higher Education - Degree": 3,
    "Higher Education - Master's": 4,
    "Higher Education - Doctorate": 5,
    "Frequency of Higher Education": 6,
    "12th Year of Schooling - Not Completed": 9,
    "11th Year of Schooling - Not Completed": 10,
    "7th Year (Old)": 11,
    "Other - 11th Year of Schooling": 12,
    "10th Year of Schooling": 14,
    "General commerce course": 18,
    "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
    "Technical-professional course": 22,
    "7th year of schooling": 26,
    "2nd cycle of the general high school course": 27,
    "9th Year of Schooling - Not Completed": 29,
    "8th year of schooling": 30,
    "Unknown": 34,
    "Can't read or write": 35,
    "Can read without having a 4th year of schooling": 36,
    "Basic education 1st cycle (4th/5th year) or equiv.": 37,
    "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Specialized higher studies course": 41,
    "Professional higher technical course": 42,
    "Higher Education - Master (2nd cycle)": 43,
    "Higher Education - Doctorate (3rd cycle)": 44
}

OCCUPATION = {
    "Student": 0,
    "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2,
    "Intermediate Level Technicians and Professions": 3,
    "Administrative staff": 4,
    "Personal Services, Security and Safety Workers and Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
    "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Installation and Machine Operators and Assembly Workers": 8,
    "Unskilled Workers": 9,
    "Armed Forces Professions": 10,
    "Other Situation": 90,
    "(blank)": 99,
    "Health professionals": 122,
    "teachers": 123,
    "Specialists in information and communication technologies (ICT)": 125,
    "Intermediate level science and engineering technicians and professions": 131,
    "Technicians and professionals, of intermediate level of health": 132,
    "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
    "Office workers, secretaries in general and data processing operators": 141,
    "Data, accounting, statistical, financial services and registry-related operators": 143,
    "Other administrative support staff": 144,
    "personal service workers": 151,
    "sellers": 152,
    "Personal care workers and the like": 153,
    "Skilled construction workers and the like, except electricians": 171,
    "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like": 173,
    "Workers in food processing, woodworking, clothing and other industries and crafts": 175,
    "cleaning workers": 191,
    "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
    "Unskilled workers in extractive industry, construction, manufacturing and transport": 193,
    "Meal preparation assistants": 94
}

DISPLACED = {
    "Yes": 1,
    "No": 0
}

EDUCATIONAL_SPECIAL_NEEDS = {
    "Yes": 1,
    "No": 0
}

DEBTOR = {
    "Yes": 1,
    "No": 0
}

TUITION_FEES_UP_TO_DATE = {
    "Yes": 1,
    "No": 0
}

GENDER = {
    "Male": 1,
    "Female": 0
}

SCHOLARSHIP_HOLDER = {
    "Yes": 1,
    "No": 0
}

INTERNATIONAL = {
    "Yes": 1,
    "No": 0
}                                           

pca_numerical_columns = [
      'Curricular_units_1st_sem_credited',
      'Curricular_units_1st_sem_enrolled',
      'Curricular_units_1st_sem_evaluations',
      'Curricular_units_1st_sem_approved',
      'Curricular_units_1st_sem_grade',
      'Curricular_units_1st_sem_without_evaluations',
      'Curricular_units_2nd_sem_credited',
      'Curricular_units_2nd_sem_enrolled',
      'Curricular_units_2nd_sem_evaluations',
      'Curricular_units_2nd_sem_approved',
      'Curricular_units_2nd_sem_grade',
      'Curricular_units_2nd_sem_without_evaluations',
]

categorical_columns = [
    'Marital_status',
    'Application_mode',
    'Course',
    'Daytime_evening_attendance',
    'Previous_qualification',
    'Nacionality',
    'Mothers_qualification',
    'Fathers_qualification',
    'Mothers_occupation',
    'Fathers_occupation',
    'Displaced',
    'Educational_special_needs',
    'Debtor',
    'Tuition_fees_up_to_date',
    'Gender',
    'Scholarship_holder',
    'International',
]

def data_preprocessing(data):
    """Preprocessing data
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()

    df["Marital_status"] = data["Marital_status"].map(MARITAL_STATUS)
    df["Application_mode"] = data["Application_mode"].map(APPLICATION_MODE)
    df["Course"] = data["Course"].map(COURSE)
    df["Daytime_evening_attendance"] = data["Daytime_evening_attendance"].map(DAYTIME_EVENING_ATTENDANCE)
    df["Previous_qualification"] = data["Previous_qualification"].map(PREVIOUS_QUALIFICATION)
    df["Nacionality"] = data["Nacionality"].map(NACIONALITY)
    df["Mothers_qualification"] = data["Mothers_qualification"].map(QUALIFICATION)
    df["Mothers_occupation"] = data["Mothers_occupation"].map(OCCUPATION)
    df["Fathers_qualification"] = data["Fathers_qualification"].map(QUALIFICATION)
    df["Fathers_occupation"] = data["Fathers_occupation"].map(OCCUPATION)
    df["Displaced"] = data["Displaced"].map(DISPLACED)
    df["Educational_special_needs"] = data["Educational_special_needs"].map(EDUCATIONAL_SPECIAL_NEEDS)
    df["Debtor"] = data["Debtor"].map(DEBTOR)
    df["Tuition_fees_up_to_date"] = data["Tuition_fees_up_to_date"].map(TUITION_FEES_UP_TO_DATE)
    df["Gender"] = data["Gender"].map(GENDER)
    df["Scholarship_holder"] = data["Scholarship_holder"].map(SCHOLARSHIP_HOLDER)
    df["International"] = data["International"].map(INTERNATIONAL)
    
    df["Application_order"] = scaler_application_order.transform(np.asarray(data["Application_order"]).reshape(-1,1))[0]
    df["Previous_qualification_grade"] = scaler_previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1,1))[0]
    df["Admission_grade"] = scaler_admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1,1))[0]
    df["Age_at_enrollment"] = scaler_age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))[0]
    df["Unemployment_rate"] = scaler_unemployment_rate.transform(np.asarray(data["Unemployment_rate"]).reshape(-1,1))[0]
    df["Inflation_rate"] = scaler_inflation_rate.transform(np.asarray(data["Inflation_rate"]).reshape(-1,1))[0]
    df["GDP"] = scaler_gdp.transform(np.asarray(data["GDP"]).reshape(-1,1))[0]

    # PCA
    data["Curricular_units_1st_sem_credited"] = scaler_curricular_units_1st_sem_credited.transform(np.asarray(data["Curricular_units_1st_sem_credited"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_enrolled"] = scaler_curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_evaluations"] = scaler_curricular_units_1st_sem_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_approved"] = scaler_curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_grade"] = scaler_curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_without_evaluations"] = scaler_curricular_units_1st_sem_without_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_without_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_credited"] = scaler_curricular_units_2nd_sem_credited.transform(np.asarray(data["Curricular_units_2nd_sem_credited"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_enrolled"] = scaler_curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_evaluations"] = scaler_curricular_units_2nd_sem_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_approved"] = scaler_curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_grade"] = scaler_curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_without_evaluations"] = scaler_curricular_units_2nd_sem_without_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_without_evaluations"]).reshape(-1,1))[0]
    
    
    df[["pc1_1", "pc1_2", "pc1_3", "pc1_4"]] = pca_1.transform(data[pca_numerical_columns])
    
    return df