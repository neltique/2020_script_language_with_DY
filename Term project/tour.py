import http.client
import xml.etree.ElementTree as ET

KEY = "%2F55799HZ4kWNygjCbwyB9fnm1HiDsnrOWQPwhswXwAU0B0EhbbV2%2FHdupErIVW0oyYaCU25Gis12h7QoZJJu3A%3D%3D"


class tour():
    def __init__(self):
        self.conn = http.client.HTTPConnection("api.visitkorea.or.kr")
        self.url = ""
        self.function = "areaCode"
        self.numOfRows = "1"
        self.areaCode = ""



    def updateUrl(self):
        self.url = "/openapi/service/rest/KorService/" +self.function+ "?serviceKey="+ KEY +"&numOfRows="+self.numOfRows+"&pageNo=1&MobileOS=ETC&MobileApp=Tour&areaCode="+self.areaCode+"&"

    def updateNumOfRows(self):
        self.numOfRows = self.getNumOfRows()

    def initAreaCode(self):
        self.areaCode = ""

    def getAreaCode(self):
        return self.areaCode

    def setAreaCode(self, num):
        self.areaCode = num

    def initNumOfRows(self):
        self.numOfRows = ""

    def getNumOfRows(self):
        return self.tree.find("body/totalCount").text

    def setNumOfRows(self,num):
        self.numOfRows = str(num)

    def requestUrl(self):
        self.conn.request("GET",self.url)
        self.req = self.conn.getresponse()

    def updateTree(self,string):
        self.tree = ET.fromstring(self.req.read().decode('utf-8'))
        self.get = self.tree.findall(string)


    def makeAreaCode(self):    # 시/도 만들기 위해
        self.updateUrl()        # 첫 url 주소 받기
        self.requestUrl()       # 요청
        self.updateTree("body/items/item") #첫 tree만들기 - totalCount를 얻기 위해
        self.updateNumOfRows()  # toalCount로 numOfRows 변경
        self.updateUrl()        # 변경된 numOfRows 적용
        self.requestUrl()       # 변경된 numOfRows를 적용한 url 요청
        self.updateTree("body/items/item")  # 변경된 numOfRows를 적용한 url tree 만들기

        lst1 = []
        lst2 = []
        for item in self.get:
            lst1.append(item.find('name').text)
            lst2.append(item.find('code').text)
        dic = dict(zip(lst1,lst2))

        return dic

    def makeAreaCode2(self):
        self.updateUrl()  # 첫 url 주소 받기
        self.requestUrl()  # 요청
        self.updateTree("body/items/item")  # 첫 tree만들기 - totalCount를 얻기 위해
        self.updateNumOfRows()  # toalCount로 numOfRows 변경
        self.updateUrl()  # 변경된 numOfRows 적용
        self.requestUrl()  # 변경된 numOfRows를 적용한 url 요청
        self.updateTree("body/items/item")  # 변경된 numOfRows를 적용한 url tree 만들기








