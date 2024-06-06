## News API Exercise 

# Use the NewsAPI and the requests module to fetch the daily news related to different topics. 
#Go to: https://newsapi.org/ and explore the various options to build you application

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='#####')

print("We are going to present you top 10 news of the day. \n \n")

top_headlines = newsapi.get_top_headlines(language='en', country='us')
articles = top_headlines['articles']
i = 1
for news in articles:
    if (i == 10):
        break
    if news['title'] != '[Removed]':
        print(news['title'])
        print()
        i +=1 