# ===============================================================
#           CREATE DASHBOARD BIKE SHARING USING STREAMLIT       =
#           ---------------------------------------------       =
# Nama          : Salsabila Zahirah / Ira Salsabila             =
# Email         : irasalsabila@gmail.com                        =
# Id Dicoding   : dicoding.com/users/irasalsabila/              =
# Created       : 30 September 2023                             =
# ===============================================================

# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

import warnings

# ==============================
# LOAD DATA
# ==============================


@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Dropdown to select the dataset
selected_dataset = st.selectbox("Select Dataset", ["Daily", "Hourly"])

if selected_dataset == "Daily":
    file_path = "dataset/day.csv"
elif selected_dataset == "Hourly":
    file_path = "dataset/hour.csv"

data = load_data(file_path)



# ==============================
# TITLE DASHBOARD
# ==============================
# Set page title
st.title("Bike Sharing Dashboard")

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Ira Salsabila**")
st.sidebar.markdown(
    "**• Email: [irasalsabila@gmail.com](irasalsabila@gmail.com)**")
st.sidebar.markdown(
    "**• Dicoding: [irasalsabila](https://www.dicoding.com/users/irasalsabila/)**")
st.sidebar.markdown(
    "**• LinkedIn: [Salsabila Zahirah](https://www.linkedin.com/in/irasalsabila/)**")


st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Show dataset source
# st.sidebar.markdown("[Download Dataset](https://link-to-your-dataset)")

# st.sidebar.markdown('**Weather:**')
# st.sidebar.markdown('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
# st.sidebar.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
# st.sidebar.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
# st.sidebar.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')


# ==============================
# VISUALIZATION
# ==============================

# create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    # Season-wise bike share count
    # st.subheader("Season-wise Bike Share Count")

    # Mapping dari angka ke label musim
    season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data["season_label"] = data["season"].map(season_mapping)

    season_count = data.groupby("season_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season_label",
                              y="cnt", title="Season-wise Bike Share Count")
    fig_season_count.update_xaxes(title="Season")
    fig_season_count.update_yaxes(title="Rental bikes")
    st.plotly_chart(fig_season_count, use_container_width=True,
                    height=400, width=600)

with col2:
    # Weather situation-wise bike share count
    # st.subheader("Weather Situation-wise Bike Share Count")

    weather_mapping = {1: "Cloudy", 2: "Foggy", 3: "Snowy", 4: "Rainy"}
    data['weather_description'] = data['weathersit'].map(weather_mapping)
    weather_count = data.groupby("weather_description")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weather_description",
                            y="cnt", title="Weather Situation-wise Bike Share Count")
    fig_weather_count.update_xaxes(title="Weather Situation")
    fig_weather_count.update_yaxes(title="Rental bikes")
    st.plotly_chart(fig_weather_count, use_container_width=True, height=400, width=800)



humidity_vs_cnt = data.groupby(["weekday", "hum", "temp", "windspeed"])["cnt"].sum().reset_index()

humidity_vs_cnt["weekday"] = humidity_vs_cnt["weekday"].apply(lambda x: calendar.day_name[x])

# Allow selection of multiple weekdays
selected_weekdays = st.multiselect("Select weekdays", list(calendar.day_name))

selected_data = humidity_vs_cnt[humidity_vs_cnt["weekday"].isin(selected_weekdays)]

selected_variable = st.selectbox("Select a variable for X-axis", ["Humidity", "Temperature", "Wind Speed"])

if selected_variable == "Humidity":
    x_data = "hum"
    x_title = "Humidity"
elif selected_variable == "Temperature":
    x_data = "temp"
    x_title = "Temperature"
elif selected_variable == "Wind Speed":
    x_data = "windspeed"
    x_title = "Wind Speed"

weekday_colors = {
    "Monday": "#636EFA",
    "Tuesday": "#EF553B",
    "Wednesday": "#00CC96",
    "Thursday": "#AB63FA",
    "Friday": "#FFA15A",
    "Saturday": "#FF6692",
    "Sunday": "#B6E880"
}

# Map weekday names to colors
selected_data['color'] = selected_data['weekday'].map(weekday_colors)

fig = px.scatter(selected_data, x=x_data, y="cnt", color='color',
                 title=f"Bike Share Count vs. {x_title} for {', '.join(selected_weekdays)}",
                 color_discrete_map={color_code: day_name for color_code, day_name in weekday_colors.items()})

# Update the legend title and axis titles
fig.update_traces(showlegend=True)
fig.update_layout(legend_title='Weekday')
fig.update_xaxes(title=x_title)
fig.update_yaxes(title="Bike Share Count")

# Update the legend labels to show weekday names instead of RGB codes
for i, day_name in enumerate(selected_weekdays):
    fig.data[i].name = day_name

st.plotly_chart(fig, use_container_width=True)
