# convert.py - file io application to read in latest covid19 data and spit out Leaflet.js circles using string concatenation
# March 24, 2020: mhoel - original coding 

# Access data from: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
# Korea, South - Bahamas, The - Gambia, The : Must be manually fixed in the data (South Korea, Bahamas, Gambia) 

# Read file in
fi = open("05-20-2020.csv","r")
fi.readline() # skip over first title line
datarows = fi.readlines()
fi.close()

# Write file out
fo = open("leafrecover.txt","w")

count = 0 # count number of circles

# loop through all rows in the csv file
for line in datarows:
        templist = line.split(",")
        prov = templist[2]
        country = templist[3]
        confirmed = templist[7]
        deaths = templist[8]
        recover = templist[9]
        lat = templist[5]
        lon = templist[6]

       
        # make radius of circle bigger for cartographic appeal
        if (recover != ""):                
                recoverradius = int(recover) * 2

                if (int(recover) > 0):
                        if (prov != ""):
                                marker = "L.circle([" + lat + "," + lon + "],{color:'#c985ac',fillColor:'#c985ac',fillOpacity:0.5,radius:" + str(recoverradius) + "}).addTo(layergroup).bindPopup('" + prov.replace("'", "") + "," + country.replace("'","") + " : " + recover + "')"	
                        else:
                                marker = "L.circle([" + lat + "," + lon + "],{color:'#c985ac',fillColor:'#c985ac',fillOpacity:0.5,radius:" + str(recoverradius) + "}).addTo(layergroup).bindPopup('" + country.replace("'", "") + " : " + recover + "')"

                        fo.write(marker + "\n")
                        count = count + 1
		

print(str(count) + " markers written out")
fo.close()
