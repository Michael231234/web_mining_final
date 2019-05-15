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
    df = pd.read_csv('J:\\final\\IMDb.csv')

    return df


stop_words = set(stopwords.words('english') + list(punctuation))
max_cut = 0.9
min_cut = 0.1


def compute_frequencies(word_sent):
    freq = defaultdict(int)

    for s in word_sent:
        for word in s:
            if word not in stop_words:
                freq[word] += 1

    try:
        m = float(max(freq.values()))
    except ValueError:
        print('err')

        for w in list(freq.keys()):
            freq[w] = freq[w]/m
            if freq[w] >= max_cut or freq[w] <= min_cut:
                del freq[w]

    return freq

def store_key_word():
    df = load_data()
    for i in range(len(df)):
        text = df['storyLines'][i]
        try:
            sents = sent_tokenize(text)
        except TypeError:
            print('err')
        else:
            word_sent = [word_tokenize(s.lower()) for s in sents]
            fre = compute_frequencies(word_sent)
            rev_fre = sorted(fre.items(), key=lambda d: d[1], reverse=True)
            count = 0
            f = []
            for item in rev_fre:
                if count == 3:
                    break
                try:
                    f.append(re.findall(r'[a-z]+', str(item))[0])
                except IndexError:
                    print(df['title'][i])
                count += 1

            words = ''
            for w in f:
                words += w+' '
            print(words)
            df['keywords'][i] = words



    print(df)

    df.to_csv("J:\\final\\search1.csv")


store_key_word()
