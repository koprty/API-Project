from amazonproduct import API

api = API(locale='us')
items = api.item_search('Books', Publisher="O'Reilly")
'''
api = API(locale='de')

# get all books from result set and
# print author and title
for book in api.item_search('Books', Publisher='Galileo Press'):
    print '%s: "%s"' % (book.ItemAttributes.Author,
                        book.ItemAttributes.Title)
'''
