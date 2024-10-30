# PART 2
import streamlit as st
import base64
from st_pages import add_page_title, get_nav_from_toml
import webbrowser
import re
import smtplib


st.title("Tính toán chỉ số BMI")

st.header("Thông tin cá nhân")
name = st.text_input("Họ và tên:")
age = st.number_input("Tuổi:", min_value=1, max_value=100, step=1)
gender = st.selectbox("Giới tính:", options=["Nam", "Nữ", "LGBT"])
height = st.number_input("Chiều cao (cm):", min_value=0.0, step=0.1)
weight = st.number_input("Cân nặng (kg):", min_value=0.0, step=0.1)

def calculate_bmi(weight, height):
    if height > 0:
        height_m = height / 100  
        bmi = weight / (height_m ** 2)
        return bmi
    else:
        return None

def classify_bmi_adult(bmi):
    if bmi < 18.5:
        return "Thiếu cân"
    elif 18.5 <= bmi < 24.9:
        return "Cân nặng bình thường"
    elif 25 <= bmi < 29.9:
        return "Thừa cân"
    else:
        return "Béo phì"

def classify_bmi_child(bmi):
    if bmi < 15:
        return "Thiếu cân"
    elif 15 <= bmi < 20:
        return "Cân nặng bình thường"
    elif 20 <= bmi < 25:
        return "Nguy cơ thừa cân"
    else:
        return "Thừa cân (béo phì)"

if st.button("Tính toán BMI"):
    bmi = calculate_bmi(weight, height)
    if bmi:
        st.write(f"Chỉ số BMI của bạn là: {bmi:.2f}")
        st.write(f"Giới tính: {gender}")
        st.write(f"Tuổi: {age}")

        if age >= 18:
            classification = classify_bmi_adult(bmi)
            st.write(f"Phân loại BMI (Người lớn): {classification}")
        else:
            classification = classify_bmi_child(bmi)
            st.write(f"Phân loại BMI (Trẻ em): {classification}")
    else:
        st.write("Vui lòng nhập chiều cao hợp lệ để tính toán BMI.")
