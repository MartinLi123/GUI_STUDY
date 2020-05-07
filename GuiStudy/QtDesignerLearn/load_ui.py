import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import sys
from login import Ui_Dialog


class Window(QWidget, Ui_Dialog):
    def __init__(self, tittle="登录界面", size=(500, 500)):
        super().__init__()
        self.setWindowTitle(tittle)
        assert len(size) == 2
        self.resize(size[0], size[1])
        self.setup_ui()

    def setup_ui(self):
        self.setupUi(self)

    def check_login(self):
        print("csdcscscdsc")


def main():
    # 1\创建一个应用程序对象，传入系统的arg参数
    app = QApplication(sys.argv)

    # 2\控件的操作-创建控件，设置控件（大小、位置、设置）、时间的处理
    # 2-1 创建控件（控件是一个容器，可以去包含其他控件）
    window = Window()

    # 2-3 展示控件
    window.show()

    # 3、应用程序执行，进入到消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

