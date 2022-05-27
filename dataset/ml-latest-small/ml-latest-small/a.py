import pandas as pd
# df = pd.read_csv("movies.csv")

def movies(request):
    df = pd.read_csv('movies.csv')
    for movieId, title, genres in zip(df.movieId, df.title, df.genres):
    models = movies(movieid = movieId, title=title, genres=genres)
    models.save()
    return redirect("loginapp:about")