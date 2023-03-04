import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "cdmx"
tweets = []
limit = 10

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

data = pd.DataFrame(tweets, columns = ['Date', 'User', 'Tweet'])
print(data)