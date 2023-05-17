                                                                          
import biblejson
import twitterapi

def main():
  sentence = biblejson.get_random_sentence()
  twitterapi.tweet_random_sentence(sentence)


if __name__ == "__main__":
  main()