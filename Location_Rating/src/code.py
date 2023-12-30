from flask import *
from selenium import webdriver
import joblib
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

import requests
import json
import numpy as np
from math import radians, cos, sin, asin

api_key = "ae6e39fce2165444d8cb435b3d14adc6"
def weather(lat,lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    #print(response.text)

    # Convert the response data to a Python dictionary
    data = response.json()

    # Extract the relevant weather data
    description = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius

    # #print the weather information
    #print(f"The current weather is {description}, with a temperature of {temperature:.2f}°C.")
    return (f"The current weather is {description}, with a temperature of {temperature:.2f}°C.")

def aqi(lat,lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}"
    # url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    #print(response.text)

    # Convert the response data to a Python dictionary
    data = response.json()

    # Extract the relevant weather data
    description = data['list'][0]['main']['aqi']
    #print(description)
    # temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
    #
    # # #print the weather information
    #print(f"The current Air Quality Index is {description}.")
    return (f"The current Air Quality Index is {description}.")


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

def calculatePlusCode(Latitude,Longitude):


    # location = geolocator.geocode(str(Latitude) + "," + str(Longitude))


    url = "https://plus.codes/api?address="+str(Latitude)+","+str(Longitude)+"&email=razisaraz123@gmail.com"

    res=requests.get(url)
    res=json.loads(res.text)

    #print("=============================================")
    #print("plus_code",res['plus_code']['global_code'])
    return res['plus_code']['global_code']

def location(Latitude,Longitude):
    # Import module
    from geopy.geocoders import Nominatim

    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Assign Latitude & Longitude
    # Latitude = "25.594095"
    # Longitude = "85.137566"

    # Displaying Latitude and Longitude
    #print("Latitude: ", Latitude)
    #print("Longitude: ", Longitude)

    # Get location with geocode
    location = geolocator.geocode(Latitude+","+Longitude)

    # Display location

    #print(location)
    return location



def location_from_place(place):
    try:
        from geopy.geocoders import Nominatim

        gl=Nominatim(user_agent="MyApp")
        lo=gl.geocode(place)
        #print(lo)
        #print(lo.latitude)
        #print(lo.longitude)
        return [str(lo.latitude),str(lo.longitude)]
    except Exception as e:
        # print(e)
        try:
            from geopy.geocoders import Nominatim

            gl = Nominatim(user_agent="MyApp")
            lo = gl.geocode(place.split(' ')[0])
            # print(lo)
            # print(lo.latitude)
            # print(lo.longitude)
            return [str(lo.latitude), str(lo.longitude)]
        except:
            return ["na", "na"]



def hospital_info(LATITUDE,LONGITUDE):
    API_KEY = "AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"



    # Define the API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{LATITUDE},{LONGITUDE}",
        "radius": "5000",
        "type": "hospital",
        "key": API_KEY,

    }

    # Send the API request and parse the JSON response
    response = requests.get(url, params=params).json()
    print(response)
    # Extract the name and location of each river from the response
    results = response["results"]
    hlrivers = []
    for result in results:
        name = result["name"]
        location = result["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        hlrivers.append((name, latitude, longitude))
        if (len(hlrivers) > 4):
            break
    return hlrivers
def school_search(LATITUDE,LONGITUDE):
    API_KEY = "AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"



    # Define the API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{LATITUDE},{LONGITUDE}",
        "radius": "5000",
        "type": "school",
        "key": API_KEY,

    }

    # Send the API request and parse the JSON response
    response = requests.get(url, params=params).json()
    print(response)
    # Extract the name and location of each river from the response
    results = response["results"]
    rivers = []
    for result in results:
        name = result["name"]
        location = result["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        rivers.append((name, latitude, longitude))
        if(len(rivers)>4):
            break
    return rivers


def search_police_station(LATITUDE,LONGITUDE):

    API_KEY = "AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"

    # Define the API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{LATITUDE},{LONGITUDE}",
        "radius": "5000",
        "type": "police",
        "key": API_KEY,

    }

    # Send the API request and parse the JSON response
    response = requests.get(url, params=params).json()
    print(response)
    # Extract the name and location of each river from the response
    results = response["results"]
    rivers = []
    for result in results:
        name = result["name"]
        location = result["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        rivers.append((name, latitude, longitude))
        print((name, latitude, longitude))
        if (len(rivers) > 4):
            break
    return rivers
def search_railway_station(LATITUDE,LONGITUDE):
    API_KEY = "AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"



    # Define the API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{LATITUDE},{LONGITUDE}",
        "radius": "50000",

        "type": "train_station",
        "key": API_KEY,

    }

    # Send the API request and parse the JSON response
    response = requests.get(url, params=params).json()
    print(response)
    # Extract the name and location of each river from the response
    results = response["results"]
    rivers = []
    for result in results:
        name = result["name"]
        location = result["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        rivers.append((name, latitude, longitude))
        print((name, latitude, longitude))
        if(len(rivers)>3):
            break
    return rivers
#
# def search_railway_station(q):
#     result = []
#     query = "railway station near " + q
#     from selenium import webdriver
#     driver = webdriver.Chrome()  # You can replace this with other web drivers
#     driver.get("https://google.com/search?q=%s" % query)
#     source = driver.page_source  # Here is your populated data.
#     # #print(source)
#     res = source.split('<div class="rqTuzc vdA38d fnSb3d"')
#
#     #print("11111111111111111111111")
#     # res=source.split('<span class="OSrXXb">')
#     for i in range(1, len(res)):
#         result.append(res[i].split('<span class="aVSTQd tNxQIb OSrXXb">')[1].split("</span>")[0])
#         #print(res[i].split('<span class="aVSTQd tNxQIb OSrXXb">')[1].split("</span>")[0])
#         #print(res[i].split('<span class="aVSTQd tNxQIb OSrXXb">')[1].split("</span>")[1]).split('<div>')[1]
#         # #print(res[i].split('class="OSrXXb">')[1].split("Tourist attraction</div><div>")[1].split("</div>")[0])
#     #print("22222222222222222222222222222222")
#     if len(result) == 0:
#         res = source.split('<span class="OSrXXb">')
#         for i in range(1, len(res)):
#             #print(res[i].split('</span>')[0])
#
#             h = res[i].split('</span>')[0]
#
#             result.append(h)
#     #print("333333333333333333333333333333")
#     if len(result) == 0:
#         res = source.split('<div class="r2fjmd VCOFK WyGS9c">')
#         for i in range(1, len(res)):
#             #print(res[i].split('">')[1].split("</div>")[0])
#             result.append(res[i].split('">')[1].split("</div>")[0])
#     #print(result)
#     driver.quit()
#     return result


def search_nearest_river(query):
    result=[]
    from selenium import webdriver
    # driver = webdriver.Chrome()  # You can replace this with other web drivers
    # driver.get("https://google.com/search?q=%s" % query)
    # source = driver.page_source  # Here is your populated data.
    source=requests.get("https://google.com/search?q=%s" % query).text

    res = source.split('<span class="OSrXXb">')
    for i in range(1, len(res)):
        #print(res[i].split('</span>')[0])
        result.append(res[i].split('</span>')[0])
    # driver.quit()  # don't forget to quit the driver!
    return result

def church_search(LATITUDE,LONGITUDE):
    API_KEY = "AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"



    # Define the API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{LATITUDE},{LONGITUDE}",
        "radius": "50000",
        # "type": "cafe",
        # "type": "train_station",
        # "type": "bus_station",
        # "type": "hindu_temple",
        # "type": "tourist_attraction",
        # "type": "mosque",
        "type": "church",
        "key": API_KEY,

    }

    # Send the API request and parse the JSON response
    response = requests.get(url, params=params).json()
    print(response)
    # Extract the name and location of each river from the response
    results = response["results"]
    rivers = []
    for result in results:
        name = result["name"]
        location = result["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        rivers.append((name, latitude, longitude))
        print((name, latitude, longitude))
        if(len(rivers)>3):
            break
    return rivers

def hindu_temple_search(LATITUDE,LONGITUDE):
    API_KEY = "AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"



    # Define the API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{LATITUDE},{LONGITUDE}",
        "radius": "50000",
        # "type": "cafe",
        # "type": "train_station",
        # "type": "bus_station",
        "type": "hindu_temple",
        # "type": "tourist_attraction",
        # "type": "mosque",
        # "type": "church",
        "key": API_KEY,

    }

    # Send the API request and parse the JSON response
    response = requests.get(url, params=params).json()
    print(response)
    # Extract the name and location of each river from the response
    results = response["results"]
    rivers = []
    for result in results:
        name = result["name"]
        location = result["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        rivers.append((name, latitude, longitude))
        print((name, latitude, longitude))
        if(len(rivers)>3):
            break
    return rivers

def mosque_search(LATITUDE,LONGITUDE):
    API_KEY = "AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"



    # Define the API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{LATITUDE},{LONGITUDE}",
        "radius": "50000",
        # "type": "cafe",
        # "type": "train_station",
        # "type": "bus_station",
        # "type": "hindu_temple",
        # "type": "tourist_attraction",
        "type": "mosque",
        # "type": "church",
        "key": API_KEY,

    }

    # Send the API request and parse the JSON response
    response = requests.get(url, params=params).json()
    print(response)
    # Extract the name and location of each river from the response
    results = response["results"]
    rivers = []
    for result in results:
        name = result["name"]
        location = result["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        rivers.append((name, latitude, longitude))
        print((name, latitude, longitude))
        if(len(rivers)>3):
            break
    return rivers


def tourist_place_search(lati,lon):
    API_KEY = "AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"

    # Define the API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lati},{lon}",
        "radius": "50000",
        # "type": "cafe",
        # "type": "train_station",
        # "type": "bus_station",
        # "type": "hindu_temple",
        "type": "tourist_attraction",
        # "type": "mosque",
        # "type": "church",
        "key": API_KEY,

    }

    # Send the API request and parse the JSON response
    response = requests.get(url, params=params).json()
    print(response)
    # Extract the name and location of each river from the response
    results = response["results"]
    rivers = []
    for result in results:
        name = result["name"]
        location = result["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        rivers.append((name, latitude, longitude))
        print((name, latitude, longitude))
        if (len(rivers) > 3):
            break
    return rivers



def search_Restaurant(LATITUDE,LONGITUDE):
    API_KEY = "AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"



    # Define the API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{LATITUDE},{LONGITUDE}",
        "radius": "5000",
        "type": "restaurant",
        "key": API_KEY,

    }

    # Send the API request and parse the JSON response
    response = requests.get(url, params=params).json()
    print(response)
    # Extract the name and location of each river from the response
    results = response["results"]
    rivers = []
    for result in results:
        name = result["name"]
        location = result["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        rivers.append((name, latitude, longitude))

        if len(rivers)>4:
            break
    return rivers

app=Flask(__name__)
@app.route("/")
def main():

    return render_template("map11.html")

@app.route("/fp",methods=['post'])
def fp():
    prediction_row=[]
    flati=request.form['lat']
    flon=request.form['lon']

    PluseCode=calculatePlusCode(flati,flon)
    details=str(location(flati,flon))

    dd=details.split(",")
    place_text=dd[0]

    for i in dd:
        if 'district' in i:
            place_text=place_text+" "+i.split(' ')[1]
            break
    else:
        place_text+=" "+dd[1]
    #print(place_text,"++++++++++++++++++")
    pluscode1 = PluseCode.replace('+', '%2B')
    # qry="https://www.google.com/search?q=police+station+near+"+pluscode1
    hoslist =hospital_info(flati,flon)
    hlresult = []
    minhdist=-1
    for i in hoslist:

        lati,longi=i[1],i[2]
        dis = calculate_spherical_distance(lati, longi, flati, flon)
        pc=calculatePlusCode(lati,longi)
        row=[i[0],pc,dis]
        if float(dis) < 50:
            if minhdist==-1:
                minhdist=dis
            else:
                if dis<minhdist:
                    minhdist=dis

        hlresult.append(row)
    prediction_row.append(minhdist)


    school=school_search(flati,flon)
    schoolresult = []
    minhdist=-1
    for i in school:

        lati,longi=i[1],i[2]


        dis = calculate_spherical_distance(lati, longi, flati, flon)
        pc=calculatePlusCode(lati,longi)

        row=[i[0],pc,dis]
        if float(dis) < 50:
            schoolresult.append(row)
            if minhdist == -1:
                minhdist = dis
            else:
                if dis < minhdist:
                    minhdist = dis

            # result.append(row)
    prediction_row.append(minhdist)



    qry =  pluscode1
    police_list = search_police_station(flati,flon)
    policeresult = []
    minhdist=-1
    for i in police_list:
        #print("=================")
        #print("=================")
        #print(i)
        #print("=================")
        #print("=================")
        lati, longi = i[1],i[2]

        dis = calculate_spherical_distance(lati, longi, flati, flon)
        pc = calculatePlusCode(lati, longi)
        row = [i[0], pc,dis]
        if float(dis) < 50:
            policeresult.append(row)
            if minhdist == -1:
                minhdist = dis
            else:
                if dis < minhdist:
                    minhdist = dis

            # result.append(row)
    prediction_row.append(minhdist)




    qry = "https://www.google.com/search?q=railway+station+near+" + pluscode1
    railway_list = search_railway_station(flati,flon)
    #print("+++++++++++++++++++++++++============")
    #print(railway_list)
    railwayresult = []
    minhdist=-1
    for i in railway_list:

        lati, longi = i[1], i[2]
        if lati != "na":
            try:
                dis = calculate_spherical_distance(lati, longi, flati, flon)
                pc = calculatePlusCode(lati, longi)
                row = [i[0], pc,dis]
                if float(dis) < 50:
                    railwayresult.append(row)
                    if minhdist == -1:
                        minhdist = dis
                    else:
                        if dis < minhdist:
                            minhdist = dis

                    # result.append(row)

                #print(row)
            except Exception as e:
                pass
        else:

            row = [i, "No data","na"]
            railwayresult.append(row)
            #print(row)
    prediction_row.append(minhdist)
    qry = "river near " + place_text

    Rivers = search_nearest_river(qry)
    Rivers1 = []
    minhdist=-1
    for i in Rivers:
        #print("=================")
        #print("=================")
        #print(i)
        #print("=================")
        #print("=================")
        lati, longi = location_from_place(i)
        if lati != "na":
            try:
                dis = calculate_spherical_distance(lati, longi, flati, flon)
                pc = calculatePlusCode(lati, longi)
                row = [i, pc, dis]
                if float(dis) < 50:
                    Rivers1.append(row)
                    if minhdist == -1:
                        minhdist = dis
                    else:
                        if dis < minhdist:
                            minhdist = dis

                    # result.append(row)

                #print(row)
            except Exception as e:
                pass
        else:

            row = [i, "No data", "na"]
            Rivers1.append(row)
            #print(row)
    prediction_row.append(minhdist)

    qry = "tourist places near " + place_text
    print(qry,"=========================")
    Tourist_Place = tourist_place_search(flati,flon)
    Tourist_Places = []
    minhdist=-1
    for i in Tourist_Place:
        #print("=================")
        #print("=================")
        #print(i)
        #print("=================")
        #print("=================")
        lati, longi = i[1],i[2]
        if lati != "na":
            try:
                dis = calculate_spherical_distance(lati, longi, flati, flon)
                pc = calculatePlusCode(lati, longi)
                row = [i[0], pc, dis]
                if float(dis)<50:
                    Tourist_Places.append(row)
                    if minhdist == -1:
                        minhdist = dis
                    else:
                        if dis < minhdist:
                            minhdist = dis

                    # result.append(row)

                #print(row)
            except Exception as e:
                pass
        else:
            pass
            # row = [i, "No data", "na"]
            # Tourist_Places.append(row)
            #print(row)
    prediction_row.append(minhdist)
    qry = "https://www.google.com/search?q=Restaurant+near+" + pluscode1
    Restaurant = search_Restaurant(flati,flon)
    Restaurants = []
    minhdist=-1
    for i in Restaurant:

        lati, longi=i[1],i[2]

        dis = calculate_spherical_distance(lati, longi, flati, flon)
        pc = calculatePlusCode(lati, longi)
        row = [i[0], pc, dis]
        if float(dis) < 50:
            Restaurants.append(row)
            if minhdist == -1:
                minhdist = dis
            else:
                if dis < minhdist:
                    minhdist = dis

            # result.append(row)
    prediction_row.append(minhdist)

    church = church_search(flati,flon)
    church_list = []
    minhdist=-1
    for i in church:

        lati, longi=i[1],i[2]

        dis = calculate_spherical_distance(lati, longi, flati, flon)
        pc = calculatePlusCode(lati, longi)
        row = [i[0], pc, dis]
        if float(dis) < 50:
            church_list.append(row)
            if minhdist == -1:
                minhdist = dis
            else:
                if dis < minhdist:
                    minhdist = dis

            # result.append(row)
    prediction_row.append(minhdist)

    hindu_temple = hindu_temple_search(flati,flon)
    hindu_temple_list = []
    minhdist=-1
    for i in hindu_temple:

        lati, longi=i[1],i[2]

        dis = calculate_spherical_distance(lati, longi, flati, flon)
        pc = calculatePlusCode(lati, longi)
        row = [i[0], pc, dis]
        if float(dis) < 50:
            hindu_temple_list.append(row)
            if minhdist == -1:
                minhdist = dis
            else:
                if dis < minhdist:
                    minhdist = dis

            # result.append(row)
    prediction_row.append(minhdist)

    mosque = mosque_search(flati,flon)
    mosque_list = []
    minhdist=-1
    for i in mosque:

        lati, longi=i[1],i[2]

        dis = calculate_spherical_distance(lati, longi, flati, flon)
        pc = calculatePlusCode(lati, longi)
        row = [i[0], pc, dis]
        dis=float(dis)

        if float(dis) < 50:
            mosque_list.append(row)
            if minhdist == -1:
                minhdist = float(dis)
            else:
                if dis < minhdist:
                    minhdist = dis

            # result.append(row)
    prediction_row.append(minhdist)

    w=weather(flati,flon)
    aq=aqi(flati,flon)


    print("============")
    print("============")
    print("============")
    print(prediction_row)
    print("************************")
    print("************************")
    print("************************")
    print("************************")
    rf_from_joblib = joblib.load('rf.pkl')

    # Use the loaded model to make predictions
    yp = rf_from_joblib.predict([prediction_row])
    rating=yp[0]
    return render_template("result.html",ml=mosque_list,hl=hindu_temple_list,cl=church_list,gp=PluseCode,d=details,r=hlresult,sr=schoolresult,pr=policeresult,rl=railwayresult,tps=Tourist_Places,Restaurants=Restaurants,River=Rivers1,w=w,a=aq,rating=rating)

app.run()

