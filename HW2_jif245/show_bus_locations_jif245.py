from __future__ import print_function

import sys
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

#Checking is the arguments are the correct number
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python  bustime.py <KEY> <BUSLINE>")
    sys.exit()

#getting the variables from the command line
thekey=sys.argv[1]
bus=sys.argv[2]

#feedback to the user
print ("The selected busline is",sys.argv[2])
print ()

#Getting URL
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+ thekey + "&VehicleMonitoringDetailLevel=calls&LineRef="+ bus

#loading data
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


#creating a variable with the vehicle activity
a=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

#feedback to the user
print("There are",(len(a)),"buses, and their names and locations are:")
print()

#printing the bus information
for it in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    print( "Bus Name:",(it["MonitoredVehicleJourney"]["VehicleRef"]))
    print ("Latitude:",(it["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]))
    print ("Longitude:",(it["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]))
    print()
    

