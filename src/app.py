import os
import requests 
import tweepy
import pandas as pd 
from dotenv import load_dotenv
import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Step 1: Create a twitter developer account https://developer.twitter.com/  = OK
#Step 2: Initial setup  Create an app.py file inside the ./src/ folder. Install tweepy using PIP. =OK
#Step 3: Environment variables OK

# load the .env file variables
load_dotenv()

consumer_key  = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
bearer_token= os.getenv('bearer_token')

#Step 4: Innitialize the tweepy library Import Tweepy and requests library and tweepy.Client().
# Creando cliente de Twitter

client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret,
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

#Step 5: Start making requests to the API 100 tweets  Definiendo el query para Tweeter = ok 
#Make a query: Search tweets that have the hashtag #100daysofcode and the word python or pandas, from the last 7 days (search_recent_tweets).
#Do not include retweets. Limit the result to a maximum of 100 Tweets.
#Also include some additional information with tweet_fields (author id, when the tweet was created, the language of the tweet text).

query = '#100daysofcode (pandas OR python) -is:retweet'      

tweets = client.search_recent_tweets(query=query, 
                                    tweet_fields=['author_id','created_at','lang'],
                                     max_results=100)

# Save data as dictionary
tweets_dict = tweets.json() 
list(tweets_dict)
# Extract "data" value from dictionary
tweets_data = tweets_dict['data'] 
# Transform to pandas Dataframe
df = pd.json_normalize(tweets_data)
tweets_data
list(tweets_data[0])
df.describe()
df.head()
#https://twittercommunity.com/t/saving-tweet-to-csv/153357/4
# save df
df.to_csv('coding-tweets.csv') #save the csv file into our computer
### Step 7: Search for the words

#Now that you have your DataFrame of tweets set up, you're going to do a bit of text analysis to count how many tweets contain the words 'pandas', and 'python'. Define the following function word_in_text(), which will tell you whether the first argument (a word) occurs within the 2nd argument (a tweet). 

#> Make sure to convert any word or tweet text into lowercase.
#> You can use the re python library (regular expression operations). See the documentation for guidance: https://docs.python.org/3/library/re.html#


#1. import de `re` library using `import re` =ok
#2. Define your `word_in_text` function and implement the code. = ok

df= pd.read_csv('coding-tweets.csv')
#print(df_tweets.to_string()) 
lowercaseString = df.to_string().lower()
keys = "pandas|python"
p = re.compile(u'\\b(?iu)(?P<name>(%s))\\b' % keys)
print(p) 

### Step 11:

#Iterate through dataframe rows counting the number of tweets in which pandas and python are mentioned, using your word_in_text() function.

#1. Initialize list to store tweet counts = ok 
#2. Iterate through df, counting the number of tweets in which each(pandas and python) is mentioned. =ok

def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

# Print head of DataFrame
print(df.head())
 
 #iterate over the rows of the DataFrame and calculate how many tweets contain
 #each of our keywords! The list of objects for each candidate has been
 #initialized to 0

# 1. Initialize list to store tweet counts = ok 
[pandas, python] = [0, 0]

# 2. Iterate through df, counting the number of tweets in which each(pandas and python) is mentioned. =ok
# each pandas and python is mentioned
for index, row in df.iterrows():
   pandas += word_in_text('pandas', row['text'])
   python += word_in_text('python', row['text'])
   ### Step 12: Visualize the data

#1. Import packages
#2. Set seaborn style
#3. Create a list of labels:cd
#4. Plot the bar chart
# first import seaborn as sns; you'll then construct a barplot of the
# data using sns.barplot, passing it two arguments: (i) a list of labels and
# (ii) a list containing e variables you wish to plot(clinton, trump and so on)

# Import packages

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['pandas', 'python']

# Plot histogram
ax = sns.barplot(cd, [pandas, python])
ax.set(ylabel="count")
plt.show()
