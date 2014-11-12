from ebaysdk import finding                                                     
from ebaysdk.finding import Connection as finding                               
from requests.exceptions import ConnectionError
import operator

def ebaysearch(searchwords,num=None):
    try:
        d=[]
        if num==None:
            num = 8
        api = finding(appid="Christin-2e88-4160-828c-885deb830846")             
        response = api.execute('findItemsAdvanced', {'keywords': searchwords})
        res = response.dict()
        print res['itemSearchURL']
        res = res['searchResult']['item']
        print res[0]['listingInfo']
        #print res
        for i, item in enumerate(res):
            if i > num:
                break
            name = item['title']
            price = float("{0:.2f}".format(float(item['sellingStatus']['currentPrice']['value'])))
            url = item['viewItemURL']
            img = item['galleryURL']
            listing = item['listingInfo']['listingType']
            if listing == "StoreInventory" or listing == "FixedPrice":
                listing = "Buy It Now"
            d.append( ( name, price, url, img, listing))
        sortedd=sorted(d, key=operator.itemgetter(1), reverse=False)
        for i, x in enumerate(sortedd):
            sortedd[i] = {'name':sortedd[i][0],'price':sortedd[i][1],'url':sortedd[i][2],'img_url':sortedd[i][3],'listing_type':sortedd[i][4]}
        return sortedd
    except ConnectionError as e:                                                
        print e                                                                
        return e.response.dict()
            
if __name__=="__main__":
    ebaysearch("safari lamy fountain pen",5)

