# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import time
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()


# loading the saved models

diabetes_model = pickle.load(open('saved models/finalized_model.sav', 'rb'))

heart_disease_model = pickle.load(open('saved models/newfinal_heart.sav','rb'))

parkinsons_model = pickle.load(open('saved models/parkinsons_model.sav', 'rb'))

liver_model = pickle.load(open('saved models/liver_model_new2.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction','Liver Disease Prediction' ],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
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
#         input_data=(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
#         input_data_as_numpy_array = np.asarray(input_data)

# #reshape array as we are predicting for one instance
#         input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# #standardize input data
#         std_data = scaler.fit_transform(input_data_reshaped)


#         diab_prediction = diabetes_model.predict(std_data)

        diab_prediction = diabetes_model.predict([[int(Pregnancies), int(Glucose), int(BloodPressure), int(SkinThickness), int(Insulin), float(BMI), float(DiabetesPedigreeFunction), int(Age)]])
        
        if (diab_prediction[0] == 0):
          diab_diagnosis = 'The person is not diabetic'
        else:
          diab_diagnosis = 'The person is diabetic'
        
    st.success(diab_diagnosis)
        



# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    # with col1:
    #     age = st.text_input('Age')
        
    # with col2:
    #     sex = st.text_input('Sex')
        
    # with col3:
    #     currentSmoker = st.text_input('Current Smoker or not')
        
    # with col1:
    #     cigsperDay = st.text_input('Cigarette amounts per day')
        
    # with col2:
    #     BPMeds = st.text_input('If the patient was on a BP medication')
        
    # with col3:
    #     prevalentStroke = st.text_input('Any previous strokes')
        
    # with col1:
    #     prevalentHyp = st.text_input('Hypertensive or not')
        
    # with col2:
    #     diabetes= st.text_input('Diabetic or not')
        
    # with col3:
    #     totChol = st.text_input('Total cholesterol level')
        
    # with col1:
    #     sysBP = st.text_input('Cystolic blood pressure')
        
    # with col2:
    #     diaBP = st.text_input('Diastolic blood pressure')
        
    # with col3:
    #     BMIn = st.text_input('Body Mass Index')
        
    # with col1:
    #     heartRate = st.text_input('Heart rate')
    
    # with col2:
    #     glucose = st.text_input('Glucose level')

    #new code -----------------------------------------------
      
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure(mm Hg)')
        
    with col2:
        chol = st.text_input('Serum Cholestrol(mg/dl)')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar>120mg/dl')
        
    with col1:
        restecg= st.text_input('Resting electrocardiographic result')
        
    with col2:
        thalach = st.text_input('Maximum heart rate achieved')
        
    with col3:
        exang = st.text_input('Exercise induced angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment                        .')
        
    with col3:
        ca = st.text_input('No of major vessels(0-4) colored by fluoroscpy')
    
    with col1:
        thal = st.text_input('thal')
     
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        # if age=='' or not age.isdigit():
        #     st.error("Age is invalid. Enter a valid age");
        # elif sex!='1' and sex!='0':
        #     st.error("Gender is invalid, Enter 1 for Male or 0 for Female");
        # elif currentSmoker!='1' and currentSmoker!='0':
        #     st.error("Current Smoker is invalid, Enter 1 for Yes or 0 for No");
        # elif cigsperDay=='' or not cigsperDay.isdigit():
        #     st.error("Cigarette Per Day value is invalid");
        # elif BPMeds!='1' and BPMeds!='0':
        #     st.error("Blood Pressure Medication Value is invalid, Enter 1 for Yes or 0 for No");
        # elif prevalentStroke!='1' and prevalentStroke!='0':
        #     st.error("Prevalent Stroke value is invalid, if patient had a previous stroke Enter 1, else 0");
        # elif prevalentHyp!='1' and prevalentHyp!='0':
        #     st.error("Hypertensive value is invalid, if patient was hypertensive Enter 1, else 0");
        # elif diabetes!='1' and diabetes!='0':
        #     st.error("Diabetes value is invalid, if patient has diabetes Enter 1, else 0");
        # elif totChol=='' or not totChol.isdigit():
        #     st.error("Total Cholesterol level  is invalid");
        # elif sysBP=='' or not sysBP.isdigit():
        #     st.error("Systolic Blood Pressure level is invalid");
        # elif diaBP=='' or diaBP.isalpha():
        #     st.error("Diastolic Blood Pressure level is invalid");
        # elif BMIn=='' or BMIn.isalpha():
        #     st.error("Body Mass Index value is invalid");
        # elif heartRate=='' or not heartRate.isdigit() or int(heartRate)>250 or int(heartRate)<25:
        #     st.error("Heart Rate value is invalid");
        # elif glucose=='' or not glucose.isdigit():
        #     st.error("Glucose level is invalid");
        if age=='' or not age.isdigit():
            st.error("Age is invalid. Enter a valid age");
        elif sex!='1' and sex!='0':
            st.error("Gender is invalid, Enter 1 for Male or 0 for Female");
        elif cp!='1' and cp!='2' and cp!='3' and cp!='0' :
            st.error("Chest Pain value is invalid, Enter 0 for 'Typical angina', Enter 1 for 'Atypical Angina', Enter 2 for 'Non-anginal Pain', Enter 3 for 'Asymptomatic'");
        elif trestbps=='' or trestbps.isalpha():
            st.error("Resting Blood Pressure value is invalid");
        elif chol=='' or chol.isalpha():
            st.error("Serum Cholestrol value is invalid");
        elif fbs!='1' and fbs!='0':
            st.error("Fasting Blood Sugar value is invalid, Enter 1 for True or Enter 0 for false ");
        elif restecg=='' or restecg.isalpha():
            st.error("Resting electrocardiographic result value is invalid, Enter 0 if normal and Enter 1 for Having ST-T");
        elif thalach=='' or restecg.isalpha():
            st.error("Maximum heart rate achieved value is invalid");
        elif exang!='0' and exang!='1':
            st.error("Exercise induced angina value is invalid, Enter 1 for Yes and Enter 0 for No");
        elif oldpeak=='' or oldpeak.isalpha():
            st.error("oldpeak level is invalid");
        elif slope!='0' and slope!='1' and slope!='2':
            st.error("slope value is invalid, Enter 0 for unsloping and Enter 1 for flat and Enter 2 for downsloping");
        elif ca!='0' and ca!='1' and ca!='2' and ca!='3' and ca!='4':
            st.error("No of major vessels(0-4) colored by fluoroscpy value is invalid");
        elif thal!='0' and thal!='1' and thal!='2' and thal!='3':
            st.error("thal value is invalid");
        else:  

        # Once the progress bar animation is complete, display the result
            heart_prediction=heart_disease_model.predict([[int(age),int(sex),int(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),float(slope),int(ca),int(thal)]])     
            # Define the endpoints for the bar graph
            happy_end = u"\U0001F603"  # Smiling face emoji
            sad_end = u"\U0001F614"  # Pensive face emoji
        
        #define the colors for the bar graph
            green_color = '#00cc96'
            red_color = '#ef5350'
        
        #define the animation function
            def animate_bar_graph(heart_prediction):
                with st.spinner('Processing...'):
                    time.sleep(2)
                    # ADD ANY ANIMATION OR PRINT CODE BELOW THIS
                    if heart_prediction[0] == 0:
                        bar_color = green_color
                        bar_width = 0.2
                        end_point = happy_end
                        heart_diagnosis = "The person has no heart disease"
                        st.success(f'{heart_diagnosis} {end_point}')
                    else:
                        bar_color = red_color
                        bar_width = 500
                        end_point = sad_end
                        heart_diagnosis = "The person has heart disease"
                        st.error(f'{heart_diagnosis} {end_point}')
                
               
                
                #st.write(f'<div style="background-color: {bar_color}; height: 50px; width: { bar_width}px;"></div>', unsafe_allow_html=True)
        
        #call the function with the heart_prediction variable
            animate_bar_graph(heart_prediction)
        

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
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
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        if fo=='' or not fo.isdigit():
            st.error("fo Value is invalid");
        elif fhi=='' or not fhi.isdigit():
            st.error("fhi Value is invalid");
        elif flo=='' or not flo.isdigit():
            st.error("flo Value is invalid");
        elif Jitter_percent=='' or not Jitter_percent.isdigit():
            st.error("Jitter_percen Value is invalid");
        elif Jitter_Abs=='' or not Jitter_Abs.isdigit():
            st.error("Jitter_Abs Value is invalid");
        elif RAP=='' or not RAP.isdigit():
            st.error("RAP level is invalid");
        elif PPQ =='' or not PPQ .isdigit():
            st.error("PPQ level is invalid");
        elif DDP=='' or not DDP.isdigit():
            st.error("DDP level is invalid");
        elif Shimmer_dB=='' or not Shimmer_dB.isdigit():
            st.error("Shimmer_dB level is invalid");
        elif APQ3=='' or not APQ3.isdigit():
            st.error("APQ3 is invalid");
        elif APQ5=='' or not APQ5.isdigit():
            st.error("APQ5 is invalid");
        elif APQ=='' or not APQ.isdigit():
            st.error("APQ is invalid");
        elif DDA=='' or not DDA.isdigit():
            st.error("DDA is invalid");
        elif NHR=='' or not NHR.isdigit():
            st.error("NHR is invalid");
        elif HNR=='' or not HNR.isdigit():
            st.error("HNR is invalid");
        elif RPDE=='' or not RPDE.isdigit():
            st.error("RPDE is invalid");
        elif DFA=='' or not DFA.isdigit():
            st.error("DFA is invalid");
        elif spread1=='' or not spread1.isdigit():
            st.error("spread1 is invalid");
        elif spread2=='' or not spread2.isdigit():
            st.error("APQ3 is invalid");
        elif D2=='' or not D2.isdigit():
            st.error("D2 is invalid");
        elif PPE=='' or not PPE.isdigit():
            st.error("PPE is invalid");
        else:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
            
            happy_end = u"\U0001F603"  # Smiling face emoji
            sad_end = u"\U0001F614"  # Pensive face emoji
            
            #define the colors for the bar graph
            green_color = '#00cc96'
            red_color = '#ef5350'
        
            #define the animation function
            def animate_bar_graph(parkinsons_prediction):
                with st.spinner('Processing...'):
                    time.sleep(2)
                    # ADD ANY ANIMATION OR PRINT CODE BELOW THIS
                    if parkinsons_prediction[0] == 0:
                        bar_color = green_color
                        bar_width = 0.2
                        end_point = happy_end
                        parkinsons_diagnosis = "The person has no parkinsons disease"
                        st.success(f'{parkinsons_diagnosis} {end_point}')
                    else:
                        bar_color = red_color
                        bar_width = 500
                        end_point = sad_end
                        parkinsons_diagnosis = "The person has parkinsons disease"
                        st.error(f'{parkinsons_diagnosis} {end_point}')
                
               
                
                #st.write(f'<div style="background-color: {bar_color}; height: 50px; width: { bar_width}px;"></div>', unsafe_allow_html=True)
        
        #call the function with the heart_prediction variable
            animate_bar_graph(parkinsons_prediction)
        

# Liver disease Prediction Page

if (selected == "Liver Disease Prediction"):
    
    # page title
    st.title("Liver Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        age_l = st.text_input('Age')
        
    with col2:
        gender_l = st.text_input('Gender')
        
    with col3:
        Bilirubin_l = st.text_input('Total_Bilirubin')
        
    with col4:
        Direct_l = st.text_input('Direct_Bilirubin	')
        
    with col5:
        Alkaline_l = st.text_input('AlkalinePhosphotase')
        
    with col1:
        Alamine_l = st.text_input('Alamine_Atf')
        
    with col2:
        Aspartate_l = st.text_input('Aspartate_Atf')
        
    with col3:
        Protiens_l = st.text_input('Total_Protiens')
        
    with col4:
        Albumin_l = st.text_input('Albumin')
        
    with col5:
        AnandG_l = st.text_input('AandG_Ratio')
        
  
  
    
    # code for Prediction
    Liverdiagnosis = ''
    
    # creating a button for Prediction    
    # if st.button("Liver Test Result"):
    #     Liverprediction = liver_model .predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB]])                          
        
    #     if (Liverprediction[0] == 1):
    #       Liverdiagnosis = "The person has Liver disease"
    #     else:
    #       Liverdiagnosis = "The person does not have Liver disease"
        
    # st.success(Liverdiagnosis)  
    #   
    if st.button('Liver Disease Test Result'):

        if age_l=='' or not age_l.isdigit():
            st.error("Age is invalid. Enter a valid age");
        elif gender_l!='1' and gender_l!='0':
            st.error("Gender is invalid, Enter 1 for Male or 2 for Female");
        elif Bilirubin_l=='' or Bilirubin_l.isalpha():
            st.error("Total_Bilirubin level is invalid");
        elif Direct_l=='' or Direct_l.isalpha():
            st.error("Direct_Bilirubin Value is invalid");
        elif Alkaline_l=='' or not Alkaline_l.isdigit():
            st.error("AlkalinePhosphotase level is invalid");
        elif Alamine_l=='' or not Alamine_l.isdigit():
            st.error("Alamine_Atf level is invalid");
        elif Aspartate_l=='' or not Aspartate_l.isdigit():
            st.error("Aspartate_Atf level is invalid");
        elif Protiens_l=='' or Protiens_l.isalpha():
            st.error("Total_Protiens level is invalid");
        elif Albumin_l=='' or Albumin_l.isalpha():
            st.error("Albumin level is invalid");
        elif AnandG_l=='' or AnandG_l.isalpha():
            st.error("AandG_Ratio is invalid");
        else:                     
        # Once the progress bar animation is complete, display the result
            Liverprediction = liver_model .predict([[int(age_l), int(gender_l), float(Bilirubin_l), float(Direct_l),int(Alkaline_l), int(Alamine_l), int(Aspartate_l),float(Protiens_l),float(Albumin_l),float(AnandG_l)]])
            # Define the endpoints for the bar graph
            happy_end = u"\U0001F603"  # Smiling face emoji
            sad_end = u"\U0001F614"  # Pensive face emoji

    # Define the colors for the bar graph
            green_color = '#00cc96'
            red_color = '#ef5350'

    # Define the animation function
            def animate_bar_graph(Liverprediction):
                with st.spinner('Processing...'):
                    time.sleep(2)
                    # ADD ANY ANIMATION OR PRINT CODE BELOW THIS
                    if Liverprediction[0] == 2:
                        bar_color = green_color
                        bar_width = 0.2
                        end_point = happy_end
                        Liverdiagnosis   = "The person has no Liver disease"
                        st.success(f'{Liverdiagnosis } {end_point}')
                    else:
                        bar_color = red_color
                        bar_width = 500
                        end_point = sad_end
                        Liverdiagnosis  = "The person has Liver disease"
                        st.error(f'{Liverdiagnosis  } {end_point}')
                
            
                
                #st.write(f'<div style="background-color: {bar_color}; height: 50px; width: { bar_width}px;"></div>', unsafe_allow_html=True)

    # Call the function with the heart_prediction variable
            animate_bar_graph(Liverprediction )
        


