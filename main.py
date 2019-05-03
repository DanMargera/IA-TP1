import json
import pandas as pd
import preprocess as pre
import MTLClassifier as model

DATA_FILES = {
    "classified_02_20.json",
    "classified_03_05.json",
    "classified_03_06.json",
    "classified_03_09.json",
    "classified_03_10.json"
}

def debug(*args, **kwargs):
    # Use this to disable/enable debugging
    if (True):
        print(*args, **kwargs)

def prepare_dataframe():
    df = pd.DataFrame()
    for fname in DATA_FILES:
        with open("classified_data/"+fname, "r") as file:
            df = pd.concat([df, pd.read_json(file, orient='index')])
    df = df.reset_index(drop=True)
    df.loc[:,'text'] = df.text.apply(lambda txt : pre.process(txt))
    debug(df)
    debug("-- Positive:", len(df[df.sentiment == 1].index))
    debug("-- Neutral:", len(df[df.sentiment == 0].index))
    debug("-- Negative:", len(df[df.sentiment == -1].index))
    df.loc[:,'sentiment'] = df.sentiment.apply(lambda s : (s+1))
    positive_df = df[df.sentiment == 2]
    neutral_df = df[df.sentiment == 1]
    negative_df = df[df.sentiment == 0]
    train_df = pd.concat([positive_df[0:108], neutral_df[0:108], negative_df[0:108]]).sample(frac=1).reset_index(drop=True) # shuffle
    debug(train_df)
    test_df = pd.concat([positive_df[108:128], neutral_df[108:128], negative_df[108:128]]).sample(frac=1).reset_index(drop=True) # shuffle
    debug(test_df)
    return train_df, test_df

if __name__ == '__main__':
    train_df, test_df = prepare_dataframe()
    classifier = model.MTLClassifier(train_df, test_df, 3, 'sentiment', 'text')
    classifier.run()