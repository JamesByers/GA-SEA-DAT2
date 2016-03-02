# # Visualization with Pandas (and Matplotlib)

import pandas as pd
import matplotlib.pyplot as plt

# display plots in the console

# increase default figure and font sizes for easier viewing
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14


# read in the drinks data
file_path_drinks = '/Users/jim_byers/Documents/GA/GA_Data_Science_course/SEA-DAT1/data/'
drink_cols = ['country', 'beer', 'spirit', 'wine', 'liters', 'continent']
url = file_path_drinks + 'drinks.csv'
drinks = pd.read_csv(url, header=0, names=drink_cols, na_filter=False)


# ## Histogram: show the distribution of a numerical variable

# sort the beer column and mentally split it into 3 groups
drinks.beer.order().values


# compare with histogram
drinks.beer.plot(kind='hist', bins=3)


# try more bins
drinks.beer.plot(kind='hist', bins=20)


# add title and labels
drinks.beer.plot(kind='hist', bins=20, title='Histogram of Beer Servings')
plt.xlabel('Beer Servings')
plt.ylabel('Frequency')


# compare with density plot (smooth version of a histogram)
drinks.beer.plot(kind='density', xlim=(0, 500))


# ## Scatter Plot: show the relationship between two numerical variables

# select the beer and wine columns and sort by beer
drinks[['beer', 'wine']].sort('beer').values


# compare with scatter plot
drinks.plot(kind='scatter', x='beer', y='wine')


# add transparency
drinks.plot(kind='scatter', x='beer', y='wine', alpha=0.3)


# vary point color by spirit servings
drinks.plot(kind='scatter', x='beer', y='wine', c='spirit', colormap='Blues')


# scatter matrix of three numerical columns
pd.scatter_matrix(drinks[['beer', 'spirit', 'wine']])


# increase figure size
pd.scatter_matrix(drinks[['beer', 'spirit', 'wine']], figsize=(10, 8))


# ## Bar Plot: show a numerical comparison across different categories

# count the number of countries in each continent
drinks.continent.value_counts()


# compare with bar plot
drinks.continent.value_counts().plot(kind='bar')


# calculate the mean alcohol amounts for each continent
drinks.groupby('continent').mean()


# side-by-side bar plots
drinks.groupby('continent').mean().plot(kind='bar')


# drop the liters column
drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar')


# stacked bar plots
drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar', stacked=True)


### Exercise 1#: Visualize the Pronto rider age data in a histogram
#
# read in the Pronto data and merge the two files
# read in the data from '2015_trip_data.csv' file into a dataframe names 'file_path' and examine the contents.
# name the file trip_data
#
###

## read in two files into separate dataframes
file_path_pronto = '/Users/jim_byers/Documents/GA/GA_Data_Science_course/SEA-DAT1/data/pronto_cycle_share/'

trip_data_url = file_path_pronto + '2015_trip_data.csv'
trip_data = pd.read_table(trip_data_url, sep=',', header=0)

station_data_url = file_path_pronto + '2015_station_data.csv'
station_data = pd.read_table(station_data_url, sep=',', header=0, usecols=['name','dockcount'])

## merge the two files on with left join on 'from_station_name' = 'name'
trip_and_dockcount_data = pd.merge(trip_data, station_data, how='left', left_on='from_station_name', right_on='name')
del trip_and_dockcount_data['name']

## create a new column of age where age is 2015 - birthyear
type(trip_and_dockcount_data.birthyear[1])  # this test shows that birthyear is a float in our dataframe rather than text. So do we do not have to convert birthyear to int of float for our calculation of age
trip_and_dockcount_data['age'] = 2015 - trip_and_dockcount_data.birthyear


trip_and_dockcount_data['age'] = 2015 - trip_and_dockcount_data.birthyear
trip_and_dockcount_data.age
type(trip_and_dockcount_data.age[1])  #this test shows that the age values are floats.  If we prefer we can change it it and integer.


## Display a histogram of the number of trips by age

# < your code here >

trip_and_dockcount_data.age.plot(kind='hist', bins=7)

## Re-display the histogram and add title and labels
# Title the chart "Histogram of # of rides by age"
# Label the x-axis "Age" and the 

# <your code here>
trip_and_dockcount_data.age.plot(kind='hist' , bins=7, title='Histogram of # of rides by age')
plt.xlabel('Age')
plt.ylabel('# of rides')

# Display a density plot for comparison
trip_and_dockcount_data.age.plot(kind='density', title='Density plot of # of rides by age')
plt.xlabel('Age')
plt.ylabel('Density of rides')



# ## Box Plot: show quartiles (and outliers) for one or more numerical variables
# 
# **Five-number summary:**
# 
# - min = minimum value
# - 25% = first quartile (Q1) = median of the lower half of the data
# - 50% = second quartile (Q2) = median of the data
# - 75% = third quartile (Q3) = median of the upper half of the data
# - max = maximum value
# 
# (More useful than mean and standard deviation for describing skewed distributions)
# 
# **Interquartile Range (IQR)** = Q3 - Q1
# 
# **Outliers:**
# 
# - below Q1 - 1.5 * IQR
# - above Q3 + 1.5 * IQR

#sort the spirit column
drinks.spirit.order().values


