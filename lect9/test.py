import requests
from xml.dom import minidom
from xml.dom.minidom import Node
api_key = "hu52sTh3n%2FVfgNDnXWZ%2FbO7GJnWth5EWloJPowEnFfIhxw8v%2BfMe2D9erS4shyGoz1FjwGnbsEDkW4cIPS9ygQ%3D%3D"
api_key_decode = requests.utils.unquote(api_key) 
parameters = {
    "ServiceKey":api_key_decode,
    "numOfROws":1, "pageNo":1,
    "startCreateDt":20200806,
    "endCreateDt":20200807} 
req = requests.get("http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?", params = parameters)
xmlraw = minidom.parseString(req.text)
clist= xmlraw.getElementsByTagName('item')
tree = clist[0].toxml()
for node in clist:
    alist = node.getElementsByTagName('decideCnt')
    for a in alist:
        title = a.firstChild.data
        print("확진자 수 " ,title)