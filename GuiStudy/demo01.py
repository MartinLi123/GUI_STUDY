from PyQt5.Qt import *  # 耗费一些内存将很多常用模块导入，对于初学者便于学习
import sys

def main():
    # 当使用命令行来调用该文件时，可以通过在文件名后接参数来将参数传入到arg列表内
    arg = sys.argv
    app = QApplication(arg)
    # arg 都被传入了app的arguments属性内
    print("app --- ", app.arguments())
    print("sys arg --- ",arg)
    print("qApp --- ", qApp.arguments())  # qApp是一个全局变量
    if arg[1] == "1":
        print("okkk")
    else:
        print("nooo")

def main2():
    pass

if __name__ == '__main__':
    # main()
    # # main2()
    pass

qApp.setStyleSheet("font-size:20px;color:red;")