import csv
import json

trips = {}
stations = {}
total = 0

def getDelay(start_date):
    time = start_date.split(" ")[1]
    hour = time.split(":")[0]
    minute = time.split(":")[1]
    now = int(hour) * 60 + int(minute)
    if now <= 360:
    	delay = now + 1440 - 360
    else:
    	delay = now - 360
    return delay


with open('data/station.csv', 'r') as stationfile:
	reader = csv.DictReader(stationfile)
	for row in reader:
		stations[row['name']] = row['city']


with open('data/trip.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		start_date = row['start_date'].split(' ')[0]
		start_station = row['start_station_name']
		end_station = row['end_station_name']
		if start_station == 'Washington at Kearney':
			start_station = 'Washington at Kearny'
		if start_station == 'Post at Kearney':
			start_station = 'Post at Kearny'
		if end_station == 'Washington at Kearney':
			end_station = 'Washington at Kearny'
		if end_station == 'Post at Kearney':
			end_station = 'Post at Kearny'
		if start_station in stations and stations[start_station] == 'San Francisco':
			if not start_date in trips:
				trips[start_date] = []
			trips[start_date].append([start_station, end_station, int(row['duration']) / 60, getDelay(row['start_date'])])
			total += 1

print(total)


with open('data/trips.json', 'w') as jsonfile:
	json.dump(trips, jsonfile)

