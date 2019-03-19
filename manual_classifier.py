import json
import msvcrt
import sys

def classify(tweet_text):
    print('--------------------------------')
    print(tweet_text)
    print('Positive(P) Negative(N) Neutral(Any Key)')
    input = msvcrt.getch()
    if (input == b'p' or input == b'P'):
        return {
            "text" : tweet_text,
            "sentiment" : 1
        }
    elif (input == b'n' or input == b'N'):
        return {
            "text" : tweet_text,
            "sentiment" : -1
        }
    else:
        return {
            "text" : tweet_text,
            "sentiment" : 0
        }

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError as error:
        print('Error! No file passed as argument')
        print('Usage: manual_classifier.py your_data_file.json')
        exit()

    data = json.loads(open(filename).read())
    classified_data = dict()
    for k,v in data.items():
        classified_data.update({k : classify(v)})

    with open('classified_'+filename, 'w') as file:
        file.write(json.dumps(classified_data, indent=4))