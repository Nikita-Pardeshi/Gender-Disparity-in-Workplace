
# Gender Disparity in Workplace

## Group 21: Aashika Padmanabhan | Mitali Shah | Nikita Pardeshi | Shazia Sulaiman

## Gender wage disparity in numbers
The topic was introduced in the earlier section and now will be dwelling deeper into each of the individual sections. We decided that the best way to go about this, is to introduce the topics in gradual complexity. So, in Gender disparity in numbers we talk about the basic issues - controlled and uncontrolled waged, gender inequality and equality index, decomposition of the wage break down to ensure that the audience does not get information overload but is gradually introduced to the nuances of gender equality with appropriate visualization so hammer home the concepts.

#### Dataset & Data Processing

**Data**:
Datasets are downloaded from World Bank, OECD, Statista which are uploaded to the datasets folder.

Original dataset link:<br>

1. https://databank.worldbank.org/source/gender-statistics
2. http://data.worldbank.org/data-catalog/world-development-indicators
3. https://ourworldindata.org/grapher/regional-averages-of-the-composite-gender-equality-index?tab=table
4. https://ourworldindata.org/grapher/gender-inequality-index-from-the-human-development-report 
5. https://ourworldindata.org/grapher/gender-inequality-index-from-the-human-development-report
6. https://stats.oecd.org/index.aspx?queryid=54758
7. https://stats.oecd.org/Index.aspx?DataSetCode=DV_DCD_GENDER
8. https://ourworldindata.org/grapher/gender-wage-gap-vs-gdp-per-capita
9. https://ourworldindata.org/grapher/regional-averages-of-the-composite-gender-equality-index

**Data Processing**:
Data pre-processing included converting data to tidy format for visualizations, merging table using country code, deleting rows with NA's, sorting values so that the plot appears more visually pleasing. 
The primary unit of analysis in most graphs was country/region and in few cases the entity - GDP, the wages, age group. 
The dataset contains - year, country code, entity being discussed which can be GDP, wage with respect to age, %representation of women in top 10% income bracket.

Cleaned dataset link:https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/datasets
Code link: https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/gender%20disparity%20in%20numbers/code
 
#### Design Choices
As mentioned earlier, the whole idea of this section is to provide visuals that are easy to understand and introduce the topic of disparity with numbers so that the readers has information needed to proceed further. Special care has been given that the audience is not boggled with details as the first few seconds are crucial to hook the readers which determines if they will read the article or not.

**Figure 1:**
This is a line chart and details about controlled and uncontrolled wages and the progress over time from 2014 and 2021. Here audience can see the gap closing but glacially and also see the difference. Line chart is the ideal fit for this as its easy to interpret and the gap noticeable. The alternative will be a bar graph which we felt would complicate such a simple concept. Chart is annotated so that information is available at the onset. Tool tip has also been added to make the reader become more involved by checking the details at different years

**Figure 2:**
This section a new concept is introduced - Gender Inequality index and how it changes throughout the world from 1995 to 2015. The best way to do this is via map and added a slider so that changes are can be seen. Here a higher index indicates more inequality and hence a darker orange (theme is orange - blue) was selected. Tool tip with the exact details have been added to provide more concrete information should reader want to find out more. The map was always the first choice in this case.

**Figure 3:**
Now the concepts have been introduced it was time to talk about the reasons for such a disparity. We have used a grouped bar graph for this comparing decomposition from 1980 and 2010 grouped by decomposition type. The same 2 colors have been used. This chart also has been annotated so that readers can understand at first glance the changes and need not ballpark any details.

**Figure 4:**
We now more to talking about disparity as we age, the easiest way to represent this is using a line chart as the widening gap can be seen. Line chart though simple, clearly explains this.

**Figure 5:**
This figure tries to explain relationship between GDP and Gender Wage Gap. The GDP has been converting to log. The relationship between the 2 are very clear using this graph. Converting to log of GDP helped this to be clear. The other option was to use a scatter plot but a joint plot does a better job and hence was selected.

**Figure 6:**
This figure explains the change in % of women representing top 10% income group in 2006 and 2013. A dumbbell was selected as the same groups changes are being shown. This makes the difference very clear.

**Figure 7:**
The last plot of this section is finally tying things all together and showing the equality index for different regions. Different regions were chosen in particular as this will provide a more wholistic picture and the countries within the same regions have the same socio-economic characteristics.

Visualization Codes: https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/gender%20disparity%20in%20numbers/code

#### Reflection
The initial proposal was to create a combination chart which was not required as the idea to keep the introduction accessible to all audience was considered. The other chart types however are the same as in the initial proposal with a story telling aspect – introducing the concepts and then drilling to details and more nuances was employed.
Technical goals have not changed
Original proposal was realistic but as we got more hands on with data, a less complicated data visualization was employed to convey the story with as much ease as possible was selected.
Was there anything you wanted to implement that you ultimately couldn't figure out how to do? If so, then what workarounds did you employ, or did you abandon your original idea?
No, thee wasn’t anything that I wanted to implement but did not. What I set out to do was completed. I would have preferred to add an altair plot with interactions.
If you were to make the project again from scratch, I would implement charts that tie with the Javascript when scrolling such as - https://www.theguardian.com/news/ng-interactive/2018/apr/05/women-are-paid-less-than-men-heres-how-to-fix-it




