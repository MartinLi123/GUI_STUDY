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
    def __init__(self, tittle="信号与槽实现点击后回应", size=(500, 500)):
        super().__init__()
        self.setWindowTitle(tittle)
        assert len(size) == 2
        self.resize(size[0], size[1])
        self.setup_ui()

    def setup_ui(self):
        self.click_then_react()

    def click_then_react(self):
        def clicked_slot():
            qlabel = QLabel(self)
            qlabel.setText("我们遇到什么困难都不要怕！\n微笑着面对它！")
            qlabel.move(200, 200)
            qlabel.setStyleSheet("color:red")
            qlabel.show()

        btn = QPushButton(self) # 作为主窗口的一个子类
        btn.setText("点我！")

        btn.clicked.connect(clicked_slot)


if __name__ == '__main__':
    main()
