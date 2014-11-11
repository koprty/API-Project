import urllib2
import json                                                                     
from flask import Flask, request, url_for, redirect, render_template            
from ebaysdk import finding                                                     
from ebaysdk.finding import Connection as finding                               
from requests.exceptions import ConnectionError
app=Flask(__name__)                                                             ##@app.route("/")                                                               
##return render_template("home.html")                                           ##@app.route("/ebay/<tag>")                                                     ##def t(tag=None)                                                               

@app.route("/")                                                                 
def home():                                                                     
    try:                                                                        
        api = finding(appid="Christin-2e88-4160-828c-885deb830846")             
        response = api.execute('findItemsAdvanced', {'keywords': 'shoes'})      
        print (response.dict())                                                 
    except ConnectionError as e:                                                
        print(e)                                                                
        print(e.response.dict())
if __name__=="__main__":
    app.debug=True
    app.run()                                                                                                                                                                                            
