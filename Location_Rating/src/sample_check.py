
import requests
def school_search(LATITUDE,LONGITUDE):
    API_KEY = "AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"



    # Define the API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{LATITUDE},{LONGITUDE}",
        "radius": "50000",
        # "type": "light_rail_station",
        "type": "train_station",
        # "type": "bus_station",
        # "type": "hindu_temple",
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
school_search("11.2593101","75.8659702")