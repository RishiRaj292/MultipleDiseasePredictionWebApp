# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:35:56 2024

@author: Nidhi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#now loading the saved models
diabetes_model=pickle.load(open('C:\\Users\\Nidhi\\OneDrive\\Desktop\\MultipleDiseasePredictionSystem\\diabetes_model.sav','rb'))
#
parkinsons_model=pickle.load(open('C:\\Users\\Nidhi\\OneDrive\\Desktop\\MultipleDiseasePredictionSystem\\parkinsons_model.sav','rb'))

heartdisease_model=pickle.load(open('C:\\Users\\Nidhi\\OneDrive\\Desktop\\MultipleDiseasePredictionSystem\\heart_disease_model.sav','rb'))

breastcancer_model=pickle.load(open('C:\\Users\\Nidhi\\OneDrive\\Desktop\\MultipleDiseasePredictionSystem\\breastcancer.sav','rb'))


with st.sidebar:
    #main title and titles for different web pages
    selected=option_menu('Multiple Diseases Prediction System',['Prediction For Diabetes','Prediction For Heart Disease',"Prediction For Parkinson's Disease","Prediction For Breast Cancer"],
                         default_index=0)

#default_index=0 means it stays at diabetes prediction page first as that is the first element of the list


#diabetes prediction page
if (selected=="Prediction For Diabetes"):
    #page title is-
    st.title("Prediction Of Diabetes Using Machine Learning")
    
    #input from user , using text_input method of streamlit and more-
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


   # code for Prediction
    diab_diagnosis = ''

   # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                     BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
           diab_diagnosis = 'The person is diabetic.'
        else:
           diab_diagnosis = 'The person is not diabetic.'

    st.success(diab_diagnosis)
    
#heart disease prediction page
if (selected=="Prediction For Heart Disease"):
    #page title is-
    st.title("Prediction Of Heart Disease Using Machine Learning")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex:(1 = male, 0 = female)')

    with col3:
        cp = st.text_input('Chest Pain types: 1 or 2 or 3 or 4')#chest pain is cp , of 4 types
   
    with col1:
        trestbps = st.text_input('Resting Blood Pressure(in mm Hg on admission to the hospital)')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results(0 or 1)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina(1=yes,0=no)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise(values between 0 to 6.2')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment(any number)')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy(0 or 1 or more')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heartdisease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

    

#parkinson's disease prediction page
if(selected=="Prediction For Parkinson's Disease"):
    #page title is-
    st.title("Prediction For Parkinson's Disease Using Machine Learning")
    
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP(0.1% to 0.5%')

    with col2:
        PPQ = st.text_input('MDVP:PPQ(0.1% to 0.7%)')

    with col3:
        DDP = st.text_input('Jitter:DDP(Three times the RAP value')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer(0.1% to 3%)')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3(0.5% to 3%)')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5(0.5% to 4%)')

    with col3:
        APQ = st.text_input('MDVP:APQ(0.5% to 3%)')

    with col4:
        DDA = st.text_input('Shimmer:DDA(three times the APQ3 value)')

    with col5:
        NHR = st.text_input('NHR(0.01 to 0.3)')

    with col1:
        HNR = st.text_input('HNR(8 to 30 dB)')

    with col2:
        RPDE = st.text_input('RPDE(0.2 to 0.7)')

    with col3:
        DFA = st.text_input('DFA(0.5 to 1.2)')

    with col4:
        spread1 = st.text_input('spread1( ranging from -7 to -2)')

    with col5:
        spread2 = st.text_input('spread2(0.1 to 0.5)')

    with col1:
        D2 = st.text_input('D2(1.5 to 3.0)')

    with col2:
        PPE = st.text_input('PPE( 0.1 to 0.6)')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

#breast cancer detection page-
if(selected=="Prediction For Breast Cancer"):
    #page title is-
    st.title("Prediction Of Breast Cancer Using Machine Learning")
    
    col1 , col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        mr= st.text_input("Mean Radius(in mm)")
        
    with col2:    
        mt = st.text_input('Mean Texture')

    with col3:
        mp = st.text_input('Mean Perimeter')

    with col4:
        ma = st.text_input('Mean Area')

    with col5:
        ms= st.text_input('Mean Smoothness')

    with col1:
        mc = st.text_input('Mean Compactness')

    with col1:
        mcc = st.text_input('Mean Concavity')
        ae = st.text_input('Area Error')
        wr = st.text_input('Worst Radius')
        wcp = st.text_input('Worst Concave Points')
        wf = st.text_input('Worst Fractal Dimension')

    with col2:
        mcp = st.text_input('Mean Concave Points')
        se = st.text_input('Smoothness Error')
        wt = st.text_input('Worst Texture')
        wsy = st.text_input('Worst Symmetry')

    with col3:
        mcs = st.text_input('Mean Symmetry')
        ce = st.text_input('Compactness Error')
        wp = st.text_input('Worst Perimeter')
        wcon = st.text_input('Worst Concavity')
    
    with col4:
        mcf = st.text_input('Mean Fractal Dimension')
        cce = st.text_input('Concavity Error')
        wa = st.text_input('Worst Area')
        wc = st.text_input('Worst Compactness')
    
    with col5:
        re = st.text_input('Radius Error')
        cpe = st.text_input('Concave Points Error')
        te = st.text_input('Texture Error')
        pe = st.text_input('Perimeter Error')
        sye = st.text_input('Symmetry Error')
        fde = st.text_input('Fractal Dimension Error')
        ws = st.text_input('Worst Smoothness')

    # code for Prediction
    breastcancer_diagnosis = ''
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):

        user_input = [mr,mt,mp,ma,ms,mc,mcc,ae,wr,wcp,wf,mcp,se,wt,wsy,mcs,ce,wp,wcon,mcf,cce,wa,wc,re,cpe,te,pe,sye,fde,ws]

        user_input = [float(x) for x in user_input]

        breastcancer_prediction = breastcancer_model.predict([user_input])

        if breastcancer_prediction[0] == 1:
            breastcancer_diagnosis = "The Cancer is benign"
        else:
            breastcancer_diagnosis = "The Cancer is malignant"

    st.success(breastcancer_diagnosis)


