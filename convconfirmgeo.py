# convert.py - file io application to read in latest covid19 data and spit out Leaflet.js circles using string concatenation
# March 24, 2020: mhoel - original coding 
# added geojson - https://github.com/datasets/geo-countries/tree/master/data

# Access data from: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
# Korea, South - Bahamas, The - Gambia, The : Must be manually fixed in the data (South Korea, Bahamas, Gambia) 

# Read file in
fi = open("05-20-2020.csv","r")
fi.readline() # skip over first title line
datarows = fi.readlines()
fi.close()

# loop through all rows in the csv file
provs2 = []
numconfirmed = []
for line in datarows:
    templist = line.split(",")
    prov = templist[2].lower()
    country = templist[3].lower()
    confirmed = templist[7]
    deaths = templist[8]
    recover = templist[9]
    lat = templist[5]
    lon = templist[6]

    if (country == "canada"):
        provs2.append(prov)
        numconfirmed.append(confirmed)

print(provs2)
print(confirmed)

import json

with open('canada_provinces.geojson') as f:
  data = json.load(f)

f.close()

for prov in data["features"]:
    name = prov["properties"]["name"].lower()
    try:
        i = provs2.index(name)
        prov["properties"]["confirmed"] = numconfirmed[i]
        print(prov["properties"])
    except:
        print(name + " not found")
        prov["properties"]["confirmed"] =0

with open('cloroplethconfirm.geojson', 'w') as json_file:
  json.dump(data, json_file)

json_file.close()
