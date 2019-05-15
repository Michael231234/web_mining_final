import numpy as np
from scipy.spatial import distance

# users number, use 0 to 100836 to label them
users = 100836
# movie numbers, ues 0 to 20766 to label them
movies = 20766
# number of movies genres
genre_num = 21
# All Genres
genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy',
          'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy',
          'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
          'Mystery', 'Romance', 'Sci-Fi', 'Short', 'Talk-Show',
          'Thriller', 'War', 'Western']
# users’ data
user_raw = np.loadtxt("new_data.csv", str, delimiter=',')
# recommend 3 movies
guess = 3
# choose the similar users
selection = 5
# get the movie data
base = np.loadtxt("IMDb.csv", int)
# initialization: default every user take -1 to every movie, which means these is no rate about the movie
# rate is a Two-dimension , row is user and column is movies
rate = np.ones([users, movies])*(-1)

# get the base data into the rate table
for j in range(base.shape[0]):
    rate[base[j, 0]-1, base[j, 1]-1] = base[j, 2]
avg = np.zeros(users)
std = np.zeros(users)

for j in range(users):
    tem = rate[j, :]
    tem = tem[tem != -1]
    avg[j] = (tem.sum()+0.0)/tem.shape[0]
    std[j] = np.std(tem)
rate_V = np.zeros([users, movies])

for j in range(users):
    rate_V[j, :] = avg[j]*np.ones(movies)
rate_V[rate != -1] = rate[rate != -1]
# Z-normalization

for i in range(users):
    for j in range(movies):
        rate_V[i, j] = (rate_V[i, j]-avg[i])/std[i]


def compute_dist1(user_guess):
    # tem_1d is one-dimension data
    tem_1d = rate_V[user_guess, :]
    # turn tem_1d into two-dimension data
    tem_2d = np.zeros([1, movies])
    tem_2d[0, :] = tem_1d
    # According to the movie genres which users has watched to recommend
    # Calculate any two users of Euclidean distance, the smaller  distance on behalf of the more similarity
    dist = distance.cdist(tem_2d, rate_V, 'euclidean')
    # get the results turn into one-dimension data
    dist = dist[0, :]
    return dist


def compute_dist2(user_guess):
    user_data = np.zeros([users, genres_num+4])
    for j in range(user_raw.shape[0]):
        if user_raw[j, 2] == 'M':
            user_data[j, genre_num] = 1
        for k in range(genre_num):
            if user_raw[j, 3] == genres[k]:
                user_data[j, k] = 1
                break
    tem_1d = user_data[user_guess, :]
    tem_2d = np.zeros([1, jobs_num+4])
    tem_2d[0, :] = tem_1d
    dist = distance.cdist(tem_2d, user_data, 'rating')
    dist = dist[0, :]
    return dist


def recom(dist, i, user_guess):
    # Initial the guessed movie rates
    pred = np.ones(movies)*(-100)
    for j in range(movies):
        # Take guess when the movies have no rates
        if rate[user_guess, j] == -1:
            tem = np.array([rate_V[:, j], dist]).T
            # Select all of the film have rate of the rating of other users
            tem = tem[rate[:, j] != -1]
            # according the distance to sort the data
            tem = tem[tem[:, 1].argsort()]
            # get all the rating
            tem = tem[:, 0]
            if tem.shape[0] > selection:
                tem = tem[0:selection]
            if tem.shape[0] > 0:
                pred[j] = (tem.sum()+0.0)/tem.shape[0]
    tem = np.array([range(movies), pred]).T
    # delete all the movies which has rated
    tem = tem[rate[:, user_guess]!=-1]
    tem = tem[tem[:, 1].argsort()][::-1]
    print("the algorithm %d recommend the movie:" % i)
    print(tem[0:guess, 0])


if __name__ == '__main__':
    user_guess = int(raw_input("Please input the number of the UserID (0 to 100836):\n"))
    if user_guess not in range(100837):
        print("We do not have this user!")
        exit(0)
    dist1 = compute_dist1(user_guess)
    dist2 = compute_dist2(user_guess)
    a = 0.3
    dist3 = dist1+a*dist2
    recom(dist1, 1, user_guess)
    recom(dist2, 2, user_guess)
    recom(dist3, 3, user_guess)
