import requests

import re



BaseURL="https://newsapi.org/v2/everything"
URLPost = {'apiKey': 'd977a2154335402b92af59083c387fd0',
                    'q':'Equal Pay',
                    'language':'en',
                    'pageSize': 100,
                    'sortBy': 'relevance',

                    }

response=requests.get(BaseURL, URLPost)

jsontxt = response.json()
print(jsontxt)
# MyFILE=open("Genderpaygapnews.csv","w")
# ### Place the column names in - write to the first row
# WriteThis="Author,Title,Headline\n"
# MyFILE.write(WriteThis)
# MyFILE.close()


## Open the file for append
MyFILE=open("Genderpaygapnews.csv", "a")
for items in jsontxt["articles"]:
    # Some articles do not have authors setting them to anonymous so there is no error due to None
    if items["author"] is None:
        Author='Anonymous'
    else:
        Author=items["author"]
    print(Author)
    ## CLEAN the Title
    ##----------------------------------------------------------
    ##Replace punctuation with space
    # Accept one or more copies of punctuation
    # plus zero or more copies of a space
    # and replace it with a single space
    Title = items["title"]
    Title = re.sub(r'[,.;@#?!&$\-\']+', ' ', Title, flags=re.IGNORECASE)
    Title = re.sub(r'\ +', ' ', Title, flags=re.IGNORECASE)
    Title = re.sub(r'\"', ' ', Title, flags=re.IGNORECASE)
    print(Title)
    # and replace it with a single space
    ## NOTE: Using the "^" on the inside of the [] means
    ## we want to look for any chars NOT a-z or A-Z and replace
    ## them with blank. This removes chars that should not be there.
    Title = re.sub(r'[^a-zA-Z]', " ", Title, flags=re.VERBOSE)
    ##----------------------------------------------------------

    Headline = items["description"]
    Headline = re.sub(r'[,.;@#?!&$\-\']+', ' ', Headline, flags=re.IGNORECASE)
    Headline = re.sub(r'\ +', ' ', Headline, flags=re.IGNORECASE)
    Headline = re.sub(r'\"', ' ', Headline, flags=re.IGNORECASE)
    Headline = re.sub(r'[^a-zA-Z]', " ", Headline, flags=re.VERBOSE)
    print(Headline)
    # print("Author: ", Author, "\n")
    # print("Title: ", Title, "\n")
    # print("Headline News Item: ", Headline, "\n\n")

    WriteThis = Author + "," + Title + "," + Headline + "\n"

    MyFILE.write(WriteThis)

## CLOSE THE FILE
MyFILE.close()