import streamlit as st
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
        
