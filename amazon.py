from amazonproduct import API
import operator
#NOTE - $ price formatting has not been implemented (since it screws up the sorting stuff)   

####################################################
#replace below config stuff
config ={
    'access_key': 'AKIAJLFLMJ7JSZKLEE4A',
    'secret_key': 'j6VMclIgFyvh0MLW5dLvWLlXkouLpf04VsPPOJo/',
    'associate_tag': 'appr0c9-20',
    'locale': 'us',
}
####################################################

api = API(cfg=config)
#returns a list of tuples in format-> (name, unformatted-price-but-with-decimal-point, page-url, img-url(medium-size), height, width)
def blendedsearch(searchwords):
    items = api.item_search('All', Keywords=searchwords)
    d=[]
    ids = []
    products = []
    counter = 0;
    for i in items:
        ids.append(i.ASIN)
        counter+=1;
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
    for i in enumerate(d):
        d[i] = {'name':d[i][0],'price':d[i][1],'url':d[i][2],'img_url':d[i][3],'img_height':d[i][4],'img_width':d[i][5]}
    print counter
    return sortedd

print blendedsearch("lamy safari fountain pen")

