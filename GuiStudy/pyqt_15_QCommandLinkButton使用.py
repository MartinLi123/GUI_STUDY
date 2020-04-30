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
        self.set_QToolButton里设置箭头图标()

    def set_QCommandLinkButton(self):  # 命令连接按钮
        # 命令连接按钮 的使用
        btn = QCommandLinkButton("标题", "描述", self)
        btn.setText("标题2")
        btn.setDescription("描述2")

    def set_QToolButton(self):
        # 提供一个快速访问按钮
        # 通常在窗口栏下面
        btn = QToolButton(self)  # 默认文本和图标都存在时，只显示图标
        # 可以通过 ToolButtonStyle 来设置显示不显示文本
        # btn = QPushButton(self)
        btn.setText("工具")
        btn.setIcon(QIcon("icon_imgs/scanner.png"))
        btn.setIconSize(QSize(50, 50))
        print(os.path.exists("icon_imgs/scanner.png"))
        btn.setToolTip("这是一个工具按钮")  # 鼠标悬停则显示tip
        # btn.setflat  # QToolButton 继承自QAbstractButton 而只有 QushButton有扁平化操作
        btn.setAutoRaise(True)

    def set_QToolButton里设置箭头图标(self):
        # 箭头也作为一个图标， 优先级比用户设置的图标优先级高
        btn = QToolButton(self)  # 默认文本和图标都存在时，只显示图标
        btn.setArrowType(Qt.UpArrow)
        # Qpushbutton 是点击触发
        # QToolButton 需要设置菜单的触发方式， 默认是长按触发
        self.set_menu(btn)

    def set_menu(self, parent, qpoint=QPoint(0, 0)):

        menu = QMenu(parent)

        # menu.setTitle("操作")
        # 不设定父类则在函数执行完毕后会销毁
        new_action = QAction(QIcon("icon_imgs/scanner.png"), "操作", menu)
        new_action2 = QAction(QIcon("icon_imgs/scanner.png"), "窗口", menu)
        new_action3 = QAction(QIcon("icon_imgs/scanner.png"), "设置", menu)

        sep_menu1 = QMenu("文件", menu)
        new_action4 = QAction(QIcon("icon_imgs/scanner.png"), "保存", sep_menu1)
        new_action5 = QAction(QIcon("icon_imgs/scanner.png"), "另存为", sep_menu1)

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
