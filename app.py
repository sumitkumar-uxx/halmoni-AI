import joblib
import time
import streamlit as st

st.title("Welcome to Halmoni AI , (know your health)")
st.title("This model will tell you how much years you will live--")
model = joblib.load("model.pkl")

gender_first = st.number_input("Enter your gender::", key="g1")
occup = st.number_input("Enter your occupation::", key="o1")
avgwork = st.number_input("Enter your Avg work Hr daliy::", key="w1")
avgrest = st.number_input("Enter your Avg rest hr During work::", key="r1")
avgsleep = st.number_input("Enter your Avg daily Sleep Hr::", key="s1")
avgex = st.number_input("Enter your Avg Exercise Min  daily::", key="e1")

click = st.button("Predict", key="b1")

if click:
    with st.spinner("wait..", show_time=False):
        time.sleep(2)
        pred = model.predict([[gender_first, occup, avgwork, avgrest, avgsleep, avgex]])
        st.write("You will live::", pred[0])


st.title("Model will tell you how much water you should drink")
model_sec = joblib.load("model_sec.pkl")

Age_sec = st.number_input("Enter your Age::", key="a2")
gender_sec = st.number_input("Enter your gender::", key="g2")
weight_sec = st.number_input("Enter your    weight::", key="w2")
phyact_sec = st.number_input("Enter your physical activity daliy::", key="p2")
weather_sec = st.number_input("Enter The weither Condition::", key="we2")

click_sec = st.button("Predict", key="b2")

if click_sec:
    with st.spinner("wait..", show_time=False):
        time.sleep(2)
        pred_sec = model_sec.predict([[Age_sec, gender_sec, weight_sec, phyact_sec, weather_sec]])
        st.write("You water Intake Should be::", pred_sec[0], "liters")


st.title("Model that will tell your Addiction Score")
model_third = joblib.load("model_third.pkl")

age_third = st.number_input("Enter the age::", key="a3")
gender_third = st.number_input("Enter your gender::", key="g3")
accd = st.number_input("Enter your Academic Leval::", key="ac3")
dailyavgusephone = st.number_input("Enter your Avg  daliy use of phone::", key="u3")
mosusedplt = st.number_input("Enter your most used platform::", key="m3")
acadicperform = st.number_input("It affects you studies?::", key="af3")
sleeppernight = st.number_input("Enter how many Hr do you sleep Daily::", key="sl3")
realation = st.number_input("Enter are you in the RelationShip?", key="re3")

click_third = st.button("Predict", key="b3")

if click_third:
    with st.spinner("wait..", show_time=False):
        time.sleep(2)
        pred_third = model_third.predict([[age_third, gender_third, accd,
                                           dailyavgusephone, mosusedplt,
                                           acadicperform, sleeppernight, realation]])
        st.write("This is your Addiction Score out of 9::", pred_third[0])


st.title("Model that will tell your Productivity Score out of 10  According TO your morning routine")
model_four = joblib.load("model_four.pkl")

wakeup = st.number_input("Enter Your wakeup time::", key="a46")
medi = st.number_input("Do you meditate in the morning::", key="g12")
accd = st.number_input("do you exercise in the morning::", key="ac10")
screen = st.number_input("Enter your Screen time Before Work::", key="u99")

click_four = st.button("Predict", key="b33")

if click_four:
    with st.spinner("wait..", show_time=False):
        time.sleep(2)
        pred_four = model_four.predict([[wakeup,medi,accd,screen]])
        st.write("This is your Addiction Score out of 9::", pred_four[0])