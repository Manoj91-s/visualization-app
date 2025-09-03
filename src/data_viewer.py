import streamlit as st
import pandas as pd

st.title(f"Data viewer")
countries = st.text_input(
    "Enter countries, separated by a comma (,)",
    value="Enter_countries"
)
start_week = st.number_input("Starting week", min_value=1, max_value=52, step=1, value=1)
end_week = st.number_input("Ending week", min_value=1, max_value=52, step=1, value=1)

# Clean up country names
countries_list = [c.strip() for c in countries.split(",")]

# Number of rows = number of weeks
weeks_list = range(1, (end_week - start_week) + 2)

# Create an initial DataFrame with zeros
df = pd.DataFrame(
    0,
    index=[f"week {week}" for week in weeks_list],
    columns=countries_list,
)

# Display editable table (every cell is a number input)
edited_df = st.data_editor(
    df,    # allow adding/removing rows
    use_container_width=True
)

st.bar_chart(edited_df, x_label = "Weeks", y_label = f"Percentagse (%)")
