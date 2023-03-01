import pickle 
import streamlit as st
from streamlit_option_menu import option_menu 

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/ajay/Desktop/mlwebapp/saved models/diabetes_model.sav','rb'))
heart_model = pickle.load(open('C:/Users/ajay/Desktop/mlwebapp/saved models/heart_model.sav','rb'))
parkinsons_model = pickle.load(open('C:/Users/ajay/Desktop/mlwebapp/saved models/parkinsons_model.sav','rb'))


# creating a sidebar for navigation 

with st.sidebar:
    selected = option_menu(
        menu_title="Multiple Disease Prediction With Machine Learning",
        options=['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
        icons=['activity','heart-fill','person-fill'],
        default_index=0
    )

if selected == 'Diabetes Prediction':
    st.title("Diabetes Disease Data")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancy = st.text_input("NUMBER OF PREGNANCY")
    with col2:
        Glucose = st.text_input("GLUCOSE")
    with col3:
        BloodPressure = st.text_input("BLOOD PRESSURE")
    with col1:
        SkinThickness = st.text_input("SKIN THICKNESS")
    with col2:
        Insulin = st.text_input("INSULIN")
    with col3:
        BMI = st.text_input("BODY MASS INDEX")
    with col1:
        DiabetesPedigreeFunction = st.text_input("DIABETES PEDIGREE FUNCTION")
    with col2:
        Age = st.text_input("AGE OF PERSON")

    # code for prediction 
    diab_dignosis = ''

    # creating a button
    if st.button('TEST RESULT'):
        diab_prediction = diabetes_model.predict([[Pregnancy,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (diab_prediction[0]==0):
            diab_dignosis = 'NOT DIABETIC'
        else:
            diab_dignosis = 'DIABETIC'
    st.success(diab_dignosis)


if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Data")

    col1,col2,col3 = st.columns(3)

    with col1:
        age = st.text_input("AGE OF PERSON")
    with col2:
        sex = st.text_input("SEX OF PERSON (WRITE IN 1 OR 0)")
    with col3:
        Cp = st.text_input("CHEST PAIN")
    with col1:
        TrestBps = st.text_input("TRESTBPS")
    with col2:
        Chol = st.text_input("CHOL")
    with col3:
        Fbs = st.text_input("FBS")
    with col1:
        restecg	= st.text_input("RESTECG")
    with col2:
        thalach = st.text_input("THALACH")
    with col3:
        exang = st.text_input("EXANG")
    with col1:
        oldpeak = st.text_input("OLD PEAK")
    with col2:
        slope = st.text_input("SLOPE")
    with col3:
        Ca = st.text_input("CA")
    with col1:
        Thal = st.text_input("THAL")


    heart_diagnosis = ''

    if st.button('TEST RESULT'):
       heart_prediction = heart_model.predict([[age,sex,Cp,TrestBps,Chol,Fbs,restecg,thalach,exang,oldpeak,slope,Ca,Thal]],)
       if (heart_prediction[0]==0):
           heart_diagnosis = 'NO HEART DISEASE'
       else:
           heart_diagnosis = 'HEART DISEASE'
    st.success(heart_diagnosis)


if selected == 'Parkinsons Prediction':
    st.title("Parkinsons Disease Data")

    col1,col2,col3 = st.columns(3) 

    with col1:
        fo = st.text_input("Average vocal fundamental frequency")
    with col2:
        fhi = st.text_input(" Maximum vocal fundamental frequency")
    with col3:
        flo = st.text_input("Minimum vocal fundamental frequency")
    with col1:
        Jitter = st.text_input("MDVP:Jitter(%)")
    with col2:
        ABS  = st.text_input(" MDVP:Jitter(Abs)")
    with col3:
        RAP = st.text_input("MDVP RAP")
    with col1:
        PPQ = st.text_input(" MDVP PPQ")
    with col2:
        DDP = st.text_input("Jitter DDP")
    with col3:
        Shimmer = st.text_input("MDVP Shimmer")
    with col1:
        shimmer_db = st.text_input("MDVP Shimmer(dB)")
    with col2:
        APQ3 = st.text_input("Shimmer APQ3")
    with col3:
        APQ5 = st.text_input("Shimmer APQ5") 
    with col1:
        APQ = st.text_input("MDVP APQ")
    with col2:
        DDA = st.text_input("Shimmer DDA")
    with col3:
        NHR = st.text_input("N H R")
    with col1:
        HNR = st.text_input("H N R")
    with col2:
        RPDE = st.text_input("R P D E")
    with col3:
        DFA = st.text_input("Signal fractal scaling exponent")
    with col1:
        spread1 = st.text_input("SPREAD 1")
    with col2:
        spread2 = st.text_input("SPREAD 2")
    with col3:
        D2 = st.text_input("nonlinear dynamical complexity measures")
    with col1:
        PPE = st.text_input("nonlinear measures of fundamental frequency variation")

    parkinsons_dignosis = ''

    if st.button('TEST RESULT'):
          parkinsons_prediction = parkinsons_model.predict([[fo,fhi,flo,Jitter,ABS,RAP,PPQ,DDP,Shimmer,shimmer_db,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
          if (parkinsons_prediction[0]==0):
              parkinsons_dignosis = "NEGATIVE"
          else: 
              parkinsons_dignosis = "POSITIVE"
    st.success(parkinsons_dignosis)



    



