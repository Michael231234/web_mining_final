import pandas as pd
import numpy as np

obj = [{'email': 'user1@example.com', 'password': 'example1'},
       {'email': 'user2@example.com', 'password': 'example2'},
       {'email': 'user3@example.com', 'password': 'example3'},
       {'email': 'user4@example.com', 'password': 'example4'},
       {'email': 'user5@example.com', 'password': 'example5'}]


def load_recommend(email):
    rec_df = pd.read_csv('J:\\final\\rec.csv')
    info_df = pd.read_csv('J:\\final\\search1.csv')
    print(np.asarray(rec_df['userId']))
    for i in range(len(rec_df)):
        e = 'user%d@example.com' % rec_df['userId'][i]
        print(e)
        rec_df['email'][i] = e
    print(rec_df['email'])
    if email in np.asarray(rec_df['email']):
        rows = []
        moviesId = np.asarray(rec_df[rec_df['email'].isin([email])]['moviesId'])[0].replace('[', '').replace(']', '')\
            .split(',')
        print(list(moviesId))
        suggestions = []
        for id in list(moviesId):
            print(id)
            print(type(info_df['imdbId']))
            for r in info_df[(info_df['imdbId'].isin([int(id)]))].index.tolist():
                rows.append(r)
                suggestions.append(info_df.loc[r])
        return suggestions
    else:
        return 'Not enough info'


def ver(email, password):
    for i in range(len(obj)):
        if (email == obj[i]['email']) & (password == obj[i]['password']):
            return True

    return False