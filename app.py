import joblib
import time
import streamlit as st
st.title("Welcome to Halmoni AI , (know your health)")
model = joblib.load("model.pkl")
gender  = st.number_input("Enter your gender::")
occup = st.number_input("Enter your occupation::")
avgwork = st.number_input("Enter your Avg work Hr daliy::")
avgrest = st.number_input("Enter your Avg rest hr During work::")
avgsleep = st.number_input("Enter your Avg daily Sleep Hr::")
avgex = st.number_input("Enter your Avg Exercise Min  daily::")
click =  st.button("Predict")
if click:
    with st.spinner("wait..",show_time=False):
        time.sleep(2)
        pred = model.predict([[gender,occup,avgwork,avgrest,avgsleep,avgex]])
        st.write("You will live::",pred)


import joblib
import time
import streamlit as st
st.title("Model will tell you how much water you should drink")
model_sec = joblib.load("model_sec.pkl")
Age_sec = st.number_input("Enter your Age::")
gender_sec  = st.number_input("Enter your gender::")
weight_sec = st.number_input("Enter your    weight::")
phyact_sec = st.number_input("Enter your physical activity daliy::")
weather_sec = st.number_input("Enter The weither Condition::")
click_sec =  st.button("Predict")
if click_sec:
    with st.spinner("wait..",show_time=False):
        time.sleep(2)
        pred_sec = model_sec.predict([[Age_sec,gender_sec,weight_sec,phyact_sec,weather_sec]])
        st.write("You water Intake Should be::",pred_sec , "liters")
        


import joblib
import time
import streamlit as st
st.title("Model that will tell your Addiction Score")
model_third = joblib.load("model_third.pkl")
age_third = st.number_input("Enter the age::")
gender_third  = st.number_input("Enter your gender::")
accd = st.number_input("Enter your Academic Leval::")
dailyavgusephone = st.number_input("Enter your Avg  daliy use of phone::")
mosusedplt = st.number_input("Enter your most used platform::")
acadicperform = st.number_input("It affects you studies?::")
sleeppernight = st.number_input("Enter how many Hr do you sleep Daily::")
realation = st.number_input("Enter are you in the RelationShip?")

click_third =  st.button("Predict")
if click_third:
    with st.spinner("wait..",show_time=False):
        time.sleep(2)
        pred_third = model_third.predict([[age_third,gender_third,accd,dailyavgusephone,mosusedplt,acadicperform,sleeppernight,
                                     realation]])
        st.write("This is your Addiction Scorem out of 9::",pred_third)
        

        
