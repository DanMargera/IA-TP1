import json
import sys

file_names = sys.argv[1:]
tweet_dict = dict()
limit = str()

for file_name in file_names:
    with open(file_name, 'r') as data:
        with open("out.txt", 'a') as out_file:
            for line in data:
                if line != '\n' and line != '\r':
                    tweet = json.loads(line)
                    try:
                        tweet_id = tweet['id']
                        full_text = tweet['extended_tweet']['full_text']
                    except:
                        # print(tweet['id'])
                        try:
                            full_text = tweet['text']
                        except:
                            limit = tweet['limit']
                    finally:
                        # print((tweet_id +": "+ full_text).encode('utf-8'))
                        if not limit:
                            tweet_dict.update({tweet_id: full_text})
                        else:
                            limit = ''
            out_file.write(json.dumps(tweet_dict, indent=4))
