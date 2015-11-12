import json
import urllib2
import MySQLdb as RAIL
import time

def station(API_KEY):
	url = "http://api.erail.in/stations/?key="+API_KEY
	data = json.load(urllib2.urlopen(url))
	for i in range(len(data)):
		# print data[i]['code']+" -> "+data[i]['name']
		s = "'%s','%s'"%(data[i]['code'],data[i]['name'])
		with open("stations.txt", "a") as myfile:
			myfile.write(s)
			myfile.write("\n")
	print "Station table updated..."
	return data

if __name__ == '__main__':
	API_KEY = "fc8ab6ef-d7ed-4fec-8bb7-3abed6cc8b52"
	stations = station(API_KEY)
