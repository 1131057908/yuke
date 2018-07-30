from urllib.request import urlopen
from urllib.parse import quote
import string
import json
import sqlite3

class Guide(object):
    def __init__(self):
        self.connect = None
        self.cursor = None

    def createDBAndTable(self):
        self.connect = sqlite3.connect('travelDB')
        self.cursor = self.connect.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS city_table(city TEXT,time TEXT,des TEXT,name text)')
        self.connect.commit()

    def addAndAaveAllInfo(self,url):
        response = urlopen(quote(url, safe=string.printable))
        responseData = response.read()
        responseJson = json.loads(responseData)
        result1 = responseJson['result']['cityname']
        for dic in responseJson['result']['itineraries']:
            name = []
            time = dic['name']
            des = dic['description']
            for dic1 in dic['itineraries']:
                for dic2 in dic1['path']:
                    result2 = dic2['name']
                    name.append(result2)
            self.cursor.execute('INSERT INTO city_table VALUES ("{}","{}","{}","{}")'.format(result1, time, des, name))
            self.connect.commit()

    def selectInfo(self,customer):
        self.cursor.execute('SELECT name FROM city_table WHERE city="{}"AND time="{}"'.format(customer.city, customer.time))
        result = self.cursor.fetchall()
        print(result)

class Customer(object):
    def __init__(self,city='',time=''):
        self.city=city
        self.time=time


g = Guide()
c = Customer('北京','三日游')
g.createDBAndTable()
# g.addAndAaveAllInfo('http://api.map.baidu.com/telematics/v3/travel_city?location=北京&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json')
# g.addAndAaveAllInfo('http://api.map.baidu.com/telematics/v3/travel_city?location=杭州&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json')
# g.addAndAaveAllInfo('http://api.map.baidu.com/telematics/v3/travel_city?location=上海&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json')
# g.addAndAaveAllInfo('http://api.map.baidu.com/telematics/v3/travel_city?location=郑州&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json')
# g.addAndAaveAllInfo('http://api.map.baidu.com/telematics/v3/travel_city?location=洛阳&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json')
g.selectInfo(c)




























































































