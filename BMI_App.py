import streamlit as st

st.title("BMI Calculator App")

height = st.number_input("Enter your height in centimeters(e.g. 170 cm)")
weight = st.number_input("Enter your weight in kilograms(e.g. 70 kg)")

try:
    bmi = weight /  ((height / 100) ** 2)
    st.write(f"Your BMI is: **{round(bmi, 2)}**")

    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
except ZeroDivisionError:
        st.error("Height cannot be zero.")

