from selenium import webdriver

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

import requests
import json
import numpy as np
from math import radians, cos, sin, asin

flati=11.3605986
flon=75.9120519


def calculatePlusCode(Latitude,Longitude):


    # location = geolocator.geocode(str(Latitude) + "," + str(Longitude))


    url = "https://plus.codes/api?address="+str(Latitude)+","+str(Longitude)+"&email=razisaraz123@gmail.com"

    res=requests.get(url)
    res=json.loads(res.text)

    #print("=============================================")
    #print("plus_code",res['plus_code']['global_code'])
    return res['plus_code']['global_code']

def tourist_place_search(query):
    result=[]
    driver = webdriver.Chrome() # You can replace this with other web drivers
    #print("https://google.com/search?q=%s" % query)
    #print("https://google.com/search?q=%s" % query)
    #print("https://google.com/search?q=%s" % query)
    #print("https://google.com/search?q=%s" % query)
    driver.get("https://google.com/search?q=%s" % query)
    source = driver.page_source # Here is your populated data.
    # #print(source)
    res=source.split('<div class="rqTuzc vdA38d fnSb3d"')


    # res=source.split('<span class="OSrXXb">')
    for i in range (1,len(res)):
        result.append(res[i].split('<span class="aVSTQd tNxQIb OSrXXb">')[1].split("</span>")[0])
        #print(res[i].split('<span class="aVSTQd tNxQIb OSrXXb">')[1].split("</span>")[0])
        # #print(res[i].split('class="OSrXXb">')[1].split("Tourist attraction</div><div>")[1].split("</div>")[0])

    if len(result)==0:
        res=source.split('<span class="OSrXXb">')
        for i in range(1,len(res)):
            #print(res[i].split('</span>')[0])
            result.append(res[i].split('</span>')[0])

    if len(result) == 0:
        res = source.split('<div class="r2fjmd VCOFK WyGS9c">')
        for i in range(1, len(res)):
            #print(res[i].split('">')[1].split("</div>")[0])
            result.append(res[i].split('">')[1].split("</div>")[0])
    # driver.quit() # don't forget to quit the driver!
    return result



def location_from_place(place):
    try:
        from geopy.geocoders import Nominatim

        gl=Nominatim(user_agent="MyApp")
        lo=gl.geocode(place.split(' ')[0])
        #print(lo)
        #print(lo.latitude)
        #print(lo.longitude)
        return [str(lo.latitude),str(lo.longitude)]
    except Exception as e:
        #print(e)
        try:
            from geopy.geocoders import Nominatim

            gl = Nominatim(user_agent="MyApp")
            lo = gl.geocode(place.split(' ')[0])
            # print(lo)
            # print(lo.latitude)
            # print(lo.longitude)
            return [str(lo.latitude), str(lo.longitude)]
        except:
            return ["na","na"]



def calculate_spherical_distance(lat1, lon1, lat2, lon2, r=6371):
    # Convert degrees to radians
    coordinates = float(lat1), float(lon1), float(lat2), float(lon2)
    # radians(c) is same as c*pi/180
    phi1, lambda1, phi2, lambda2 = [
        radians(c) for c in coordinates
    ]

    # Apply the haversine formula
    a = (np.square(sin((phi2 - phi1) / 2)) + cos(phi1) * cos(phi2) *
         np.square(sin((lambda2 - lambda1) / 2)))
    d = 2 * r * asin(np.sqrt(a))
    return d


qry = "tourist places near Kattangal-Koduvally Road Kozhikode"
print(qry,"=========================")
Tourist_Place = tourist_place_search(qry)
Tourist_Places = []
for i in Tourist_Place:
    #print("=================")
    #print("=================")
    print(i)
    #print("=================")
    #print("=================")
    lati, longi = location_from_place(i)
    if lati != "na":
        try:
            dis = calculate_spherical_distance(lati, longi, flati, flon)
            pc = calculatePlusCode(lati, longi)
            row = [i, pc, dis]
            if float(dis)<50:
                Tourist_Places.append(row)
            #print(row)
        except Exception as e:
            pass
    else:

        row = [i, "No data", "na"]
        Tourist_Places.append(row)
        #print(row)
print(Tourist_Places)