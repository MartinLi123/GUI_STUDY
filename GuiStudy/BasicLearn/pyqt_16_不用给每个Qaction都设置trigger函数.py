from PyQt5.Qt import *
import sys
import os


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
    def __init__(self, tittle="QCommandLinkButton使用", size=(500, 500)):
        super().__init__()
        self.setWindowTitle(tittle)
        assert len(size) == 2
        self.resize(size[0], size[1])
        self.set_ToolButtonWithMenu()

    def set_ToolButtonWithMenu(self):
        btn = QToolButton( self)
        self.set_menu(btn)
        # Qpushbutton 没有 triggered 方法
        # 当 ToolButton 内的action被触发， 获取其内部的data作为标识符， 再同一个函数内通过判断data来分发操作
        btn.triggered.connect(lambda qaction: print("！！！！", qaction, qaction.data()))

    def set_menu(self, parent, qpoint=QPoint(0, 0)):
        menu = QMenu(parent)

        # menu.setTitle("操作")
        # 不设定父类则在函数执行完毕后会销毁
        new_action = QAction(QIcon("icon_imgs/scanner.png"), "操作", menu)
        new_action.setData(1)

        new_action.triggered.connect(lambda: print("new_action 被触发"))

        new_action2 = QAction(QIcon("icon_imgs/scanner.png"), "窗口", menu)
        new_action2.triggered.connect(lambda: print("new_action2 被触发"))

        new_action3 = QAction(QIcon("icon_imgs/scanner.png"), "设置", menu)
        new_action3.triggered.connect(lambda: print("new_action3 被触发"))

        sep_menu1 = QMenu("文件", menu)
        new_action4 = QAction(QIcon("icon_imgs/scanner.png"), "保存", sep_menu1)
        new_action4.triggered.connect(lambda: print("new_action4 被触发"))

        new_action5 = QAction(QIcon("icon_imgs/scanner.png"), "另存为", sep_menu1)
        new_action5.triggered.connect(lambda: print("new_action5 被触发"))

        menu.addMenu(sep_menu1)
        sep_menu1.addAction(new_action4)
        sep_menu1.addAction(new_action5)
        menu.addAction(new_action)
        menu.addAction(new_action2)
        menu.addSeparator()
        menu.addAction(new_action3)

        parent.setMenu(menu)
        # 此时传入的是相对于app窗口的坐标而不是相对于屏幕 global 的坐标， 需要转化
        # glb_point = self.mapToGlobal(qpoint)
        # menu.exec_(glb_point)
        # btn1.showMenu()


if __name__ == '__main__':
    main()
