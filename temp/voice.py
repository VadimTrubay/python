# import speech_recognition as sr
#
#
# def record_volume():
#     r = sr.Recognizer()
#     with sr.Microphone(device_index=1) as source:
#         print("Listen...")
#         audio = r.listen(source)
#
#     query = r.recognize_google(audio, language="ru")
#     print(query.lower(), type(query.lower()))
#
#
# record_volume()

import streamlit as st

# Создание двух колонок в 2/3 и 1/3 ширины экрана
left_column, right_column = st.columns([2, 1])

# В левой колонке поместите элементы для левой панели
with left_column:
    st.write("Left Panel")
    st.button("Button 1 - Left")

# В правой колонке поместите элементы для правой панели
with right_column:
    st.write("Right Panel")
    st.button("Button 2 - Right")