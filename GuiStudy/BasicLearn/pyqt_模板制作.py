from PyQt5.Qt import *
import sys


def main():
    # with open("QObject.qss","r") as f:
    #     style = f.read()
    # print(style)
    # qApp.setStyleSheet(style)   # 全局模式设置了q label 的字体颜色等

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
    def __init__(self, tittle="yahoo!", size=(500, 500)):
        super().__init__()
        self.setWindowTitle(tittle)
        assert len(size) == 2
        self.resize(size[0], size[1])
        self.setup_ui()

    def setup_ui(self):
        # self.inherit_sequence()
        # self.show_font_style_setting()
        self.show_memory_management()

    def show_font_style_setting(self):
        # 注意-只有进行了 QWidget.__init__() 才可以使用qApp这个全局变量进行设置
        with open("QObject.qss", "r") as f:
            style = f.read()
        print(style)
        qApp.setStyleSheet(style)  # 全局模式设置了q label 的字体颜色等

        label0 = QLabel(self)
        label0.setText("yahoo！")
        label0.setObjectName("notice")
        # label0.setStyleSheet("font-size:50px;color:green;")
        label0.move(200, 200)

        label = QLabel(self)
        label.setObjectName("notice")
        label.setProperty("notice_level", "normal")
        label.setText("yigeiwoligiaogiao!")
        # label.setStyleSheet("font-size:20px;color:red;")

    def show_inherit_sequence(self):
        mro = QObject.mro()
        for seq in mro:
            print(seq)

    def show_memory_management(self):
        obj1, obj2 = QObject(), QObject()
        obj2.setParent(obj1)
        self.Obj1 = obj1

        obj2.destroyed.connect(lambda : print("obj2 被释放了"))
        obj1.destroyed.connect(lambda : print("obj1 被释放了"))

        del self.Obj1


if __name__ == '__main__':
    main()
