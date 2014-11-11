from amazonproduct import API
import operator
config ={
    'access_key': 'AKIAIE3MWTF3ITAIP4OA',
    'secret_key': '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',
    'associate_tag': 'appr0c9-20',
    'locale': 'us',
    }

api = API(cfg=config)

def booksearch ():
    items = api.item_search('Books', Publisher="O'Reilly")
    for book in items:
        print '%s: "%s"' % (book.ItemAttributes.Author,
                            book.ItemAttributes.Title)

def blendedsearch(searchwords):
    items = api.item_search('All', Keywords=searchwords)
    d={}
    ids = []
    products = []
    for i in items:
        ids.append(i.ASIN)
    for asin in ids:
        product = api.item_lookup(str(asin), ResponseGroup="ItemAttributes")
        productprice = api.item_lookup(str(asin),ResponseGroup="OfferFull")
        
        name = product.Items.Item.ItemAttributes.Title
        price = productprice.Items.Item.OfferSummary.LowestNewPrice
        print name, price

        d[name] = price/100

    sortedd=sorted(d.items(), key=operator.itemgetter(1), reverse=False)
    return sortedd
        
print blendedsearch("bracelet")
        
'''
api = API(locale='de')

# get all books from result set and
# print author and title
for book in api.item_search('Books', Publisher='Galileo Press'):
    print '%s: "%s"' % (book.ItemAttributes.Author,
                        book.ItemAttributes.Title)
'''
