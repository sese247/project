import json
import requests
import os
import django
from firstapp.models import Datasample

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mapproject.settings")
django.setup()

def gotaddress(addressList):
    conResult = []
    for add in addressList:
        try:
            result = getLatLng(add)
            match_first = result['documents'][0]['address']
        except:
            match_first = {'x': '0', 'y': '0'}      #주소가 이상하면 999로 셋팅
        context = {'address': add, 'x': float(match_first['x']), 'y': float(match_first['y'])}
        conResult.append(context)
    return (conResult)

def getLatLng(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
    headers = {"Authorization": "KakaoAK 1af4a3b899028e9720c99fc752d7986c"}
    result = json.loads(str(requests.get(url, headers=headers).text))
    return result

########################## 아래 테스트 ##########################

orgAddressList = []
alldata = Datasample.objects.all()
for data in alldata:
    orgAddressList.append(data.sisuladdr)

test = gotaddress(orgAddressList)


for chk in test:
    Datasample.objects.create(
        lat = chk['y'],
        lng = chk['x'],)
    print(chk['address'], ',', chk['x'], ',', chk['y'])