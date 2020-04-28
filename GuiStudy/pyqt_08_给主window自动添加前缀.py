from PyQt5.Qt import *
import sys
import time

def main():
    # 1\创建一个应用程序对象，传入系统的arg参数
    app = QApplication(sys.argv)
    window = QWidget()

    def add_predfix(tittle):
        # global window
        print("window 标题改变成了---", tittle)
        window.blockSignals(True)
        window.setWindowTitle("加油---"+tittle)
        window.blockSignals(False)

    # 2\控件的操作-创建控件，设置控件（大小、位置、设置）、时间的处理
    # 2-1 创建控件（控件是一个容器，可以去包含其他控件）

    window.windowTitleChanged.connect(add_predfix)
    window.setWindowTitle("奥里给")
    window.show()
    time.sleep(1)
    window.setWindowTitle("okkk")

    # 2-3 展示控件
    window.show()

    # 3、应用程序执行，进入到消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()