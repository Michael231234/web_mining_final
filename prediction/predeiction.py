import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.externals import joblib
from sklearn.model_selection import cross_val_score


def load_data(user):
    df = pd.read_csv('J:\\PycharmProjects\\prediction\\new_data.csv')
    data = df.drop(['genres', 'timestamp', 'title', 'rating'], axis=1)
    clf = joblib.load('J:\\PycharmProjects\\prediction\\decision_tree.pkl')
    x = data
    print(np.isnan(x))
    print(np.where(np.isnan(x)))
    pre = []
    watched_movies = []
    rec_movies = []
    for i in range(len(x)):
        if x['userId'][i] == user:
            watched_movies.append(x['movieId'][i])
    print(watched_movies)
    for i in range(len(x)):
        # print(type(x['userId'][i]))
        # print(x['userId'][i])
        movie_id = x['movieId'][i]
        if (x['userId'][i] != user) and (movie_id not in watched_movies):
            watched_movies.append(movie_id)
            print(movie_id)
            new_x = np.nan_to_num(x.drop(['movieId'], axis=1))
            y_pre = clf.predict([new_x[i]])
            if y_pre >= 4.5:
                rec_movies.append(int(movie_id))
                pre.append({int(movie_id): y_pre})
        else:
            continue
        if len(pre) == 5:
            break
    print(pre)

    return rec_movies


rec = []
userId = []
for i in range(1, 6):
    userId.append(i)
    print(type(load_data(i)))
    rec.append(load_data(i))

rec_df = pd.DataFrame({'userId': userId, 'moviesId': rec})
rec_df.to_csv('rec.csv')
print(rec)
