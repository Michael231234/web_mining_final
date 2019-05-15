import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.externals import joblib
from sklearn.model_selection import cross_val_score


def load_data():
    df = pd.read_csv('J:\\PycharmProjects\\prediction\\new_data.csv').drop(['movieId', 'genres', 'timestamp', 'title'],
                                                                      axis=1)
    x = df.drop(['rating'], axis=1).values
    y = df['rating'].values

    return df, x, y


def decision_tree(x, y):
    depth = []
    clf = tree.DecisionTreeRegressor(max_depth=4, criterion="mse", splitter="best", min_samples_split=2,
                                     min_samples_leaf=1, min_weight_fraction_leaf=0., max_features=None,
                                     random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.,
                                     min_impurity_split=None, presort=False)
    scores = cross_val_score(estimator=clf, X=x, y=y, cv=10, n_jobs=4)
    depth.append((4, scores.mean()))
    print(depth)
    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(x, y)
    joblib.dump(clf, 'J:\\PycharmProjects\\prediction\\decision_tree.pkl')


def main():
    df, x, y = load_data()
    print(np.isnan(x))
    print(np.where(np.isnan(x)))
    new_x = np.nan_to_num(x)
    decision_tree(new_x, y)


main()
# clf = joblib.load('J:\\PycharmProjects\\prediction\\decision_tree.pkl')

