import os
import sys
import urllib.request
import datetime
import json
import pandas as pd
import re
import html  # HTML 엔티티 변환을 위한 모듈

client_id = '2JmlVSnmtVzUk7n58aDK'
client_secret = 'f4t57D2Atl'

title1 = []
pDate1 = []
description1 = []
org_link1 = []
link1 = []
dt_now = datetime.datetime.now().strftime('%Y-%m-%d')

def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?sort=sim&query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = base + node + parameters
    responseDecode = getRequestUrl(url)

    if responseDecode is None:
        return None
    else:
        return json.loads(responseDecode)

def getPostData(post, jsonResult, cnt):
    cleanr = re.compile('<.*?>')
    
    title = post['title']
    titlec = re.sub(cleanr, '', title)
    titlec = html.unescape(titlec)  # HTML 엔티티 변환
    description = post['description']
    descriptionc = re.sub(cleanr, '', description)
    descriptionc = html.unescape(descriptionc)  # HTML 엔티티 변환
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    title1.append(titlec)
    description1.append(descriptionc)
    org_link1.append(org_link)
    link1.append(link)
    pDate1.append(pDate)

    jsonResult.append({
        'cnt': cnt,
        'title': titlec,
        'description': descriptionc,
        'org_link': org_link,
        'link': link,
        'pDate': pDate
    })
    return

def main():
    node = 'news'
    srcText = input('검색어를 입력하세요: ')
    cnt = 0
    jsonResult = []
    
    jsonResponse = getNaverSearch(node, srcText, 1, 10)
    if jsonResponse is None:
        print("검색 결과가 없습니다.")
        return

    total = jsonResponse['total']
    
    while jsonResponse is not None and jsonResponse['display'] != 0:
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)
            
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)
        
    print('전체 검색 : %d 건' % total)
        
    df = pd.DataFrame({
        '제목': title1,
        '날짜': pDate1,
        '내용': description1,
        '원래주소': org_link1,
        '네이버뉴스주소': link1
    })

    output_path = os.path.join('log', f'{dt_now}_{srcText}.xlsx')
    df.to_excel(output_path, index=False)

    print("가져온 데이터 : %d 건" % cnt)

if __name__ == '__main__':
    main()
