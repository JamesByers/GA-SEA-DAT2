'''
CLASS: Getting Data from APIs

Exercise 1 - retrieving US Census language use data

'''
# Link to the Census Bureau language stats API description page
import requests
r = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625')

# Look through the API description links and examples to see what use you have avaialble

# Use the requests library to interact with a URL

import requests
# Use a URL example in a browser to see the result returned and the use request to access with python
# http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625
r = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625:650')

# modify the request to get languges 625 through 650 so we can see a larger sample of what is returned from the request
# Hint the syntax for more than one language number is similar to one we use for multiple elements in a list
r = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625:650')

# check the status: 200 means success, 4xx means error
r.status_code

# view the raw response text
r.text

# Convert to jason()
r.json()

# 
#look at the contents of the output of the jason() method.  It looks like it can easily become a list of lists

# Convert the jason() method output into a dataframe with the first list as the column header and the rest as rows of data
data= r.json()
import pandas as pd
data_cols=['LANLABEL', 'EST', 'NAME', 'state']
header = r.json()[0]
body = r.json()[1:]
data = pd.DataFrame(body, columns=header)

type(header)
# Sort the dataframe decending by the number of people speaking the language
# Check the data type of 'EST', the number of people that speak the language

data.sort('EST', ascending=False)
data.columns

type('EST')

# Now create a new request that brings in the stats for all the us and primary languages
# See the websites links for syntax for us and range of language nunbers



### Bonus
# Create a loop that will collect the counts of Spanish language speakers by state
