import urllib.request
from urllib.request import Request
import ssl

from bs4 import BeautifulSoup
url = "https://www.dontpayfull.com/at/ebay.com"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urllib.request.urlopen(req,context=ctx)
soup_packtpage = BeautifulSoup(page, "html.parser")

soup_packtpage.findAllNext ('div', class_=['product', 'details', 'product-item-details'], limit=1)


UrlsArray=[]
titleArray=[]
EndsArray=[]
olabel_code_Array=[]
Data_Id_Array=[]
"""The Main Function"""

def get_detailed_data(soup):
   title = soup.findAll("div", {"class": "otitle"})
   for item in title:
    titl = item.text
    titleArray.append(titl.replace('\n',' '))

   Ends = soup.findAll("div", {"class": "oexpire"})
   for item in Ends:
     End = item.text
     EndsArray.append(End.replace('\n', ' '))

   olabel_code = soup.findAll("div", {"class": "olabel code"})
   for item in olabel_code:
     olabel_cod = item.text
     olabel_code_Array.append(olabel_cod.replace('\n', ' '))
   """Get the Data id so we can do and new Url"""
   pagecode = soup_packtpage.findAll("ul", {"class": "coupons-container"})
   urls = [item.findAll('li', {"class": "obox code clearfix"}) for item in pagecode]
   for item in pagecode:
      urls = item.findAll('li', {"class": "obox code clearfix"})
   iddata = [item.get('data-id') for item in urls]
   for i in range(len(iddata)):
    UrlsArray.append("https://www.dontpayfull.com/at/ebay.com"+"c="+iddata[i]+"#"+"c"+iddata[i])

   data = {

     'title': titleArray,
     'Ends ': EndsArray,
     'code+deal+Sponsored': olabel_code_Array,
     'Data  Id': iddata,
     'Data Id Urls ':UrlsArray
   }
   return data

print(get_detailed_data(soup_packtpage))