# show "five-number summary" for spirit
drinks.spirit.describe()


# display a box plot of spirits
drinks.spirit.plot(kind='box')


# include multiple variables
drinks.drop('liters', axis=1).plot(kind='box')


### Exercise 2: Display a box plot of the Pronto ride volume by age
##

#Display a box plot of age

# <your code goes here>
trip_and_dockcount_data.age.plot(kind='box', title='Box plot of # of rides by age')
plt.ylabel('# of rides first Pronto year')

## Bonus: State a conclusion you can make about the distribution of rider ages for the rides?
trip_and_dockcount_data.age.describe()

# <your statement and new code (if needed) go here>


# One statement that we can make is that half of our rides in the first year are from riders with ages
#  between 28 and 41.




# ## Line Plot: show the trend of a numerical variable over time

# read in the ufo data
file_path_ufo = '/Users/jim_byers/Documents/GA/GA_Data_Science_course/SEA-DAT1/data/'
url = file_path_ufo + 'ufo.csv'
ufo = pd.read_csv(url)
ufo['Time'] = pd.to_datetime(ufo.Time)
ufo['Year'] = ufo.Time.dt.year


# count the number of ufo reports each year (and sort by year)
ufo.Year.value_counts().sort_index()


# Look at trend with a line plot
ufo.Year.value_counts().sort_index()
ufo.Year.value_counts().sort_index().plot()
ufo.Year.value_counts().sort_index().plot(kind='line')

# don't use a line plot when there is no logical ordering
drinks.continent.value_counts().plot()



### Exercise 3: Display a line plot of the Pronto ride volume by day
###

type(trip_and_dockcount_data.starttime[1]) # note that type of starttime is string but we want datetime

## Create a new column 'start_datetime' in the dataframe from_date_day that contains datetimes from the starttime str values

# <your code goes here>
trip_and_dockcount_data['start_datetime'] = pd.to_datetime(trip_and_dockcount_data.starttime, infer_datetime_format=True)

## Display a line chart of trips by date
# Note: the line chart will be quite noisy 
# <your code goes here>

trip_and_dockcount_data.start_datetime.value_counts().sort_index() # Get the sort of the values working
trip_and_dockcount_data.start_datetime.value_counts().sort_index().plot(kind='line')  # plot the values

# <your code goes here>


## Bonus: create a line chart with the rides per month.  You can use the month number for the month rather than the month name
trip_and_dockcount_data['month_number'] = trip_and_dockcount_data.start_datetime.dt.month
trip_and_dockcount_data.month_number.value_counts().sort_index() # Get the sort of the values working

trip_and_dockcount_data.month_number.value_counts().sort_index().plot(kind='line') # plot it as a line plot

#plot with title and axis labels
trip_and_dockcount_data.month_number.value_counts().sort_index().plot(kind='line', title='Pronto rides by month number') # plot it as a line plot
plt.xlabel('Month number')
plt.ylabel('Number of rides')




### Grouping in plots 
# ## Grouped Box Plots: show one box plot for each group

# reminder: box plot of beer servings
drinks.beer.plot(kind='box', column='beer')


# box plot of beer servings grouped by continent
drinks.boxplot(column='beer', by='continent')


# box plot of all numeric columns grouped by continent
drinks.boxplot(by='continent')


# ## Grouped Histograms: show one histogram for each group

# reminder: histogram of beer servings
drinks.beer.plot(kind='hist')


# histogram of beer servings grouped by continent
drinks.hist(column='beer', by='continent')


# share the x axes
drinks.hist(column='beer', by='continent', sharex=True)


# share the x and y axes
drinks.hist(column='beer', by='continent', sharex=True, sharey=True)


# change the layout
drinks.hist(column='beer', by='continent', sharex=True, layout=(2, 3))


# ## Assorted Functionality

# saving a plot to a file
plt.rcParams['figure.figsize'] = (8, 6)
drinks.beer.plot(kind='hist', bins=20, title='Histogram of Beer Servings')
plt.xlabel('Beer Servings')
plt.ylabel('Frequency')
plt.savefig('beer_histogram.png', dpi=1000)


# list available plot styles
plt.style.available


# change to a different style
plt.style.use('ggplot')
plt.style.use('fivethirtyeight')

## Exercise 4 - Display a grouped box plot of the trip_and_dockcount_data ride durations by usertype

# Reminder, in Exercise 1 your line chart by day code was like this:
trip_and_dockcount_data.start_datetime.value_counts().sort_index().plot(kind='line') 

# also in exercise #3 you did something like this to change the text values of start_time to type datetime and assign it to a new column
trip_and_dockcount_data['start_datetime'] = pd.to_datetime(trip_and_dockcount_data.starttime, infer_datetime_format=True)

# Create a new column 'trip_duration' that is stoptime - startime in minutes

# <your code goes here>



# Create a group box plot of the the frequency of the trip_duration values by usertype

# <your code goes here>




# Bonus 1: Display a box plot of duration that compares the duration box plots for each month

# <your code goes here>



# Bonus 2: Write your box plot to a file

# <your code goes here>




# Bonus 3: Write your box plot to a file with image size 700x700
# Hint: Web search for plt.savefig and image size

# <your code goes here>





