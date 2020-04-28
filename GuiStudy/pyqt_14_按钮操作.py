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
    def __init__(self, tittle="按钮操作示例", size=(500, 500)):
        super().__init__()
        self.setWindowTitle(tittle)
        assert len(size) == 2
        self.resize(size[0], size[1])
        self.set_菜单的设置()

        exitAct = QAction(self)
        exitAct.setShortcut('Alt+q')
        exitAct.triggered.connect(qApp.quit)

    def setup_ui(self):
        btn1 = QPushButton("按钮1", self)
        btn1.setGeometry(100, 00, 300, 100)
        qsize = QSize(50, 50)
        icon1 = QIcon("icon.png")
        btn1.setIcon(icon1)

    def set_长按自动重复按钮(self):

        # -----------------长按重复触发按下对应的动作---------------------
        btn1 = QPushButton("按钮1", self)
        btn1.setGeometry(100, 50, 100, 30)
        qsize = QSize(50, 50)
        icon1 = QIcon("icon.png")
        btn1.setIcon(icon1)
        btn1.clicked.connect(lambda: print("!!!"))
        #  设置按下不松则重复发送
        btn1.setAutoRepeat(True)
        #  设置按下不松多少秒之后才开始触发重复操作
        btn1.setAutoRepeatDelay(3000)
        #  设置重复发送槽函数的时间间隔
        # -----------------长按重复触发按下对应的动作---------------------

    def set_按钮状态(self):
        btn1 = QPushButton("按钮1", self)
        btn1.setGeometry(0, 0, 100, 30)
        qsize = QSize(50, 50)
        icon1 = QIcon("icon.png")
        btn1.setIcon(icon1)
        btn1.clicked.connect(lambda: print("!!!"))

        radio_btn = QRadioButton(self)
        radio_btn.setText("这是一个radio button")
        radio_btn.move(100, 100)

        checkbox = QCheckBox(self)
        checkbox.setText("这是个check box")
        checkbox.move(100, 200)
        #  设置按下的样式
        btn1.setStyleSheet("QPushButton:pressed {background-color: red}")

        # -----------------设置三种按钮都为按下状态---------------------begain
        btn1.setDown(True)
        radio_btn.setDown(True)
        checkbox.setDown(True)
        # -----------------设置三种按钮都为按下状态---------------------end

        # -----------------查看按钮能否被选中---------------------begain
        print(btn1.isCheckable())  # 可通过setCheckable（）使其可被选中
        print(radio_btn.isCheckable())
        print(checkbox.isCheckable())
        # -----------------查看按钮能否被选中---------------------end

    def set_按钮排他性(self):
        # 只有拥有相同的父类时排他性才有效， 不同的父控件的按钮不具有排他性
        # -----------------设置按钮的排他性---------------------begain
        for i in range(3):
            # btn = QPushButton(self)
            btn = QRadioButton(self)

            btn.setText("BTN"+str(i))
            btn.move(50, i*50)
            # btn.setCheckable(True)
            # btn.setAutoExclusive(True)
            print(btn.isCheckable())
            print(btn.autoExclusive())
        # -----------------设置按钮的排他性---------------------end

    def set_模拟用户点击事件(self):
        btn = QPushButton("BTN", self)
        btn.setGeometry(100, 100, 100, 50)
        btn.clicked.connect(lambda: print("!!!!!!!"))
        btn.click()  # 模仿用户的一次点击

        btn2 = QPushButton("BTN2", self)
        btn2.setGeometry(0, 0, 100, 50)
        def test():
            btn.animateClick(2000)  # btn 会显示按住不松的动画2000ms
        btn2.clicked.connect(test)

    def set_按钮的有效点击区域(self):
        class BTN(QPushButton):
            # def hitButton(self, point):
            #     print(point)
            #     return True
            pass

        btn1 = BTN("按钮", self)
        btn1.setGeometry(100, 100, 80, 50)
        btn1.setCheckable(True)
        btn1.clicked.connect(lambda value: print(" clicked", value))
        btn1.released.connect(lambda: print(" released"))
        btn1.pressed.connect(lambda : print(" presssed "))
        btn1.toggled.connect(lambda : print(" 状态发生了反转 "))

    def set_菜单的设置(self):
        btn1 = QPushButton("按钮", self)
        btn1.setIcon(QIcon("icon_imgs/scanner.png"))
        btn1.setGeometry(100, 100, 200, 100)
        btn1.setFlat(True)
        # btn1.setCheckable(True)

        menu = QMenu()





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


        btn1.setMenu(menu)
        btn1.showMenu()


if __name__ == '__main__':
    main()
