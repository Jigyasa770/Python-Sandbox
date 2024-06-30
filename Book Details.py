class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print('The title is: ', self.title)
        print('The author is: ', self.author)
        print('The price is: ', self.price)

a = Book('FAMOUS FIVE', 'ENID BLYTON', 2000)
print(a.show_details())