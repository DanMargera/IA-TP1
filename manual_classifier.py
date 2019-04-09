import json
import msvcrt
import sys

def save_and_exit(filename, data):
    with open(filename, 'w') as file:
        file.write(json.dumps(data, indent=4))
    exit()

def classify(data, key, tweet_text, filename):
    print('--------------------------------')
    print(tweet_text)
    print('Positive(P) Negative(N) Neutral(Any Key) Quit(Q)')
    input = msvcrt.getch()
    if (input == b'p' or input == b'P'):
        data[key]["sentiment"] = 1
    elif (input == b'n' or input == b'N'):
        data[key]["sentiment"] = -1
    elif (input == b'q' or input == b'Q'):
        save_and_exit(filename, data)
    else:
        data[key]["sentiment"] = 0

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError as error:
        print('Error! No file passed as argument')
        print('Usage: manual_classifier.py your_data_file.json')
        exit()

    data = json.loads(open(filename).read())
    for k,v in data.items():
        if (v["sentiment"] == 99):
            classify(data, k, v['text'], filename)

    save_and_exit(filename, data)