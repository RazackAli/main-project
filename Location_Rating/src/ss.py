# # import requests
# #
# # res=requests.get("https://www.google.com/search?q=river%20near%20civil%20station%20kozhikode")
# #
# # print(res.text)
# #
# # try:
# # 	from googlesearch import search
# # except ImportError:
# # 	print("No module named 'google' found")
# #
# # # to search
# # query = "river near civil station kozhikode"
# #
# # for j in search(query, tld="co.in", num=10, stop=10, pause=2):
# # 	print(j)
#
#
# # # Enter your Google Maps API key here
# # API_KEY = "AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"
# #
# # # Enter the latitude and longitude of the location you want to search from
# # LATITUDE = "11.8063479"
# # LONGITUDE = "75.9515076"
# #
# # # Define the API endpoint and parameters
# # url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
# # params = {
# #     "location": f"{LATITUDE},{LONGITUDE}",
# #     "radius": "5000",
# #     "type": "river",
# #     "key": API_KEY,
# # }
# #
# # # Send the API request and parse the JSON response
# # response = requests.get(url, params=params).json()
# #
# # # Extract the name and location of each river from the response
# # results = response["results"]
# # rivers = []
# # for result in results:
# #     name = result["name"]
# #     location = result["geometry"]["location"]
# #     latitude = location["lat"]
# #     longitude = location["lng"]
# #     rivers.append((name, latitude, longitude))
# #
# # print("Print the list of rivers")
# # for river in rivers:
# #     print(f"{river[0]} ({river[1]}, {river[2]})")
# # #
# # # import requests
# # #
# # # url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants%20in%20vivil station kozhikode=AIzaSyB3y0szjZmNj_w2q9Vnc08ZL_FU6Z4VTFE"
# # #
# # # payload={}
# # # headers = {}
# # #
# # # response = requests.request("GET", url, headers=headers, data=payload)
# # #
# # # print(response.text)
#
#
#
#
# # from googlesearch import *
# # import webbrowser
# # #to search, will ask search query at the time of execution
# # query = input("Input your query:")
# # #iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
# # chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# # for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
# #    res= webbrowser.get("https://google.com/search?q=%s" % query)
# #    print(res)
#
# def search_Restaurant(q):
#     result=[]
#     query="Restaurant near "+q
#     from selenium import webdriver
#     driver = webdriver.Chrome() # You can replace this with other web drivers
#     driver.get("https://google.com/search?q=%s" % query)
#     source = driver.page_source # Here is your populated data.
#     # print(source)
#     res=source.split('<div class="rqTuzc vdA38d fnSb3d"')
#
#     print("11111111111111111111111")
#     # res=source.split('<span class="OSrXXb">')
#     for i in range (1,len(res)):
#         result.append(res[i].split('<span class="aVSTQd tNxQIb OSrXXb">')[1].split("</span>")[0])
#         print(res[i].split('<span class="aVSTQd tNxQIb OSrXXb">')[1].split("</span>")[0])
#         print(res[i].split('<span class="aVSTQd tNxQIb OSrXXb">')[1].split("</span>")[1]).split('<div>')[1]
#         # print(res[i].split('class="OSrXXb">')[1].split("Tourist attraction</div><div>")[1].split("</div>")[0])
#     print("22222222222222222222222222222222")
#     if len(result)==0:
#         res=source.split('<span class="OSrXXb">')
#         for i in range(1,len(res)):
#
#             print(res[i].split('</span>')[0])
#
#             h=res[i].split('</span>')[0]
#
#             result.append(h)
#     print("333333333333333333333333333333")
#     if len(result)==0:
#         res=source.split('<div class="r2fjmd VCOFK WyGS9c">')
#         for i in range(1,len(res)):
#             print(res[i].split('">')[1].split("</div>")[0])
#             result.append(res[i].split('">')[1].split("</div>")[0])
#     print(result)
#
#     return result
# # search_police_station("Thottakkara  Perinthalmanna")
# search_police_station("7J2RX68C%2BJ4")
# # driver.quit() # don't forget to quit the driver!
#
# # query="river near civil station kozhikode"
# # from selenium import webdriver
# # driver = webdriver.Chrome() # You can replace this with other web drivers
# # driver.get("https://google.com/search?q=%s" % query)
# # source = driver.page_source # Here is your populated data.
# #
# # res=source.split('<span class="OSrXXb">')
# # for i in range (1,len(res)):
# #     print(res[i].split('</span>')[0])
# #     result.append(res[i].split('</span>')[0])
# # driver.quit() # don't forget to quit the driver!


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
        #print(e)
        return ["na","na"]



def school_search(q):
    result=[]
    query="schools near "+q
    from selenium import webdriver
    driver = webdriver.Chrome() # You can replace this with other web drivers
    driver.get("https://google.com/search?q=%s" % query)
    source = driver.page_source # Here is your populated data.
    # print(source)
    res=source.split('<div class="rqTuzc vdA38d fnSb3d"')

    print("11111111111111111111111")
    # res=source.split('<span class="OSrXXb">')
    for i in range (1,len(res)):
        result.append(res[i].split('<span class="aVSTQd tNxQIb OSrXXb">')[1].split("</span>")[0])
        print(res[i].split('<span class="aVSTQd tNxQIb OSrXXb">')[1].split("</span>")[0])
        print(res[i].split('<span class="aVSTQd tNxQIb OSrXXb">')[1].split("</span>")[1]).split('<div>')[1]
        # print(res[i].split('class="OSrXXb">')[1].split("Tourist attraction</div><div>")[1].split("</div>")[0])
    print("22222222222222222222222222222222")
    if len(result)==0:
        res=source.split('<span class="OSrXXb">')
        for i in range(1,len(res)):
            try:
                print(res[i].split('</span>')[1].split('</div><div>')[2].split('</div>')[0])
                print(res[i].split('</span>')[0])
                [print("=============")]
                print(res[i].split('</span>')[1].split('</div><div>')[2].split('</div>'))

                h=res[i].split('</span>')[0]+' '+res[i].split('</span>')[1].split('</div><div>')[2].split('</div>')[0]

                result.append(h)
            except:
                print("++++++++++++=")
                print(res[i].split('</span>'))
                print(res[i].split('School</div><div>')[1].split('</div><div>')[0])
                h = res[i].split('</span>')[0]+' '+res[i].split('School</div><div>')[1].split('</div><div>')[0]

                result.append(h)
    print("333333333333333333333333333333")
    if len(result)==0:
        res=source.split('<div class="r2fjmd VCOFK WyGS9c">')
        for i in range(1,len(res)):
            print(res[i].split('">')[1].split("</div>")[0])
            result.append(res[i].split('">')[1].split("</div>")[0])
    print(result)
    driver.quit()
    return result

# school_search("7J3R446C%2B46")
