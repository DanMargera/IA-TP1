import json
import sys

raw_file_name = sys.argv[1]

tweet_dict = dict()

with open(raw_file_name, 'r') as data:
    with open("out.txt", 'w') as out_file:
        for line in data:
            if line != '\n':
                tweet = json.loads(line)
                tweet_id = tweet['id']
                try:
                    full_text = tweet['extended_tweet']['full_text']
                except:
                    full_text = tweet['text']
                finally:
                    # print((tweet_id +": "+ full_text).encode('utf-8'))
                    tweet_dict.update({tweet_id: full_text})
        out_file.write(json.dumps(tweet_dict, indent=4))