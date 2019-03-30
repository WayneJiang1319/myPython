# python解析xml有三种方式，SAX、DOM、ElementTree
# SAX（simple API for XML）:SAX解析器用于事件驱动模型，在解析xml过程中触发一个个事件并调用用户定义的回调函数来处理xml文件
# DOM（Document Object Model）：将xml数据在内存中解析成一个树，通过对树的操作来操作XML

# 使用SAX解析xml文件
# SAX解析xmml文件涉及到两个部分：解析器+事件处理器。
# 解析器负责读取xml文档，并向事件处理器发送事件，比如元素开始和元素结束事件
# 事件处理器赋值对事件进行响应，对传递的xml数据进行处理
# python中使用sax方法处理xml需要先引入xml.sax中的parse函数，还有xml.sax.hander中的contentHandler


# from xml import sax
import xml.sax

class MoiveHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.content=""
        self.tag="" # tag：xml文件名称

    # 元素开始调用
    def startElement(self,name,attrs):
        self.tag=name
        if name=="collection":#
            print("**************collection****************")
        if self.tag=="movie":
            print("MOVIES:"+attrs["title"])
            print("-----------------------------------------")

     # 元素结束调用
    def endElemnet(self,name):
        if name == "collection":
            print("**************collection****************")
        elif name == "type":
            print("Type:"+self.content)
        elif name == "format":
            print("format:"+self.content)
        elif name == "year":
            print("year:"+self.content)
        elif name == "rating":
            print("rating:"+self.content)
        elif name == "stars":
            print("stars:"+self.content)
        elif name == "description":
            print("description:"+self.content)
        else:
            pass
    # 读取字符时调用
    def characeters(self,content):
        self.content=content


if __name__=="__main__":
   handler = MoiveHandler()
   xml.sax.parse("collection.xml",handler)











