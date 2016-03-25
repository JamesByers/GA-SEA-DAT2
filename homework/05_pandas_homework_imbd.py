'''
Pandas Homework with IMDb data
'''

'''
BASIC LEVEL
'''

import pandas as pd
import matplotlib.pyplot as plt

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
file_path_movies= '/Users/reneehosogi/Documents/GitHub_Clones/GA-SEA-DAT1/data/'
url = file_path_movies + 'imdb_1000.csv'
movies= pd.read_csv(url, header=0, na_filter=False)

# check the number of rows and columns
movies.shape


# check the data type of each column
movies.dtypes

# calculate the average movie duration
movies.duration.values.mean()

# sort the DataFrame by duration to find the shortest and longest movies
movies.duration.values.min()
movies.duration.values.max()

# create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind='hist', bins=250)

# use a box plot to display that same data
movies.duration.plot(kind='box')


'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.content_rating.value_counts()


# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar', title='Movie Ratings')
plt.xlabel('Movie Rating')
plt.ylabel('Number of Movies')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.rename(columns={'not rated':'unrated', 'approved':'unrated', 'passed':'unrated', 'gp':'unrated'})

# convert the following content ratings to "NC-17": X, TV-MA
movies.rename(columns={'x':'NC-17', 'tv-ma':'NC-17'})

# count the number of missing values in each column
movies.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values
movies.content_rating.isnull
movies.content_rating.fillna(value='NA', inplace=True)

# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
rating_bool = movies.duration > 120
movies[rating_bool]
movies[movies.duration > 120].star_rating.value_counts() 
movies[movies.duration < 120].star_rating.value_counts() 


# use a visualization to detect whether there is a relationship between duration and star rating
movies.groupby('star_rating').mean().plot(kind= 'bar')

# calculate the average duration for each genre
movies.groupby(['genre']).duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
movies.boxplot(column='duration', by='content_rating')

# determine the top rated movie (by star rating) for each genre
movies.groupby('star_rating').max()


# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies.duplicated().sum()

# calculate the average star rating for each genre, but only include genres with at least 10 movies



'''
BONUS
'''

# Figure out something "interesting" using the actors data!
