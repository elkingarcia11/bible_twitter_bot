import biblejson
import twitterapi
import time

def main():
  while True:
    time.sleep(60)
    post_tweet()

def post_tweet():
  sentence = biblejson.get_random_sentence()
  twitterapi.tweet_random_sentence(sentence)    

if __name__ == "__main__":
  main()