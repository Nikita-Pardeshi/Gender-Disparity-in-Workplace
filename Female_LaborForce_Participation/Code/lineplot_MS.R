#####################################################################################
# ANLY 503 Project: Interactive, Data-driven Visual Narrative
#
####################################################################################


# Import libraries
library(dplyr)
library(plotly)


################### READ DATASET ##########################################
data <- read.csv("./datasets/FL_maritial_status.csv")
names(data)
str(data)


# rename
## RENAME column names
names(data)[names(data) == "Single..never.married"] <- "Single,never married"
names(data)[names(data) == "All.women"] <- "All women"
names(data)[names(data) == "Married.women..spouse.present"] <- "Married women,spouse present"


# convert data format
data_n <- data %>%
  pivot_longer(c("Single,never married", "All women", "Others", "Married women,spouse present"), names_to = "maritial_status", values_to = "value")



#-----------------------
# PLOTLY VISUALIZATION
#-----------------------
# define style attributes
t <- list(
  family = "Arial",
  size = 15,
  color = "black"
)


# create the interactive plot
p <- plot_ly(
  data = data_n,
  x = ~Year,
  y = ~value,
  group = ~maritial_status,
  color = ~maritial_status,
  colors = c("deepskyblue1", "blue", "skyblue", "skyblue1"),
  type = "scatter",
  mode = "lines+markers"
) %>%
  layout(
    title = list(text = "LabourForce Participation of Women in the USA by Marital Status", font = t),
    plot_bgcolor = "#e5ecf6", xaxis = list(title = "Year"),
    hovermode = "x unified",
    yaxis = list(title = "Labor Force Participation (%)", ticksuffix = "%"),
    legend = list(title = list(text = "<b> Marital Status </b>"), orientation = "h", xanchor = "center", x = 0.5, y = -0.15)
  )



# Save the plot
htmlwidgets::saveWidget(as_widget(p), "lineplot_maritalStatus.html")
