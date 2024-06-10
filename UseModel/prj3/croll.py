import os
import sys
import urllib.request
client_id = "2JmlVSnmtVzUk7n58aDK"
client_secret = "f4t57D2Atl"
query = urllib.parse.quote(input('검색어'))
start = '1'
display='10'
sort ='sim'
url = "https://openapi.naver.com/v1/search/news?query=" + query + "&start="+start+"&display="+display+"&sort="+sort# JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    
    print(response_body.decode('utf-8'))
    
else:
    print("Error Code:" + rescode)