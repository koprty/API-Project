import urllib2
import json                                                                     
from flask import Flask, request, url_for, redirect, render_template            
from ebaysdk import finding                                                     
from ebaysdk.finding import Connection as finding                               
from requests.exceptions import ConnectionError
app=Flask(__name__)                        

@app.route("/")
def home():
#def search(searchwords):                                                                
    try:                                                                        
        api = finding(appid="Christin-2e88-4160-828c-885deb830846")             
        response = api.execute('findItemsAdvanced', {'keywords': 'lamy safari fountain pen'}) ##replace pens with searchwords     
        res = response.dict()
        print res['itemSearchURL']
        res = res['searchResult']['item']
        page = ""
        for item in res:
       #     print item['itemId']
        #    print item['title']
         #   print item['sellingStatus']
            page = page + "<img height=200 src=%s>"%item['galleryURL']
            page = page + "<br><center><a href=%s>%s</a></center>"%(item['viewItemURL'],item['title'])
            page = page + "<br> <center> Price: $%s </center>"%(item['sellingStatus']['currentPrice']['value'])
            page = page + "<hr>"
        return page
    except ConnectionError as e:                                                
        print e                                                                
        print e.response.dict()
            
if __name__=="__main__":
    app.debug=True
    app.run()

