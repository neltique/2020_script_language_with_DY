import http.client
import xml.etree.ElementTree as ET

KEY = "%2F55799HZ4kWNygjCbwyB9fnm1HiDsnrOWQPwhswXwAU0B0EhbbV2%2FHdupErIVW0oyYaCU25Gis12h7QoZJJu3A%3D%3D"


class tour():
    def __init__(self):
        self.conn = http.client.HTTPConnection("api.visitkorea.or.kr")
        self.url = "/openapi/service/rest/KorService/areaCode?" + "serviceKey="+ KEY + "&"

        self.numOfRows = "17"
        self.areaCode = ""
        self.updateUrl()

        self.conn.request("GET",self.url)
        self.req = self.conn.getresponse()

        self.tree = ET.fromstring(self.req.read().decode('utf-8'))
        self.get = self.tree.findall("body/items/item")

    def updateUrl(self):
        self.url = self.url + "numOfRows="+self.numOfRows+"&pageNo=1&MobileOS=ETC&MobileApp=Tour&areaCode="+self.areaCode+"&"

    def initAreaCode(self):
        self.areaCode = ""

    def initNumOfRows(self):
        self.numOfRows = ""

    def getNumOfRows(self):
        return int(self.tree.find("body/totalCount").text)

    def setNumOfRows(self):
        self.numOfRows = "17"

    def requestUrl(self):
        pass

    def findData(self,string):
        for item in self.get:
            print(item.find(string).text)



T = tour()

T.findData("code")






