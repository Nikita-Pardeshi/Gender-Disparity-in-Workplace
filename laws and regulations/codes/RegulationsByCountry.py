# Importing libraries
import pandas as pd
import altair as alt


# Importing data
data=pd.read_csv("../datasets/Women Business and the Law Index Score (scale 1-100) & flag data.csv")
td=pd.read_csv("../datasets/WBL2022_Reforms Database.xlsx - ReformDatabase.csv")

#Merging data frames
data1=pd.merge(td,data,on='ID')

# Drop-down options
Continents=['Asia','Africa','Europe','North America','South America','Oceania']

# Selection based on ID interaction
selector = alt.selection_single(empty='all', fields=['ID'])

# Drop-down based on continent
genre_dropdown = alt.binding_select(options=Continents)
genre_select = alt.selection_single(fields=["Continent"], bind=genre_dropdown, name="Select")

# Base chart properties
base = alt.Chart(data).properties(
    width=700,
    height=700,
    title="WBL Score Index v/s Number of Laws made"
).add_selection(selector)


# Adding scatter plot with points as flags to base chart
points = base.mark_image(
    width=50,
    height=50
).encode(
    alt.X('Number of Laws:Q',
        scale=alt.Scale(domain=(0, 20))
    ),
    alt.Y('WBL Index Score:Q',
        scale=alt.Scale(domain=(25, 105))
    ),
    url='Mark',
    opacity = alt.condition(selector, alt.value(1.0), alt.value(0.3)),
    tooltip=['Country','Number of Laws','WBL Index Score','Continent']
).add_selection(genre_select).transform_filter(
    genre_select).interactive()


# Timeseries plot
timeseries = alt.Chart(data1).mark_line(point={
      "filled": False,
      "fill": "white"
    }).encode(
    alt.X('Year:Q',
          scale=alt.Scale(zero=False),axis=alt.Axis(format='.0f')),
    y='Country',
    color=alt.Color('ID:N', legend=None,scale=alt.Scale(scheme="darkred")),
    # opacity = alt.condition(selector, alt.value(1.0), alt.value(0.3)),
    tooltip=['Country','Year','Indicator','Type of Reform','Reform Description']
).transform_filter(
    selector
).add_selection(genre_select).transform_filter(
    genre_select).properties(title="Regulation details by Country"
)

# Combining both plots
plot=alt.concat(points,timeseries)
plot.properties(
    width=100,
    height=100
)

# Saving plot as html
plot.save('RegulationsByCountry.html')

"""

These tags were added to the final html to shift position of the drop down menu and 
add interaction help text
<style>
vis {

  margin-top: 2%;

}
form.vega-bindings {
  position: absolute;
  left: 0px;
    top: -20px;

}
</style>

<body>
<p style="color:grey;">
    Select_Continent drop-down menu to filter both charts by continent. <br>
    Zoom/Pan the left chart to find a specific country or hover over flag to see country name. <br>
    Select the flag of any country to see the details of reforms made in that country on the chart on the right.<br>
    Hover over the points on the right chart to get details about the reform made in that year.  </p>

"""

