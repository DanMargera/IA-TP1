import json
import pandas as pd
import preprocess as pre

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
    df.loc[:,'text'] = df.text.apply(lambda txt : pre.process(txt))
    debug(df)
    debug("-- Positive:", len(df[df.sentiment == 1].index))
    debug("-- Neutral:", len(df[df.sentiment == 0].index))
    debug("-- Negative:", len(df[df.sentiment == -1].index))
    return df

if __name__ == '__main__':
    prepare_dataframe()