## Change in women's participation in the workforce

#### Dataset & Data Processing
<!--Talk about data variables and source as well as cleaning-->
**Data**:
The Datasets are collected from the offcial website of U.S Bureau of Labor Statistics and the World Bank Data.
It has different columns for year, women participation rate , maritial status, age, race and
educational attainment. <br>
Original dataset link: <br>
1. https://www.bls.gov/news.release/empsit.t01.htm <br>
2. https://data.worldbank.org/



**Data Processing**:
As part of data cleaning, removed unwanted observations from the dataset and filtered for the required columns for our analysis. The data is also converted data into wide format. The separate data tables are also be joined over the common variable i.e. year to
analyze the trends over a period of time.<br>
Code link:https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/Female_LaborForce_Participation/Code
Cleaned dataset link: https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/datasets

#### Design Choices
<!--For each figure describe why is it important and the design choices-->
**Figure 8:** The line plot indicates how the gender dynamics has changed in the labor force over the years for different countries.
 The chart is important in analyzing the changes over a period of time. The trendline for United States is highlighted in blue color and the drop-down on the top right corner gives user the ability to select different countries and analyze the trends. A line chart is chosen as it is the best chart to show trends over time. The line plot also allows users to interact with graphs on display and point value display allowing for a better storytelling experience. Findings have been noted against the graph.

**Figure 9:** The lineplot illustrates the changes in the female labor force participation rates in United states by different Marital Status over the years. This is important to understand whether the marked upward trend observed for female participation is driven by the trend among married women or not. A lineplot is chose to display the trends over time.


**Figure 10:** The bar plot shows how the female employment to population ratio changed for the top 10 countries by Gender equality.
As the Labor force participation comprises of both employed and unemployed people searching for work, this barplot is important in understanding whether the Female employment has grown together with rising female participation in the Labor force. The top 10 countries which highest gender equality are selected to analyze the change in the number of employed women as a share of the total female population. The Barplot are extremely effective and allows user to recognize patterns or trends far more easily.

**Figure 11:** : The world map shows the ratio between female and male labor participation rates over the years. The slider to the bottom of the chart allow users to see how data changes over time on the world map. This map plot presents the information on the ratio between female and male labor participation rates across the world in a simple, visual way. This provides user an easy way to visualize how a ratio varies across a geographic area and show the level of variability within a region as the slider moves over a date range.

Visualization Codes: https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/Female_LaborForce_Participation/Code


#### Reflection
The tasks and plots for this section have changed from the initial proposal. Although the visualization goal remains the same , the visual implementations have evolved. The knowledge on Timeseries and building interactive charts helped change the outlook on building visualizations that can tell the story in a more impactful and easier manner. These charts also provide users the flexibility of getting data for a certain timeframe and more user interactions are added to make visualization more appealing and interesting.

The color themes, legend position and alignment of the charts are changed from the midpoint submission. Additional information (i.e., included all the countries with a drop-down ) was added in the plots including a trendline in the chart to better understand the plot and show visual data trends.


## Measuring laws and regulations

#### Dataset & Data Processing
<!--Talk about data variables and source as well as cleaning-->
**Data**:
Original Dataset: https://wbl.worldbank.org/content/dam/sites/wbl/documents/2021/02/WBL50YearPanelDetailsWeb21Feb2021.xlsx <br>

**Data Processing**: For plotting the number of maternity and paternity leaves as two separate sunburst charts, there was a need to get the data into proper format. Hence, heirarchies were created across the five continents by using groupby() by Region and converted to a two separate pandas dataframe.

Code link: https://github.com/anly503/project-spring-2022-projectgroup21/blob/main/laws%20and%20regulations/codes

#### Design Choices
<!--For each figure describe why is it important and the design choices-->
**Figure 12:** The chart indicates the laws made in each country with respect to gender equality. The chart can be used to find countries with higher scores and the laws they have implemented to promote gender equality. It can also be used to find laws made by a country's neighbor with similar geographic and cultural backgrounds that could be applied to that country. The chart plots the WBL index v/s the number of laws made per country to see if there is a correlation between the two. The idea of using flags was to make the chart more clean and impactful instead of adding points and labels since there are 190 countries on this chart. The drop-down menu lets the user filter out based on continent and see all laws made by each country. This aids comparison between countries and their laws within the same continent. A simple line plot with markers was added for the timeline to show how actively are countries adding laws. If actual details of the law was added to the plot it would be messy and difficult to read and hence the option to hover to see more details was used. The color of this chart has been selected to match the overall theme of the site and has no particular significance.

**Innovative aspect:** 

