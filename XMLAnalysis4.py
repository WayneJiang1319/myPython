# ElementTree 元素树
# elementTree 就像一个轻量级的DOM
# https://www.cnblogs.com/qianshuixianyu/p/9184213.html
from xml.etree import ElementTree

class Book:
    def __init__(self,bookname=None,author=None,price=None):
        self.bookname=bookname
        self.author=author
        self.price=price

    def __str__(self):
        return self.bookname+","+self.author+","+self.price


roota=ElementTree.parse("book.xml")
bk=roota.findall("book")
boo=[]

for aa in bk:
    book=Book()
    book.bookname=aa.find("bookname").text
    book.author=aa.find("author").text
    book.price=aa.find("price").text
    boo.append(book)

for i in boo:
    print(i)
