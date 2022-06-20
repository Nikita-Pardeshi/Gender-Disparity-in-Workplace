from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re
from sklearn.feature_extraction import text

My_Content_List = []


with open("./datasets/Political Speeches.csv", "r") as News:
    next(News)  ## skipping the first row

    for next_row in News:
        tweet=next_row
        temp = tweet.lower()
        temp = re.sub("'", "", temp)  # to avoid removing contractions in english
        temp = re.sub("@[A-Za-z0-9_]+", "", temp)
        temp = re.sub("#[A-Za-z0-9_]+", "", temp)
        temp = re.sub(r'http\S+', '', temp)
        temp = re.sub('[()!?]', ' ', temp)
        temp = re.sub('\[.*?\]', ' ', temp)
        temp = re.sub("[^a-z0-9]", " ", temp)
        My_Content_List.append(temp)


my_additional_stop_words=["new","just","said","like","say","com","el","li","di","amp","das","der","des","did","en","il","ist","la","und",
"uswnt","ve","mit","von","know","ein","dont","got","actually","don","doing","day","going","sure","thank","today","vice","want",0,"able","does"]
stop_words = text.ENGLISH_STOP_WORDS.union(my_additional_stop_words)
MyCV_content = CountVectorizer(input='content',
                               stop_words=stop_words,
                               max_features=120
                               )
My_DTM2 = MyCV_content.fit_transform(My_Content_List)

ColNames = MyCV_content.get_feature_names()
My_DF_content = pd.DataFrame(My_DTM2.toarray(), columns=ColNames)
My_DF=pd.DataFrame(My_DF_content.sum(),columns=["value"])
My_DF.index.name = 'id'
My_DF.reset_index(inplace=True)

My_DF.to_csv("SpeechWordFrequency.csv")


