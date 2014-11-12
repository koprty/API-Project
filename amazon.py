from amazonproduct import API
import operator
#NOTE - $ price formatting has not been implemented (since it screws up the sorting stuff)   

####################################################
#replace below config stuff

####################################################

api = API(cfg=config)
#returns a list of tuples in format-> (name, unformatted-price-but-with-decimal-point, page-url, img-url(medium-size), height, width)
def blendedsearch(searchwords,num=None):
    items = api.item_search('All',Availability="Available", Keywords=searchwords)
    count =0
    d=[]
    ids = []
    products = []
    for i in items:
        ids.append(i.ASIN)
        count += 1
        if num == None:
            num = 10
        if count >num:
            break
    for asin in ids:
        try:
            product = api.item_lookup(str(asin)) #itemAttributes has name, brand, and other info
            productprice = api.item_lookup(str(asin),ResponseGroup="OfferFull") #price info
            image = api.item_lookup(str(asin),ResponseGroup="Images") #image info
 
            name = product.Items.Item.ItemAttributes.Title
            price = productprice.Items.Item.OfferSummary.LowestNewPrice.Amount
            link = product.Items.Item.DetailPageURL
            imglink = image.Items.Item.MediumImage.URL
            height = image.Items.Item.MediumImage.Height
            width = image.Items.Item.MediumImage.Width
            
            d.append(  (name, float("{0:.2f}".format(price/100.0)), link, imglink, height, width)   ) #cannot add dollarsign or else it messes up sorting
        except AttributeError:
            pass
    sortedd=sorted(d, key=operator.itemgetter(1), reverse=False)
    return sortedd
print blendedsearch("bracelet")


