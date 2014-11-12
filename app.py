from flask import Flask, render_template, request, redirect
from amazon import blendedsearch
from ebay import ebaysearch

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result",methods=['GET','POST'])
def search():
    if request.method=='POST':
        query = request.form['query']
        print query
        amazon = blendedsearch(query,8)
        ebay = ebaysearch(query,8)
        return render_template("result.html",amazon=amazon, ebay=ebay)
    else:
        return "Bleh."

if __name__ == "__main__":
    app.run(debug=True,port=9233)