1. Creativity: The information represented in this chart could have been very well been conveyed using a simple scatter plot. However, we decided to represent the laws as a story timelines and countries using flags. We normally see laws presented in tabular or paragraph format and hence is not appealing to users but this new way of presenting this information would increase not only the curiosity but also read more laws which was our goal to begin with. User can select the continents that they need to know more laws about and select the country which then provides laws passed with respect to gender equality in that country. We also mention if the laws are positive or negative by including a tooltip. Present information that are not necessarily interesting but vital for readers to know, in a way that hooks them and gets them to read it.

2. Complexity: The datasets for number of laws per country, WBL Index score and flag image database were merged to plot the left graph. An ID was added to this data as well as to the reforms database to map country flags to their timelines. A add_selection property was added to filter data in the left graph and transform_filter so as to transform data on right chart.Altair does not allow moving the customization of menu hence the html generated by altair had to edited manually. To add customizations for menu locations and chart spacing and interactions the tags associated with them were searched in the html and css style attribute was altered. The instructions for how to interact with the chart were also added by editing the altair generated html.


**Figure 13:** This plot is combination of a world map with markers and a line chart representing the progression of different indices based on the country selected from the Country Dropdown. This figure is extremely important to understand where a country stands and how it has improved laws and policies narrowing the gender gap across all aspects i.e. Mobility or freedom of movement, workplace balance, pay gap, legal marital reights, paternity and maternity leaves and benefits, estabilishing onself as an entrepreneur, division of assets and legal rights to pension pay. In a single view, a user is able to view the above indicators and also dig deeper into country data and understand how a country has evolved over the past 5 decades. 

**Innovative aspect:**

1. Complexity: For this chart, different libraries were used in R such as leaflet and crosstalk. The main complexity was to convert a data frame to a format that could be used for crossfiltering and multiple interactions between the world map, dropdown, slider and line chart. Combining data from 6 different columns in the dataset and adjusting the layout of all the filters and interactions was time consuming.

**Figure 14:** The plot is a sunburst chart with the number of maternity and paternity leaves (federal government granted) by country. Given that the Parenthood index has been consistently performing poorer than the other indicators, it is a supressing issue that needs to be addressed. Less than 16% of the economies have scored 100 on this index. The main reason behind choosing sunburst chart is that it represents the heirarchy of continents and countries well in a single view. Users can also compare the number of paid maternity and paternity leaves side by side and visually see the dip in numbers for the latter. 

Visualization Codes: https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/laws%20and%20regulations/codes

#### Reflection
Although the visualization goals remain the same, major improvements have been made to make the charts interactive and detail-oriented. Advanced Data visualization tools and techniques have been deployed to present a comprehensive chart as clearly and as visually attractive as possible. Consistent color themes, alignment and labeling has been maintained for each chart. Charts with multiple features and interactivity, each have a small explanation on how to navigate and use the chart which is a significant addition as compared to the proposal. 


## Summary of media coverage

#### Dataset & Data Processing
<!--Talk about data variables and source as well as cleaning-->
**Data**: Twitter and News API was used to get tweets and news articles respectively. The data for political speeches was downloaded from multiple websites and combined into a single dataset. The tweet data contains the user name and tweet. The news articles dataset contains new source, headline and content. Political speeches dataset only has one column wit the content of the speech.<br>

Scraping Codes link: https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/Text_Analysis/Code

Datasets link: https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/datasets

**Data Processing**:The text data was cleaned to remove stop words, links, punctuation, etc. and then the frequency of each word was extracted using count vectorizer. Top 100 words were selected from each dataset. The final datasets for each of the text datasets consist only of the top 100 words and their counts.

Code link: https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/Text_Analysis/Code

Cleaned datasets link: https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/datasets


#### Design Choices
<!--For each figure describe why is it important and the design choices-->
**Figure 15:** The idea of summarizing articles, tweets and speeches is to find what subtopics are most spoken about and what direction should efforts to decrease wage gap be made. The drop-down menu allows the users to choose between tweets, news and speeches. The reason to keep the charts separate is because news articles have more information on the current status, tweets are peoples opinions and political speeches talk about current laws and future actions hence, each of them looks at the topic from a different aspect. Bubble plot was used instead of a wordcloud for better clarity instead of words since 100 words were used for each chart. The color scheme for news and political speeches is used to match the theme of the site. Blue gradient is used for tweets as the color for twitter logo is blue and also this matches the orange and blue theme of the site.

Visualization Codes: https://github.com/anly503/project-spring-2022-projectgroup21/tree/main/Text_Analysis/Code


#### Reflection
<!-- How different are they from the proposal? What would you change or failed to implement-->
The style of the chart has not changed much from the proposal. The color scheme has changed from the midpoint to have a more coherent theme for the website. The chart also mentions the time period of the data as suggested in the feedback given. The original idea was for this chart to be automatically updated every month so the website could actually look at the current summaries and have the users form their own insights. However, without having dash and a backend server this implementation was not possible. The findings from this chart are helpful and do highlight certain topics but if it could be updated that would make it more relevant
