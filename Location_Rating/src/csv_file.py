import csv
import random
xx=[]
with open('rating.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["hospital", "school", "police_station","railway_station","tourist_place","Restaurant","river","church","temple","mosque","rating"])

    for i in range(0,100):
        r=[]
        for ii in range(0,10):


            x = random.random()


            r.append(x)
        r.append(10)
        xx.append(r)

    for i in range(0,100):
        r=[]
        for ii in range(0,10):
            x=random.random()+1
            r.append(x)
        r.append(9)
        xx.append(r)
    for i in range(0,100):
            r=[]
            for ii in range(0,10):
                x=random.random()+2
                r.append(x)
            r.append(8)
            xx.append(r)
    for i in range(0,100):
        r=[]
        for ii in range(0,10):
            x=random.random()+3
            r.append(x)
        r.append(7)
        xx.append(r)
    
    for i in range(0,100):
        r=[]
        for ii in range(0,10):
            x=random.random()+4
            r.append(x)
            
        r.append(6)
        xx.append(r)

    for i in range(0, 100):
        r = []
        for ii in range(0, 10):
            x = random.random() + 5
            r.append(x)

        r.append(5)
        xx.append(r)
    for i in range(0, 100):
        r = []
        for ii in range(0, 10):
            x = random.random() + 6
            r.append(x)

        r.append(4)
        xx.append(r)
    for i in range(0, 100):
        r = []
        for ii in range(0, 10):
            x = random.random() + 7
            r.append(x)

        r.append(3)
        xx.append(r)
    for i in range(0, 100):
        r = []
        for ii in range(0, 10):
            x = random.random() + 8
            r.append(x)

        r.append(2)
        xx.append(r)
    for i in range(0, 100):
        r = []
        for ii in range(0, 10):
            x = random.random() + 9
            r.append(x)

        r.append(1)
        xx.append(r)
    for i in xx:

            writer.writerow(i)

    
