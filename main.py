import time
import schedule
import twitterapi
import cloudfs

def post_tweet():
  sentence = cloudfs.get_random_document()
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