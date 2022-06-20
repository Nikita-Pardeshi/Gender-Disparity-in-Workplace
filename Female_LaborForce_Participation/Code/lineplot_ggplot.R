#####################################################################################
# ANLY 503 Project: Interactive, Data-driven Visual Narrative
#
####################################################################################


# Import libraries
library(readr)
library(dplyr)
library(plyr)
library(tidyverse)
library(dplyr)
library(varhandle)
library(reshape)
library(tidyr)
library(ggplot2)
library(gganimate)
library(hrbrthemes)


# Theme definition for ggplot
th <- ggplot2::theme(
  plot.title = element_text(color = "#003366", size = 12, face = "bold"),
  axis.title.x = element_text(color = "black", size = 11, face = "bold"),
  axis.title.y = element_text(color = "black", size = 11, face = "bold"),
  panel.background = element_rect(
    fill = "white",
    colour = "white",
    size = 0.5, linetype = 2
  ),
  panel.grid.major = element_line(
    size = 0.5, linetype = 2,
    colour = "gray80"
  ),
  panel.grid.minor = element_line(
    size = 0.25, linetype = 2,
    colour = "gray80"
  ),
  axis.line = element_line(size = 0.53, colour = "black"),
  panel.border = element_rect(linetype = 1, fill = NA, size = 0.53),
  axis.text = element_text(colour = "black", face = "bold", size = 10)
)



################### READ DATASET ##########################################
df <- read.csv("./datasets/laborforce_changes.csv")
head(df)


# Filter out the required columns
df_n <- df %>% filter(Code == "AUS" | Code == "USA" | Code == "DEU" | Code == "ISL" | Code == "SWE" | Code == "CAN")
df_nn <- df_n %>% filter(Year > "1960")


# Rename column names
names(df_nn1)[names(df_nn1) == "Entity"] <- "Country"



#-----------------------
# GGPLOT2 VISUALIZATION
#-----------------------

p <- ggplot(
  df_nn,
  aes(Year, Female_labor_force_participation_rate, group = Country, color = (Country))
) +
  geom_line(size = 1.2) +
  geom_point(size = 2.5, color = "red") +
  scale_color_viridis_d() +
  labs(x = "Year", y = "Female_labor_force_participation_rate") +
  theme(legend.position = "right") +
  theme_bw(base_size = 15) +
  th +
  scale_y_continuous(labels = function(x) paste0(x, "%"))


# Adding animation
p +
  geom_point(aes(group = seq_along(Year))) +
  transition_reveal(Year) + ggtitle("Female Labour force Participation Rates, 1960-2020") +
  ylab("Labor Force Participation Rate (%)")


# Save the animated plot
anim_save("plot.gif", height = 800, width = 800)
