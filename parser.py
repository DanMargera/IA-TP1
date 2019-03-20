import json
import sys

file_names = sys.argv[1:]
tweet_dict = dict()

for file_name in file_names:
    with open(file_name, 'r') as data:
        with open("out.txt", 'a') as out_file:
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