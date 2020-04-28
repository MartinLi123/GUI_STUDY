from PyQt5.Qt import *
import sys

'''
控件的设计使用面向对象的继承思想
子类拥有父类的属性和方法（共性）同时可以设置自己的属性和方法（特性）

'''

def main():
    # print(QObject.__subclasses__())
    # for cont in QObject.__subclasses__():
    #     print(cont)
    # print("")
    # for cont in QWidget.__subclasses__():
    #     print(cont)
    getSubclass(QWidget)

class Window(object):
    def __init__(self, tittle, size=(500, 500)):
        self.window = QWidget()
        self.window.setWindowIconText(tittle)
        self.window.resize(size)

def getSubclass(cls_name):
    print(cls_name, "的子类有：")
    for subClass in cls_name.__subclasses__():
        print(subClass)
        if len(subClass.__subclasses__()) > 0:
            getSubclass(subClass)
        print("")

if __name__ == '__main__':
    main()
