For more information, visit http://prontocycleshare.com/data or email questions to data@prontocycleshare.com. 

FILE LIST
1) 2015_status_data.csv - records of bike and dock availability
2) 2015_station_data.csv - station latitude, longitude, name, dockcount, online date
3) 2015_trip_data.csv - records of individual trips
4) 2015_weather_data.csv - daily weather by city

Files contain data from 10/13/14 (system launch) to 10/12/15.

1) STATUS DATA
FILE = "2015_status_data.csv"
-station_id: station ID number (use "2015_station_data.csv" to find corresponding station information)
-bikes_available: number of available bikes
-docks_available: number of available docks
-bikes_blocked: number of unavailable bikes
-docks_blocked: number of unavailable docks
-time: date and time, in PST

2) STATION INFORMATION
FILE = "2015_station_data.csv"
-station_id: station ID number (corresponds to "station_id" in "2015_status_data.csv")
-name: name of station
-lat: station latitude
-long: station longitude
-dockcount: number of total docks at each station as of 10/12/2015
-online: date that station was active

3) TRIP DATA
FILE = "2015_trip_data.csv"
-trip_id: numeric ID of bike triptrip taken
-starttime: day and time trip started, in PST
-stoptime: day and time trip ended, in PST
-bikeid: ID attached to each bike
-tripduration: time of trip in seconds 
-from_station_name: name of station where trip originated
-to_station_name: name of station where trip terminated 
-from_station_id: ID of station where trip originated
-to_station_id: ID of station where trip terminated
-usertype: "Short-Term Pass Holder" is a rider who purchased a 24-Hour or 3-Day Pass; "Annual Member" is a rider who purchased an Annual Membership
-gender: gender of rider 
-birthyear: birth year of rider

Notes:

* First row contains column names
* Trips that did not include a start or end date were removed from original table
* Trips of duration less than one minute or greater than eight hours were removed from original table
* Gender and birth year are only available for Annual Members
* Some stations have been renamed or moved within two blocks of their original location, all stations use current names

4) WEATHER DATA
FILE = "2015_weather_data.csv"
Daily weather information in service area