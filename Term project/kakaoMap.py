import urllib.request

import http.client
import xml.etree.ElementTree as ET


def mapDownLoad(mapx, mapy):
     server = 'dapi.kakao.com'
     key = 'c11cd41a6b4ce614ae81b1b07cc954eb'  # 본인 카카오앱키 입력
     header = {'Authorization': 'KakaoAK '+key}


     conn = http.client.HTTPSConnection(server)
     conn.request("GET", "/v2/local/geo/transcoord.xml?x="+mapx+"&y="+mapy+"&input_coord=WGS84&output_coord=WCONGNAMUL", None, header)
     req = conn.getresponse()
     rb = req.read().decode('utf-8')
     tree = ET.fromstring(rb)

     urlx = tree.find('documents/x').text
     urly = tree.find('documents/y').text

     for i in range(1, 16):
         url = 'https://ssl.daumcdn.net/map3/staticmap/image?srs=WCONGNAMUL&lv=' + str(i) + '&size=225x190&markers=symbol:sc_marker%7Clocation:' + urlx + ',' + urly
         urllib.request.urlretrieve(url, "maps/map" + str(i) + '.jpg')