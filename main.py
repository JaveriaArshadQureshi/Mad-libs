import streamlit as st
import random

# Creating python mad_lib game 

#title of the game
st.title("🚨 Adjective Alert ! A Mad Libs 📺")

#sidebar to get user input
st.sidebar.header("Fill information below: ")
#user input
adj = st.sidebar.text_input("Enter an Adjective:  ", 'Revolutionary, exciting, Inspiring')
famous_person = st.sidebar.text_input("Enter a famous_person:  " ,'Zia Khan')
verb = st.sidebar.text_input("Enter a Verb:  " , 'code, develop, learn')
verb2 = st.sidebar.text_input("Enter another Verb:  ", 'Debug, Break, Tech')

# creating list of mad libs
mad_libs = [
    f"Learning Python is {adj}! I {verb} with joy every time I {verb2} like {famous_person} on a coding spree.",
    f"Tech trends are {adj}! Stay ahead by learning to {verb} and always {verb2} like {famous_person}, the visionary!",
    f"Open-source is {adj}! To contribute like {famous_person}, you must {verb} daily and {verb2} without fear!",
    f"Startup life is {adj}! Every founder should {verb} like crazy and {verb2} like {famous_person} to succeed.",
]

# button to generate mad lib
if st.button("Generate Mad Lib"):
    #randomly select a mad lib
    mad_lib = random.choice(mad_libs)
    #display the mad lib
    st.write(mad_lib)
    