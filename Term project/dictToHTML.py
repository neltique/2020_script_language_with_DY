def dictToHTML(InfoDict):
    sum = """"""

    if 'title' in InfoDict:
        sum += """<h2 style="text-align: center">""" + InfoDict['title'] + """</h2>"""
    if 'firstimage' in InfoDict:
        sum += """<p style="text-align: center"><img src="""+'"'+InfoDict['firstimage']+'"'+""" alt="없음" width = "300" height = "200"></p>"""
    if 'addr1' in InfoDict:
        sum+="""<font size =5><b>주소</b></font><br><font size = 4>""" + InfoDict['addr1'] + """</font><br><br>"""
    if 'tel' in InfoDict:
        sum += """<font size =5><b>전화번호</b></font><br><font size = 4>""" + InfoDict['tel'] + """</font><br><br>"""
    if 'homepage' in InfoDict:
        sum += """<font size =5><b>홈페이지</b></font><br><font size = 4>""" + InfoDict['homepage'] + """</font><br><br>"""
    if 'zipcode' in InfoDict:
        sum += """<font size =5><b>우편번호</b></font><br><font size = 4>""" + InfoDict['zipcode'] + """</font><br><br>"""
    if 'overview' in InfoDict:
        sum += """<font size =5><b>상세내용</b></font><br><font size = 4>""" + InfoDict['overview'] + """</font>"""

    HTML = """<!doctype html>
    <html lang="ko">
    	<head>
    	<meta charset="utf-8">
    		<title>HTML</title>
    	</head>
    
    
    <body >
    """+sum+"""
        
    </body>
    
    </html>"""
    return HTML


