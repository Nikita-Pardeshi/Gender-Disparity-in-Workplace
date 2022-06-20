#import the necessary library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

#import the data frame with countries, number of days of maternity and paternity leaves and region for filters
leaves= pd.read_csv('./datasets/MAJOR-COUNTRIES.csv', encoding='latin-1')
leaves.head()

leaves['Region'].unique()

"""### MATERNITY LEAVES BY REGION AND COUNTRY"""

# Reorder the dataframe
maternity = (
    leaves
    .groupby(["Region"])
    .apply(lambda x: x.sort_values(["Length of paid maternity leave"], ascending = False))
    .reset_index(drop=True)
)
maternity= maternity.drop(['Length of paid paternity leave'],axis=1)
maternity.head()

"""### PATERNITY LEAVES BY REGION AND COUNTRY"""

# Reorder the dataframe
paternity = (
    leaves
    .groupby(["Region"])
    .apply(lambda x: x.sort_values(["Length of paid paternity leave"], ascending = False))
    .reset_index(drop=True)
)
paternity= paternity.drop(['Length of paid maternity leave'],axis=1)
paternity.head()

"""### Side by side sunburst plots for Maternity and Paternity leaves"""

from plotly.subplots import make_subplots
import plotly.offline as pyo


#Maternity Leaves
fig1 = px.sunburst(maternity, path=['Region', 'Country'], values='Length of paid maternity leave',
                   color='Region', hover_data=['Length of paid maternity leave'],
                   color_discrete_map={'(?)':'blue', 'Africa':'darkblue', 'Asia':'darkorange',
                                       'Oceania':'#89CFF0','Americas':'#FF7F50',
                                       'Europe':'#0F52BA'})#set custom blue orange theme
                                       
#Paternity Leaves
fig2 = px.sunburst(paternity, path=['Region', 'Country'], values='Length of paid paternity leave',
                   color='Region', hover_data=['Length of paid paternity leave'],
                   color_discrete_map={'(?)':'blue', 'Africa':'darkblue', 'Asia':'darkorange',
                                       'Oceania':'#89CFF0','Americas':'#FF7F50',
                                       'Europe':'#0F52BA'}) #set custom blue orange theme

fig = make_subplots(rows=1, cols=2, subplot_titles=['Number of Paid Maternity Leaves by Country', 
                                                    'Number of Paid Paternity Leaves by Country'],
                    specs=[[{"type": "sunburst"}, {"type": "sunburst"}]
])

fig.add_trace(fig1.data[0], row=1, col=1)
fig.add_trace(fig2.data[0], row=1, col=2)
pyo.iplot(fig, filename = 'sunburst')

fig.write_html('paternity_maternity.html')

#creating a function to plot a separate html plot for each of the regions 

def create_plot(dataframe, country_name):
  group=['Maternity Leave']*len(dataframe['Country'])
  group.extend(['Paternity Leave']*len(dataframe['Country']))
  leaves= dataframe['Length of paid maternity leave'].to_list()
  leaves.extend(dataframe['Length of paid paternity leave'].to_list())
  country=dataframe['Country'].tolist()
  country.extend(dataframe['Country'].to_list())
  df= pd.DataFrame({'country':country, 
                        'leaves':leaves, 'Group':group})
  
  fig = px.bar(df, y="leaves", x="country",
             hover_data=['leaves'],
             barmode = 'group',
             color='Group',
             color_discrete_map={
                 'Maternity Leave': '#1434A4',
                 'Paternity Leave': '#F28C28'}
               )


  fig.update_layout(
      template="simple_white",
      xaxis=dict(title_text="Country"),
      yaxis=dict(title_text="Number of Paid leaves"),
      title='Number of Paid leaves by '+country_name+' Country',
      width= 900,
      height=600
  )
  fig.update_xaxes(tickangle=45)

  pyo.iplot(fig, filename = 'country-bar')
  fig.write_html(country_name+'.html')

create_plot(leaves.loc[leaves['Region'] == 'Africa'], 'African')
create_plot(leaves.loc[leaves['Region'] == 'Asia'], 'Asian')
create_plot(leaves.loc[leaves['Region'] == 'Europe'], 'European')
create_plot(leaves.loc[leaves['Region'] == 'Americas'], 'American')
create_plot(leaves.loc[leaves['Region'] == 'Oceania'], 'Ocenian')

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# jupyter nbconvert --to html /content/Parenthood_leaves.ipynb