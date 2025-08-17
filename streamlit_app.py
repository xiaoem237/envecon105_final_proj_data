import streamlit as st

st.title("Envecon 105 Case Study Dashboard")
st.write("Author: Emily Xiao")

st.write("This dashboard takes you through findings about CO2 emissions and related variables of the world, the United States, and Switzerland.")
st.write("Below is a graph of the world's CO2 emissions over the years. Within the past century, emissions have only increased exponentially, and continue to grow.")
st.image("https://github.com/xiaoem237/envecon105_final_proj_data/blob/main/static/world_co2.png?raw=true")

st.image("https://github.com/xiaoem237/envecon105_final_proj_data/blob/main/static/top_10_co2.png?raw=true")
st.write("Here is a plot illustrating more detailed the trends of the top 10 CO2 emission-producing countries over time. While the United States held the #1 spot, China has since surpassed the U.S. and the rest of the world by far.")

st.write("Now, let's take a look at the CO2 emissions, GDP per capita, and energy use of the United States compared to other countries:")
st.image("https://github.com/xiaoem237/envecon105_final_proj_data/blob/main/static/indicators_vs_US.png?raw=true")
st.write("")

st.write("Let's do the same for Switzerland:")
st.image("https://github.com/xiaoem237/envecon105_final_proj_data/blob/main/static/indicators_vs_Switzerland.png?raw=true")
