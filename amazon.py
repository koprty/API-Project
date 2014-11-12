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
            num = 8
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

            d.append(  (name, float("{0:.2f}".format(price/100.0)), link, imglink)) #cannot add dollarsign or else it messes up sorting
        except AttributeError:
            pass
    sortedd=sorted(d, key=operator.itemgetter(1), reverse=False)
    for i, x in enumerate(sortedd):
        sortedd[i] = {'name':sortedd[i][0],'price':sortedd[i][1],'url':sortedd[i][2],'img_url':sortedd[i][3]}
    return sortedd

#print blendedsearch("lamy safari fountain pen")

