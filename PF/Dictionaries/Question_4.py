# Delete Dictionary Items
# Given:
# book = {
#     "title": "Python Basics",
#     "author": "John",
#     "price": 1200,
#     "pages": 350
# }
# Delete:
# "price"
# "pages"
# Print the remaining dictionary.


book = {
    "title": "Python Basics",
    "author": "John",
    "price": 1200,
    "pages": 350
}
book.pop("price")
book.pop("pages")
print(book)