from amazonproduct import API
import operator
#NOTE - $ price formatting has not been implemented (since it screws up the sorting stuff)   
config ={
    'access_key': 'AKIAIE3MWTF3ITAIP4OA',
    'secret_key': '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',
    'associate_tag': 'appr0c9-20',
    'locale': 'us',
    }

api = API(cfg=config)
#returns a tuple with (name, unformatted-price-but-with-decimal-point, page-url, img-url(medium-size), height, width)
def blendedsearch(searchwords):
    items = api.item_search('All', Keywords=searchwords)
    d=[]
    ids = []
    products = []
    for i in items:
        ids.append(i.ASIN)
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

print blendedsearch("fluffy")
        
'''
api = API(locale='de')

# get all books from result set and
# print author and title
for book in api.item_search('Books', Publisher='Galileo Press'):
    print '%s: "%s"' % (book.ItemAttributes.Author,
                        book.ItemAttributes.Title)
'''
