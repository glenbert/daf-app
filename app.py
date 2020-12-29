import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">',
                unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(
        f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

st.title('Hourly Day Ahead Forecast')

file = st.file_uploader("Choose an excel file", type="xlsx")

if st.button('Upload Data'):
    df = pd.read_excel(file, sheet_name="Data")
    plt_series = px.line(df, x='DateTime', y='Actual',
                         labels={
                             "Actual": "Actual Hourly Load (MW)",
                             "DateTime": "Date Time"
                         },
                         width=1000, height=500,
                         title="Hourly Actual Load")
    st.plotly_chart(plt_series)
