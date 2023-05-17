# Import the dotenv and os and tweey module
import dotenv
import os
import twitter
import tweepy
# Load the environment variables from the .env file
dotenv.load_dotenv()

# Access the environment variables in your Python3 file
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET =  os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN =  os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

# Create an API object
client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Define a function to tweet a random sentence from a paragraph
def tweet_random_sentence(sentence):
  client.create_tweet(text=sentence)
