
library(tidyverse)
library(ggplot2)
library(forecast)
library(astsa)
library(xts)
library(tseries)
library(fpp2)
library(fma)
library(lubridate)
library(TSstudio)
library(quantmod)
library(tidyquant)
library(plotly)
library(TSstudio)
library(ggalt)
library(readxl)
library(kableExtra)
library(ggtext)
library(fpp3)

df2 <- read.csv("../datasets/share-of-women-in-top-income-groups.csv")
df3 <- df2 %>% group_by(Entity) %>% filter(Year == '2013'| Year == '2006')

# rename column names and delete the code
df3 <-  subset(df3, select = -c(Code,`Share.of.women.in.top.1.`,`Share.of.women.in.top.5.` ))
colnames(df3) <- c("country","year", "%women")

#conevrting year to factor
names <- c('year','country')
df3[,names] <- lapply(df3[,names] , factor)

#setting paired so that start and end of the scatters are selected
paired <- rep(1:8,each=2)

df_dub <- df3
df_dub[4] <- paired
colnames(df_dub)[4] <- "paired"

df_dub$country <- reorder(df_dub$country, df_dub$`%women`)

p <- df_dub %>% 
  ggplot(aes(x= `%women`,y= country)) +
  geom_line(aes(group = paired),color="grey")+
  geom_point(aes(color=year), size=4) +
  labs(y="Country",
       x="% of Women in Top 10 income group",
       ) +
  theme_classic()+
scale_color_manual(values=c("Orange", "Blue")) +
  ggtitle("  Change in % of women representing top 10% income groups from <span style = 'color: orange;'> 2006</span> and <span style = 'color: blue;'>2013</span>")
  

ggplotly(p)

