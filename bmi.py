import streamlit as st
import pandas as pd
import time
# MAIN TITILE 
st.title("BMI Calculator")
# SLIDER FOR USER INPUT
height = st.slider("Enter Your Hight (in cm)",100,250,175)
weight = st.slider("Enter Your Wiaght (in kg)",40,200,75)
 # CALCULATION PART
bmi = weight/((height/100)**2)
#CHECKING WHETHER CLICK OR NOT
button1 = st.button("Click Me")

# SOME FANCY THINGS
if(button1):
    with st.spinner("In Progress..."):
        time.sleep(2)
        st.success("Done",icon="✅")
    st.write(f"### Your BMI is {bmi:.2f} ###")
    if(bmi<18.5):
        st.write("Take a Protien Rich Diet")
    elif(18.5<=bmi<=24.90):
        st.snow()  
        st.success("Keep it up do Maintain Your Sprit",icon="🔥") 
    elif(25<=bmi< 29.9):
        st.warning("You are Over Weight Do Physical Activity ",icon="⚠️")
    else:
        st.error("You are Over Weight Do Physical Activity ",icon="🚨")  
        
# DISCRIPTION ABOUT BMI             
st.write("### BMI Categories ###")
st.write("- Undrweight : BMI less then 18.5 ")
st.write("- Normal Weight : BMI between 18.5 and 24.9")
st.write("- OverWeight : BMI between 25 and 29.9")
st.write("- Obesity : BMI 30 or greater")
