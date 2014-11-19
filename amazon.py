from amazonproduct import API
import operator

####################################################
#replace below config stuff

####################################################

api = API(cfg=config)
#returns a dictionary
def blendedsearch(searchwords,num=None):
    d = []
    items = api.item_search('All',Availability="Available", Keywords=searchwords,ResponseGroup='Large')   
    if num == None:
        num = 8
    
    for i, item in enumerate(items):
        if i > num:
            break
        #print i
        try:
            name = item.ItemAttributes.Title
            price = item.OfferSummary.LowestNewPrice.Amount
            link = item.DetailPageURL
            imglink = item.MediumImage.URL
        
            d.append(  (name, float("{0:.2f}".format(price/100.0)), link, imglink)) #cannot add dollarsign or else it messes up sorting
        except AttributeError:
            pass
    #sortedd = a list of tuples in format-> (name, unformatted-price-but-with-decimal-point, page-url, img-url(medium-size))
    sortedd=sorted(d, key=operator.itemgetter(1), reverse=False)
    for i, x in enumerate(sortedd):
        sortedd[i] = {'name':sortedd[i][0],'price':sortedd[i][1],'url':sortedd[i][2],'img_url':sortedd[i][3]}
    return sortedd

#blendedsearch("lamy safari fountain pen",2)
