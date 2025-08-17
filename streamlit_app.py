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

st.write("Let's do the same for Switzerland:")
st.image("https://github.com/xiaoem237/envecon105_final_proj_data/blob/main/static/indicators_vs_Switzerland.png?raw=true")

st.write("Neither of these countries seem to have odd trends of these variables, besides the U.S. that has very large CO2 emissions.")

st.write("Another interest of this case study was the relationship between CO2 emissions and average annual temperature. Let's take a look at the trends of these variables for both countries.")
st.image("https://github.com/xiaoem237/envecon105_final_proj_data/blob/main/static/co2_temp_us.png?raw=true")
st.write("In these two plots, it seems that the regression lines offer a similar shape, both variables peaking in the 2000s and falling in more recent years.")
st.image("https://github.com/xiaoem237/envecon105_final_proj_data/blob/main/static/co2_temp_switzerland.png?raw=true")
st.write("Switzerland, however, is quite different. It arguably does have a small peak around the year 2010 for CO2 emissions like the U.S., but the temperature continues to curve upward instead of matching the trend of the emissions.")

st.write("Lastly, we can take a look at a scaled scatterplot for CO2 emissions and temperature for both countries to get a better idea of the association between them:")
st.image("https://github.com/xiaoem237/envecon105_final_proj_data/blob/main/static/us_co2_temp_scatter.png?raw=true")
st.image("https://github.com/xiaoem237/envecon105_final_proj_data/blob/main/static/switzerland_co2_temp_scatter.png?raw=true")
