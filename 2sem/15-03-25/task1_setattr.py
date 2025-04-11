class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
    def __setattr__(self, key, value):
        if key=='author' or key=='title':
            if not isinstance(value, str):
                raise TypeError('Wrong type!')
        if key=='pages' or key=='year':
            if not isinstance(value, int):
                raise TypeError('Wrong type!')
        object.__setattr__(self, key, value)

a = Book()
print(a.__dict__)