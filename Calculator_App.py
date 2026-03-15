import streamlit as st 

st.title("Calculator App")

number1 = st.number_input("Enter the first number")
number2 = st.number_input("Enter the second number")

operation = st.selectbox(
                        "Select an operation: ", 
                        ("Add", "Subtract", "Multiply", "Divide")
)

result = 0

if operation == "Add":
    result = round(number1 + number2, 2)
elif operation == "Subtract":
    result = round(number1 - number2, 2)
elif operation == "Multiply":
    result = round(number1 * number2, 2)
elif operation == "Divide":
    if number2 != 0:
        result = round(number1 / number2, 2)
    else:
        st.error("Cannot divide by zero")
        result = "Error"

st.write("---")
if result != "Error":
    st.success(f"The result of {number1} {operation} {number2} is: **{result}**")