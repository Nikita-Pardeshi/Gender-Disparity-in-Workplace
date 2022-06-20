




# install.packages("twitteR")
# install.packages("ROAuth")
# install.packages("rtweet")
library(rtweet)
library(twitteR)
library(ROAuth)
library(jsonlite)

#######################################################



consumer_key='JTxsx4HozzSso47i1UbpduPmP'
consumer_secret='fvwO4knHeafB4699ksHm8wNaXJLuKzTjGVadLMX83WhK46zA6b'
access_token='1435636445922922498-6W9cE9cP8ovhyhuEMfpkOVX1CTkDdy'
access_secret='jzJMCkuKQ368BzVjCmFvlRUkfRN7DerwyoCtf0KCblyBv'

##################################################################

requestURL='https://api.twitter.com/oauth/request_token'
accessURL='https://api.twitter.com/oauth/access_token'
authURL='https://api.twitter.com/oauth/authorize'

create_token(
  app             = "Fitnessapp95",
  consumer_key    = consumer_key,
  consumer_secret = consumer_secret,
  access_token    = access_token,
  access_secret   = access_secret)


rstats_tweets <- search_tweets(q ='#equalpay' ,
                               include_rts = FALSE, tweet_mode = "extended",langs='en',n=500)



genderpaygap<-rstats_tweets[,c('screen_name','text')]


FName = "GenderpayGap3.csv"
## Start the file
write.csv(genderpaygap,FName)
