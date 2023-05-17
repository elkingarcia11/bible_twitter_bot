import tweepy
import json
import biblejson

# Set your Twitter API credentials

# Create an OAuthHandler object
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# Set the access token and secret
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create an API object
api = tweepy.API(auth)

# Define a function to get a random sentence from a paragraph
def get_random_sentence(paragraph):
  sentences = paragraph.split(".")
  return random.choice(sentences)

# Define a function to tweet a random sentence from a paragraph
def tweet_random_sentence(paragraph):
  sentence = biblejson.get_random_sentence(paragraph)
  api.update_status(sentence)

# Get the paragraph of input from the user
paragraph = input("Enter a paragraph of text: ")

# Tweet the random sentence
tweet_random_sentence(paragraph)