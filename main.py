import biblejson
import twitterapi
import time
import schedule

def post_tweet():
  sentence = biblejson.get_random_sentence()
  twitterapi.tweet_random_sentence(sentence)

def main():
  # Schedule the function to run every 2 hours after midnight.
  post_tweet()
  schedule.every(2).hours.do(post_tweet)
  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()