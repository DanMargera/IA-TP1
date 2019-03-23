import json
import sys

file_names = sys.argv[1:]
tweet_dict = dict()
limit = str()

def isRetweet(tweet):
    if (tweet[:2].upper() == "RT"):
        return True
    else:
        return False

for file_name in file_names:
    with open(file_name, 'r') as data:
        print("Parsing file " + file_name)
        with open("out_"+file_name[14:], 'w') as out_file:
            tweet_dict.clear()
            # i = 0
            for line in data:
                # print("Parsing line " + str(i))
                if line != '\n' and line != '\r':
                    tweet = json.loads(line)

                    try:
                        tweet_id = tweet['id']
                        tweet_text = tweet['text']

                        if (isRetweet(tweet_text)):
                            full_text = tweet['retweeted_status']['extended_tweet']['full_text']
                        else:
                            full_text = tweet['extended_tweet']['full_text']

                    except:
                        try:
                            full_text = tweet['text']
                        except:
                            limit = tweet['limit']
                    finally:
                        if not limit:
                            tweet_dict.update({tweet_id: full_text})
                        else:
                            limit = ''
                # i += 1
            out_file.write(json.dumps(tweet_dict, indent=4))
