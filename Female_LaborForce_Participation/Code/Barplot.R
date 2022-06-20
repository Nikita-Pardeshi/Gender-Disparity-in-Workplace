#####################################################################################
# ANLY 503 Project: Interactive, Data-driven Visual Narrative
#
####################################################################################


# Import libraries
library(tidyverse)
library(gganimate)


################### READ DATASET ##########################################
data <- read.csv("./datasets/female-employment-to-population-ratio.csv")
names(data)
str(data)


# rename
## RENAME column names
names(data)[names(data) == "Entity"] <- "country_name"
names(data)[names(data) == "Employment.to.population.ratio.female...."] <- "employment_to_population_ratio"


# select required columns
# selecting top 10 countries in gender imquality order
data <- data %>% filter(Code == "AUS" | Code == "USA" | Code == "ISL" |
  Code == "CHE" | Code == "FIN" | Code == "CHE" |
  Code == "CAN" | Code == "RUS" | Code == "ZAF" | Code == "SWE" | Code == "NZL")
data <- data %>% filter(Year > "1995")

# replace NAs with 0
data[is.na(data)] <- 0


# Data Manipulation:
data_formatted <- data %>%
  group_by(Year) %>%
  mutate(
    rank = rank(-employment_to_population_ratio),
    Value_rel = employment_to_population_ratio / employment_to_population_ratio[rank == 1],
    Value_lbl = paste0(" ", (employment_to_population_ratio))
  ) %>%
  group_by(country_name) %>%
  filter(rank <= 10) %>%
  ungroup()




#-----------------------
# GGPLOT2 VISUALIZATION
#-----------------------
# Building Static Plots
staticplot <- ggplot(data_formatted, aes(rank,
  group = country_name,
  fill = as.factor(country_name)
)) +
  geom_tile(aes(
    y = employment_to_population_ratio / 2,
    height = employment_to_population_ratio,
    width = 0.9
  ), alpha = 0.8, color = NA) +
  geom_text(aes(y = 0, label = paste(country_name, " ")), vjust = 1, hjust = 1, size = 6) +
  geom_text(aes(y = employment_to_population_ratio, label = paste(Value_lbl, "%")), hjust = 0, size = 5) +
  coord_flip(clip = "off", expand = FALSE) +
  scale_y_continuous(labels = scales::comma) +
  scale_x_reverse() +
  guides(color = FALSE, fill = FALSE) +
  theme(
    axis.line = element_blank(),
    axis.text.x = element_blank(),
    axis.text.y = element_blank(),
    axis.ticks = element_blank(),
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    legend.position = "none",
    panel.background = element_blank(),
    panel.border = element_blank(),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_line(size = .1, color = "grey"),
    panel.grid.minor.x = element_line(size = .1, color = "grey"),
    plot.title = element_text(size = 21, hjust = 0.5, face = "bold", colour = "black", vjust = -1),
    plot.subtitle = element_text(size = 20, hjust = 0.5, face = "italic", color = "grey"),
    plot.caption = element_text(size = 15, hjust = 0.5, face = "italic", color = "grey"),
    plot.background = element_blank(),
    plot.margin = margin(2, 2, 2, 6.5, "cm")
  ) +
  scale_fill_manual("legend", values = c(
    "Iceland" = "blue",
    "Sweden" = "lightblue",
    "Switzerland" = "dodgerblue1",
    "Australia" = "dodgerblue2",
    "South Africa" = "dodgerblue3",
    "Finland" = "dodgerblue4",
    "United States" = "dodgerblue",
    "Canada" = "deepskyblue1",
    "New Zealand" = "deepskyblue2",
    "Russia" = "deepskyblue3"
  ))




# adding animation to the plot
anim <- staticplot + transition_states(Year, transition_length = 0.01, state_length = 1) +
  view_follow(fixed_x = TRUE) +
  labs(
    title = "Female Employment to Population Ratio : {closest_state}",
    subtitle = "Top 10 Countries",
    caption = "Female employment- to-population ratio | Data Source: World Bank Data"
  )



# Save the plot
# For GIF
animate(anim, 200,
  fps = 8, width = 800, height = 700,
  renderer = gifski_renderer("invertedbarplot-1.gif")
)
