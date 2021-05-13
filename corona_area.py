import requests
from pprint import pprint
from datetime import date, timedelta
import xmltodict
import json

def get_city_data():
    url= "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"

    # 오늘 어제 계산
    today = date.today()
    yesterday = today - timedelta(days=1)

    # 시간데이터->문자열로 만들기
    today = today.strftime("%Y%m%d") # 20200604
    yesterday = yesterday.strftime("%Y%m%d") # 20200603
    print(today, yesterday)

    params ={
        'serviceKey':'fSTuUhMmq16ajlOFNVaTghszpQuXjHda9CMS13w3f8YYnIXrsskicuF5kGHogjZD7NLJvzYlQEPe9QKrREwe5w==',
        'pageNo': '1',
        'numOfRows': '30',
        'startCreateDt' : yesterday, # '20200603',
        'endCreateDt': today, # '20200604',
    }

    res = requests.get(url, params=params)
    # print(res.text)

    # xml->dict
    dict_data = xmltodict.parse(res.text)
    # print(dict_data)

    # xml->dict->json->dict
    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)
    # print(dict_data)

    # items만 확인
    items = dict_data['response']['body']['items']['item']
    # print(items)

    # 날짜로 필터
    # 'createDt': '2020-06-16 11:32:18.509' 에서 `2020-06-16`를 검사할 것임
    f_string = date.today().strftime("%Y-%m-%d")

    # 만일 오늘 데이터가 있다면 오늘 날짜 데이터만 쏙 골라내기
    results = []
    if f_string in items[0]['createDt']:
        for item in items:
            if f_string in item['createDt']:
                results.append(item)
    else :
        results = items # 어제 날짜면 그대로
    # print(results)

    # 역순 정렬( 검역->서울->합계를 합계->서울-검역 순으로)
    results.reverse()
    # print(results)
    return results

# 테스트 코드
if __name__ == "__main__":
    print(get_city_data())