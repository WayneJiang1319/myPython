# DOM：document Object Model
# DOM解析原理：一个DOM解析器在解析一个xml文档时，会一次性读取整个文档，把文档中所有的元素保留在内存中一个树结构中。
# 可以利用DOM提供的不同函数来读取或者修改xml文档的内容和结构
# python中用xml.dom.minidom来解析xml文件

from xml.dom.minidom import parse

# 加载xml文档
doc=parse("book.xml")
# 获取元素的根节点
root=doc.documentElement
# 获取元素的子节点，得到的一个数组
books=root.getElementsByTagName('book')


# 遍历所有的子节点
for book in books:
    print("==book==")
    # 如果book有id属性，则输出id值
    if book.hasAttribute('id'):
        print("book ID is："+book.getAttribute("id"))
    # 根据标签名找到，并输出第一个元素
    bookname = book.getElementsByTagName("bookname")[0]
    # 输出标签名子节点的第一值，并转换为data类型
    print("书名是："+bookname.childNodes[0].data)
    author = book.getElementsByTagName("author")[0]
    print("作者是："+author.childNodes[0].data)
    price = book.getElementsByTagName("price")[0]
    print("价格是："+price.childNodes[0].data)
