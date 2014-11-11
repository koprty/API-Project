from amazonproduct import API
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
    print ids
    for asin in ids:
        product = api.item_lookup(str(asin), ResponseGroup="ItemAttributes")
        productprice = api.item_lookup(str(asin),ResponseGroup='OfferFull')
        
        name = product.Items.Item.ItemAttributes.Title
        price = productprice.Items.Item.OfferSummary.LowestNewPrice.FormattedPrice
        d[name] = price
    return d
        
'''d[product.ItemAttributes.title]= product.ItemAttributes.title
#d[product.title] = product.price_and_currency
    print d'''
#booksearch()

<<<<<<< HEAD
def code(searchWord):
    pageNo = 1
    result = api.item_search('All', Keywords=searchWord, ResponseGroup='Large', ItemPage=pageNo, MerchantId='All')
    for item in result:
        try:
            print item.ItemAttributes.Title
        except (UnicodeEncodeError):
            pass
    prices = api.item_lookup('All', Keywords=searchWord, ResponseGroup='Offers', ItemPage=pageNo, MerchantId='All')
    for item in prices.Items.Item.Offers.Offer:
        try:
            print item.OfferListing.Price.FormattedPrice
        except (UnicodeEncodeError):
            pass
=======
blendedsearch("Bracelet")
>>>>>>> 8f59cb5e89b948eeda775d7bc9f2e3c62b0df7aa

print blendedsearch("fluffy")
        
'''
api = API(locale='de')

# get all books from result set and
# print author and title
for book in api.item_search('Books', Publisher='Galileo Press'):
    print '%s: "%s"' % (book.ItemAttributes.Author,
                        book.ItemAttributes.Title)
'''
