from __future__ import print_function

import sys
import os
import json
import pandas as pd
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

#Checking is the arguments are the correct number
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python bustime.py <KEY> <BUSLINE> <FILENAME>")
    sys.exit()

#getting the variables from the command line
thekey=sys.argv[1]
bus=sys.argv[2]
bus=bus.upper()
fout=sys.argv[3]



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


#Creating dictionaries and appending to a df
df = pd.DataFrame()

for it in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    Busname=(it["MonitoredVehicleJourney"]["VehicleRef"])
    Latitude=(it["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"])
    Longitude=(it["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"])
    StopName=(it["MonitoredVehicleJourney"]["MonitoredCall"]["StopPointName"])
    StopStatus=(it["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"])
    bus_things = [{'Busname': Busname, "Latitude": Latitude, "Longitude": Longitude, 'StopName': StopName, 'StopStatus': StopStatus}]
    df=df.append(bus_things)

df.StopName = df.StopName.replace("","N/A")
df.to_csv(fout+".csv", index=False)
print ("Your file has been saved to "+fout+".csv")
