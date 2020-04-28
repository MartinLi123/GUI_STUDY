from PyQt5.Qt import *
import sys


class MyObject(QObject):

    def timerEvent(self, QTimerEvent):
        print(QTimerEvent, "1s过去了！")


class MyQlabel(QLabel):
    def __init__(self, begain_num, parent_obj=None):
        super().__init__()
        if parent_obj is not None: self.setParent(parent_obj)
        self.current_num = begain_num
        self.setText(str(self.current_num))
        self.resize(100, 50)
        self.move(200, 200)
        self.timer_id = self.startTimer(1000)

    def timerEvent(self, *args, **kwargs):
        self.current_num = int(self.text())
        self.current_num -= 1
        self.setText(str(self.current_num))

        if self.current_num == 0:
            self.killTimer(self.timer_id)


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
    def __init__(self, tittle="定时器", size=(500, 500)):
        super().__init__()
        self.setWindowTitle(tittle)
        assert len(size) == 2
        self.resize(size[0], size[1])
        self.setup_ui2()

    def setup_ui(self):
        obj = MyObject(self)
        timer_id = obj.startTimer(1000)
        print("定时器id is ", timer_id)

        # obj.killTimer(timer_id)

    def setup_ui2(self):
        qlabel = MyQlabel(10, self)  # 重写qlabel中的time event方法来执行，每次定时器变化后要执行的操作


if __name__ == '__main__':
    main()
