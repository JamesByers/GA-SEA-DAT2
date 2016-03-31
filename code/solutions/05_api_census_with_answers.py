'''
CLASS: Getting Data from APIs

Exercise 1 - retrieving US Census language use data
You will use the API described here: https://www.census.gov/data/developers/data-sets/language-stats.html

'''
# Link to the Census Bureau language stats API description page

# Look through the API description links and examples to see what use you have avaialble

# Use the requests library to interact with a URL

import requests
# Use a URL example in a browser to see the result returned and the use request to access with python
# http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625
r = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625')
r.text
r.json()
# modify the request to get languges 625 through 650 so we can see a larger sample of what is returned from the request
# Hint the syntax for more than one language number is similar to one we use for multiple elements in a list
r = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625:650')
r.text
r.json()
# check the status: 200 means success, 4xx means error
r.status_code

# view the raw response text
r.text

# Convert to jason()
r.json()

# Does not make sense to decode into a dictionary as we did before becasue this is a list of lists
# Convert this data into a dataframe with the first list as the column header
import pandas as pd
header = r.json()[0]
body = r.json()[1:]
data = pd.DataFrame(body, columns=header)

# Sort the dataframe decending by the number of people speaking the language
data.sort('EST', ascending=False) # sorts the text values of 'EST' since values are strings.  We must change thise to a number to sort what we want
data.dtypes
data['EST'] = data['EST'].convert_objects(convert_numeric=True)
data.sort('EST', ascending=False) # sorts the numeric values of 'EST' descending

# Now create a new request that brings in the stats for all the us and primary languages
# See the websites links for syntax for us and range of language nunbers
r2 = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=us:01&LAN=625:999')
r2.status_code
header = r2.json()[0]
body = r2.json()[1:]
data2 = pd.DataFrame(body, columns=header)
print(data2)


### Bonus
# Create a loop that will collect the counts of Spanish language speakers by state

url_part1 = "http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:"
url_part3 = "&LAN=625"
for count in range(1, 52):
    if count == 1:
        r = requests.get(url_part1 + str(count) + url_part3)      
        header = r.json()[0]
        body = r.json()[1:]
        data = pd.DataFrame(body, columns=header)
    else:
        if count not in [3, 7, 14, 43, 52 ]:
            r = requests.get(url_part1 + str(count) + url_part3)      
            header = r.json()[0]
            body = r.json()[1:]
            data_temp = pd.DataFrame(body, columns=header)
            data_temp.tail(10)
            data = data.append(data_temp)
            data.tail(47)
            data.shape
print (data)
 
           