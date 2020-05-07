from PyQt5.Qt import *
import sys


def main():

    windows = QWidget()
    windows.setWindowIconText("第一个窗口程序")
    windows.resize(500, 500)
    windows.move(400, 200)

    label = QLabel(windows)
    label.setText("Hello world!")
    label.move(200, 200)

    windows.show()

    app = QApplication(sys.argv)
    # app.exec_()为程序的退出码，同时告诉系统需要退出，保证程序不会立即退出
    # 并且进入消息循环（无限循环）
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()