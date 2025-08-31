import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello, Streamlit! How are you?")
txt_var = st.text_input("Your name")
st.write(f"Your name is : {txt_var}")

btn = st.button("Click me!")
if btn:
    st.write(f"Hello {txt_var} how can i help you")

num1 = st.number_input(f"Enter first value")
num2 = st.number_input(f"Enter second value")
chart_data = pd.DataFrame(np.random.randn(int(num1), int(num2)))

st.bar_chart(chart_data)
st.line_chart(chart_data)