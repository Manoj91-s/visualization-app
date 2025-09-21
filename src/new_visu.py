import streamlit as st
import pandas as pd
import calendar
import datetime
from typing import Optional

class Visualizer():
    def __init__(
        self,
        month:int,
        year: int
    ):
        self.month = month
        self.year = year
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        self.df = None
        if uploaded_file is not None:
            self.df = pd.read_csv(uploaded_file, sep=";")
            self._plot_monthly_avg_otp()
    
    def _get_countries(self) -> Optional[set]:
        if self.df is not None:
            countries = self.df["Countries"]
            country_set = set()
            for country in countries:
                country_set.add(country)
            country_set = {country for country in country_set if not pd.isna(country)}
            return country_set
    
    def _get_week_count_in_the_month(self) -> set:
        week_num_set = set()
        days = calendar.monthrange(self.year, self.month)[1]
        for day in range(1, days +1):
            week_num = datetime.date(year=self.year, month=self.month, day=day).isocalendar()[1]
            week_num_set.add(week_num)
        return week_num_set

    def _plot_monthly_avg_otp(self) -> Optional[dict[str, float]]:
        countries_otps: dict[str, list[float]] = {}
        monthly_avg_otp: dict[str, float] = {}
        if self.df is not None:
            countries = self.df["Countries"]
            week_numbers = self.df["Week number"]
            otps = self.df["OTP (%)"]

            weeks_of_month = self._get_week_count_in_the_month()
            for country in range(1, len(countries)):
                if week_numbers[country] in weeks_of_month:
                    country_name = countries[country]
                    if country_name not in countries_otps.keys():
                        countries_otps[country_name] = [otps[country]]
                    else:
                        countries_otps[country_name].append(otps[country])

            for country, opt_vals in countries_otps.items():
                monthly_avg_otp[country] = sum(opt_vals) / len(opt_vals)
            df_result = pd.DataFrame(monthly_avg_otp.items(), columns=["Country", "OTP Percentage"])
            st.bar_chart(df_result, x="Country", y= "OTP Percentage")


            
month = int(st.number_input(f"Enter month"))
year = int(st.number_input(f"Enter year"))       
visualizer = Visualizer(month, year)
