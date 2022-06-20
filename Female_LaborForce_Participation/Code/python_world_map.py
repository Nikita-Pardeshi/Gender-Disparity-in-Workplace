##############################################################
#* ANLY 503 Project: Interactive, Data-driven Visual Narrative
#* 
#*
##############################################################


# Import Libraries
import pandas as pd
import plotly.express as px


# Importing the dataset
data = pd.read_csv("./datasets/ratio-of-female-to-male-labor-force-participation-rates.csv")
print(data.head(5)) # print top 5 records

# Validate and correct the attribute data types
print(data.info())
data.dtypes
data['date']= pd.to_datetime(data['date'])

# Remove all NAs
data=data.fillna(0)


# Aggregate data
data=data.groupby(['Code','Year']).sum().reset_index()
print(data.head(5)) # print top 5 records

# Rename columns
data = data.rename(columns={'Ratio of female to male labor force participation rate (%) (modeled ILO estimate)': 'Ratio(%)',
                           'Code':'Country_Code'})



################
# VISUALIZATION
################

# create choropleth world map
fig = px.choropleth(data, 
              locations = 'Country_Code',
              color="Ratio(%)", 
              animation_frame="Year",
              color_continuous_scale="icefire",
              locationmode='ISO-3',
              scope="world",
              range_color=(0, 108),
              title='Ratio of Female to Male Labor Force Participation Rates, (1990-2020)',
              height=700,
              width=1000
             )

# save the chart
fig.write_html("world-map.html")
