from PyQt5.Qt import *
import sys


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


class Window(QWidget):
    def __init__(self, tittle="QRadioButton", size=(500, 500)):
        super().__init__()
        self.setWindowTitle(tittle)
        assert len(size) == 2
        self.resize(size[0], size[1])
        self.set_设置部分单选按钮互斥()

    def setup_ui(self):
        choice1 = QRadioButton("male", self)
        choice1.setGeometry(0, 0, 50, 20)
        choice2 = QRadioButton("female", self)
        choice1.setGeometry(0, 30, 50, 20)

    def set_设置部分单选按钮互斥(self):
        #  方法1---设置两个父控件，一个父控件内的单选按钮是互斥的
        choice1 = QRadioButton("male", self)
        choice1.setGeometry(0, 0, 50, 20)
        choice2 = QRadioButton("female", self)
        choice1.setGeometry(0, 30, 50, 20)

        # 方法2---设置两个按钮组 ButtonGroup 按钮组内部的button是互斥的


if __name__ == '__main__':
    main()
