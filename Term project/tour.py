import http.client
import xml.etree.ElementTree as ET

KEY = "SpWe9UpmMXVZh8MHhnRCpSeVMBO88OXs%2F%2FHIVBSWA3GLBFMhbV9i0WbynUMZ6G66WEUgerpPxoXEVU5DYrQRTg%3D%3D"
CONN = http.client.HTTPConnection("api.visitkorea.or.kr")

class AreaCodeXML():
    def __init__(self):
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

    def setAreaCode(self, areaCode):
        self.areaCode = areaCode

    def initNumOfRows(self):
        self.numOfRows = ""

    def getNumOfRows(self):
        return self.tree.find("body/totalCount").text

    def setNumOfRows(self,num):
        self.numOfRows = str(num)

    def requestUrl(self):
        CONN.request("GET",self.url)
        self.req = CONN.getresponse()

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

class AreaBasedList():
    def __init__(self):
        self.url = ""
        self.numOfRows = "1"
        self.areaCode = ""
        self.sigunguCode = ""


    def updateUrl(self):
        self.url = "/openapi/service/rest/KorService/areaBasedList?serviceKey="+KEY+"&pageNo=1&numOfRows="+self.numOfRows+"&MobileApp=tour&MobileOS=ETC&arrange=A&cat1=&contentTypeId=&areaCode="+self.areaCode+"&sigunguCode="+self.sigunguCode+"&cat2=&cat3=&listYN=Y&modifiedtime=&"

    def setAreaCode(self,areaCode):
        self.areaCode = areaCode

    def setSigunguCode(self, sigunguCode):
        self.sigunguCode = sigunguCode

    def updateNumOfRows(self):
        self.numOfRows = self.getNumOfRows()

    def getNumOfRows(self):
        return self.tree.find("body/totalCount").text

    def requestUrl(self):
        CONN.request("GET",self.url)
        self.req = CONN.getresponse()

    def updateTree(self,string):
        self.tree = ET.fromstring(self.req.read().decode('utf-8'))
        self.get = self.tree.findall(string)

    def makeAreaBasedList(self):    # 시/도 만들기 위해
        self.updateUrl()        # 첫 url 주소 받기
        self.requestUrl()       # 요청
        self.updateTree("body/items/item") #첫 tree만들기 - totalCount를 얻기 위해
        self.updateNumOfRows()  # toalCount로 numOfRows 변경
        self.updateUrl()        # 변경된 numOfRows 적용
        self.requestUrl()       # 변경된 numOfRows를 적용한 url 요청
        self.updateTree("body/items/item")  # 변경된 numOfRows를 적용한 url tree 만들기

        addrList = []
        titleList = []
        contentIdList = []
        for item in self.get:
            if item.find('addr1') == None:
                addrList.append('')
            else:
                addrList.append(item.find('addr1').text)
            if item.find('title') == None:
                titleList.append('')
            else:
                titleList.append(item.find('title').text)
            if item.find('contentid') == None:
                contentIdList.append('')
            else:
                contentIdList.append(item.find("contentid").text)



        return list(zip(titleList,addrList,contentIdList))

def makeDetail(contentId):
    url = "/openapi/service/rest/KorService/detailCommon?serviceKey="+KEY+"&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=tour&contentId="+contentId+"&contentTypeId=&defaultYN=Y&firstImageYN=Y&areacodeYN=Y&catcodeYN=Y&addrinfoYN=Y&mapinfoYN=Y&overviewYN=Y&"
    CONN.request("GET", url)
    req = CONN.getresponse()
    tree = ET.fromstring(req.read().decode('utf-8'))
    get = tree.findall("body/items/item")

    dic = {}
    for item in get:
        if item.find("addr1") != None:
            dic["addr1"]= item.find("addr1").text
        if item.find("firstimage") != None:
            dic["firstimage"] = item.find("firstimage").text
        if item.find("mapx") != None:
            dic["mapx"] = item.find("mapx").text
        if item.find("mapy") != None:
            dic["mapy"] = item.find("mapy").text
        if item.find("homepage") != None:
            dic["homepage"] = item.find("homepage").text
        if item.find("tel") != None:
            dic["tel"] = item.find("tel").text
        if item.find("zipcode") != None:
            dic["zipcode"] = item.find("zipcode").text
        if item.find("overview") != None:
            dic["overview"] = item.find("overview").text
        if item.find("title") != None:
            dic["title"] = item.find("title").text

    return dic
