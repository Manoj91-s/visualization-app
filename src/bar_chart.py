import streamlit as st

st.title(f"OTP Chart")

no_of_weeks = st.number_input(
    f"Enter number of weeks",
    min_value=1,
    max_value=10,
    step=1
)

week_inputs = []
for week in range(1, no_of_weeks + 1):
    week_inputs.append(st.number_input(f"Enter otp in percentage for week: {week}", key=f"week_{week}"))

st.bar_chart(week_inputs, x_label="Weeks", y_label="OTP in percentage")
