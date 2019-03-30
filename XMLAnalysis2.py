from xml.sax import parse, ContentHandler #引入继承包ContentHandler


#书的类
class Book:
    #定义初始化属性，和xml文件属性相同
    def __init__(self,bookname=None,author=None,price=None):
        self.bookname=bookname
        self.author=author
        self.price=price
    def __str__(self):  #转化为字符串输出
        return self.bookname+","+self.author+","+self.price

books=[]#定义一个书的数组,用来存放每次得到的数据

#定义继承ContentHandler的类，可以实现相应的方法
class bkdemo(ContentHandler):
    def __init__(self):
        #定义全局变量
        self.book=None #用来接收book的相应数据
        self.tag=None  #用来接收characters方法得到的content内容
    def startDocument(self): #books对象开始
        print("对象开始")
    def endDocument(self):  #books对象结束
        print("对象结束")
    def startElement(self, name, attrs): #每一个标签元素的开始，name：标签名称 attrs:标签内部相应属性
        if name=='book':  #如果标签名是book
            self.book=Book()  #创建一个Book()对象
    def endElement(self, name):  #每一个标签元素的结束，name：标签名称 （此时才会得到相应的content）
        if name=='bookname':
            self.book.bookname=self.tag  #对象的标签名=得到相应content的值
        if name=='author':
            self.book.author=self.tag
        if name=='price':
            self.book.price=self.tag
        if name=='book':
            books.append(self.book)  #为定义的数组追加得到的相应元素

    def characters(self, content):
        self.tag=content   #写了self的，就可以定义为全局变量


parse("book.xml",bkdemo())  #parse的方法，分别指明xml文件，并调用查找的类方法
for i in books:   #对数组books[]循环
    print(i)
