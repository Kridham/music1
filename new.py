import streamlit as st

st.title("Login")
a=st.text_input("ID bhro ")
b=st.text_input("password bhro")
if st.button("Sign in"):
    if a=="kridham08" and b=="ridham_08":
        st.write("login ho gya")
        st.title("ridham music")
        music1="akhar.mp3"
        music2="the ringtone.mp3"
        song=st.text_input("enter the song name")
        if st.button("press"):
            if song.lower() in music1.lower():
                st.header("akhar")
                st.audio(music1,format="audio/mp3")
                

            if song.lower() in music2.lower():
                st.header("the ringtone")
                st.audio(music2,format="audio/mp3")

        
    else:
        st.write(" chal password yaad krke aa ")
        st.image("stress.jpg")

