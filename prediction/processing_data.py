import pandas as pd


def process_data():
    genome_scores = pd.read_csv('J:\\PycharmProjects\\prediction\\genome-scores.csv')
    movies = pd.read_csv('J:\\PycharmProjects\\prediction\\movies.csv')

    new_genome_scores = genome_scores.pivot_table(index='movieId', columns='tagId', values='relevance')
    c = [
        'Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy', 'Romance', 'Drama', 'Action', 'Crime', 'Thriller',
        'Horror', 'Mystery', 'Sci-Fi', 'War', 'Musical', 'Documentary', 'IMAX', 'Western', 'Film-Noir'
    ]
    # print(new_genome_scores)
    new_movies = pd.concat([movies, pd.DataFrame(columns=c)], sort=False)
    for i, r in new_movies.iterrows():
        for col in c:
            genres = new_movies.loc[i, 'genres']
            if col in genres:
                new_movies.loc[i, col] = 1
            else:
                new_movies.loc[i, col] = 0
    # print(new_movies)
    new_data = pd.concat([new_genome_scores, new_movies], sort=False)
    # for c in new_data.columns:
    #     print(c)
    new_data.to_csv("new.csv")

    return new_data


process_data()
# movies = pd.read_csv('J:\\PycharmProjects\\prediction\\new_data.csv')
# for c in movies.columns:
#     print(c)
