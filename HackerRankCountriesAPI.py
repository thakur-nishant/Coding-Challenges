import sys
import os
import urllib.request
import json
def  getCountries(str, p):
    try:
        url = "https://jsonmock.hackerrank.com/api/countries/search?name={}".format(str)
        response = urllib.request.urlopen(url)
        response_data = json.loads(response.read().decode('utf-8'))
    except:
        return 0
    count = 0
    total_pages = response_data['total_pages']
    for page in range(1,total_pages+1):
        url = "https://jsonmock.hackerrank.com/api/countries/search?name={}&page={}".format(str,page)
        response = urllib.request.urlopen(url)
        response_data = json.loads(response.read().decode('utf-8'))
        for i in response_data['data']:
            if i['population'] > p:
                count += 1
    return count

s = "un"
p = 100090
x = getCountries(s,p)
print(x)


