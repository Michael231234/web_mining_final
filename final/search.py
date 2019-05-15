import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from heapq import nlargest
from collections import defaultdict


# nltk.download('stopwords')
# nltk.download('punkt')


def load_data():
    df = pd.read_csv('J:\\final\\search1.csv')

    return df


def word_search(user_input, type):
    df = load_data()
    collection = np.asarray(df[type])
    suggestions = []
    pattern = user_input
    regex = re.compile(pattern, re.I)
    rows = []
    for item in collection:
        match = regex.search(str(item))
        if match:
            for r in df[(df[type] == item)].index.tolist():
                rows.append(r)
                suggestions.append(df.loc[r])
    return suggestions
