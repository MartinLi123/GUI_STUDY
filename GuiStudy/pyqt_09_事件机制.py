from PyQt5.Qt import *
import sys


class App(QApplication):
    def notify(self, reciver, evt):
        # print("QObject--- ", reciver)
        if reciver.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
        #  if type(reciver) is QPushButton:
            print(reciver, evt)
        return super().notify(reciver, evt)


def main():

    def slot_fuc():
        print("按钮被点击了")

    # 1\创建一个应用程序对象，传入系统的arg参数
    app = App(sys.argv)

    # 2\控件的操作-创建控件，设置控件（大小、位置、设置）、时间的处理
    # 2-1 创建控件（控件是一个容器，可以去包含其他控件）
    window = QWidget()

    btn = QPushButton(window)
    btn.setText("按键")
    btn.setStyleSheet("color:red")
    btn.move(200, 200)

    btn.pressed.connect(slot_fuc)

    # 2-3 展示控件
    window.show()

    # 3、应用程序执行，进入到消息循环
    sys.exit(app.exec_())


class Window(QWidget):
    def __init__(self, tittle="WINDOW", size=(500, 500)):
        super().__init__()
        self.setWindowTitle(tittle)
        assert len(size) == 2
        self.resize(size[0], size[1])
        self.setup_ui()

    def setup_ui(self):
        pass


if __name__ == '__main__':
    main()
