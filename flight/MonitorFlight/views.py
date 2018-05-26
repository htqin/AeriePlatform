from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from pymongo import MongoClient
from collections import Counter
import json
import jieba

days = [1467302400 , 1467388800 , 1467475200 , 1467561600 , 1467648000 , 1467734400 , 1467820800 , 1467907200]

def index(request):#调用显示网站主页
    return render(request, 'index.html')

def video(request):#调用显示网站主页
    return render(request, 'video.html')

def video1(request):#调用显示网站主页
    return render(request, 'video1.html')

def video2(request):#调用显示网站主页
    return render(request, 'video2.html')

def WordsSort(request):
    file = "C:/Users/Fox/Downloads/train.csv"
    temp = []
    with open(file, 'r',  newline='') as f:
        line = ""
        try:
            line = f.readline()
        except:
            line = ""
        seg_content = jieba.cut(line[2])
        for x in seg_content:
            if(len(x) > 3):
                temp.append(x)
    counter = Counter(temp)
    count_pairs = counter.most_common(20)
    words, _ = list(zip(*count_pairs))
    list1 = []
    num = 40
    for x in words:
        list1.append([x, num/4])
        num -= 1
    return list1

def LoadPoints(request):#数据打包传递到网页端
    settings.DAY = (settings.DAY + 1) % 7
    client = MongoClient('localhost', 27017)
    db = client.flightradar_data
    collection = db.Monitor
    Start = days[settings.DAY]
    End   = days[settings.DAY + 1]
    #data = collection.find({'lon': {"$gt": -130, "$lt": -70}, 'lat': {"$gt": 29, "$lt": 49},'timestamp': {"$gt": Start, "$lt": End}})
    data = collection.find({'timestamp': {"$gt": Start, "$lt": End}})
    Points = []
    for item in data:
        Points.append({"lng":item['lon'],"lat":item['lat'],"count":0.5})
    return HttpResponse(json.dumps(Points), content_type='application/json')

def LoadHeight(request): #机场数据打包传递到网页端
    client = MongoClient('localhost', 27017)
    db = client.flightradar_data
    collection = db.Monitor

    Start = days[settings.DAY]
    End = days[settings.DAY + 1]

    data = collection.find({'lon': {"$gt": -130, "$lt": -70}, 'lat': {"$gt": 29, "$lt": 49},
                            'timestamp': {"$gt": Start, "$lt": End} , 'height' : {"$lt" : 8100}})
    lower_8100 = []
    for item in data:
        lower_8100.append([item['lon'] , item['lat']])
    data = collection.find({'lon': {"$gt": -130, "$lt": -70}, 'lat': {"$gt": 29, "$lt": 49},
                            'timestamp': {"$gt": Start, "$lt": End}, 'height': {"$gt": 8100 , "$lt": 12500}})
    between_8100_12500 = []
    for item in data:
        between_8100_12500.append([item['lon'], item['lat']])
    data = collection.find({'lon': {"$gt": -130, "$lt": -70}, 'lat': {"$gt": 29, "$lt": 49},
                            'timestamp': {"$gt": Start, "$lt": End}, 'height': {"$gt": 12500 }})
    higher_12500 = []
    for item in data:
        higher_12500.append([item['lon'], item['lat']])
    return HttpResponse(json.dumps([lower_8100 , between_8100_12500 , higher_12500]), content_type='application/json')

def LoadHeightLow(request): #机场数据打包传递到网页端


    Start = days[settings.DAY]
    End = days[settings.DAY + 1]

    client = MongoClient('localhost', 27017)
    db = client.flightradar_data
    collection = db.Monitor
    data = collection.find({'lon': {"$gt": -130, "$lt": -70}, 'lat': {"$gt": 29, "$lt": 49},
                            'timestamp': {"$gt": Start, "$lt": End} , 'height' : {"$lt" : 8100}})
    lower_8100 = []
    for item in data:
        lower_8100.append([item['lon'] , item['lat']])

    return HttpResponse(json.dumps(lower_8100), content_type='application/json')

def LoadHeightMid(request): #机场数据打包传递到网页端


    Start = days[settings.DAY]
    End = days[settings.DAY + 1]

    client = MongoClient('localhost', 27017)
    db = client.flightradar_data
    collection = db.Monitor

    data = collection.find({'lon': {"$gt": -130, "$lt": -70}, 'lat': {"$gt": 29, "$lt": 49},
                            'timestamp': {"$gt": Start, "$lt": End}, 'height': {"$gt": 8100 , "$lt": 12500}})
    between_8100_12500 = []
    for item in data:
        between_8100_12500.append([item['lon'], item['lat']])

    return HttpResponse(json.dumps( between_8100_12500), content_type='application/json')

def LoadHeightHig(request): #机场数据打包传递到网页端

    Start = days[settings.DAY]
    End = days[settings.DAY + 1]

    client = MongoClient('localhost', 27017)
    db = client.flightradar_data
    collection = db.Monitor

    data = collection.find({'lon': {"$gt": -130, "$lt": -70}, 'lat': {"$gt": 29, "$lt": 49},
                            'timestamp': {"$gt": Start, "$lt": End}, 'height': {"$gt": 12500 }})
    higher_12500 = []
    for item in data:
        higher_12500.append([item['lon'], item['lat']])
    return HttpResponse(json.dumps(higher_12500), content_type='application/json')