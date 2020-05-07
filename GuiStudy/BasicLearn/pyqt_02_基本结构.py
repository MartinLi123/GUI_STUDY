from PyQt5.Qt import *
import sys

def main():
    # 1\创建一个应用程序对象，传入系统的arg参数
    app = QApplication(sys.argv)
    # 2\控件的操作-创建控件，设置控件（大小、位置、设置）、时间的处理
    # 2-1 创建控件（控件是一个容器，可以去包含其他控件）
    # 创建一个控件时如果没有父控件则把它当成一个顶层控件
    window = QWidget()
    window.setWindowTitle("GIAO")   # 只有顶层窗口可以设置setWindowTitle
    # window = QPushButton()
    # window = QLabel()
    # window.setText("giao!")

    # qlabel是一个和window平级别的主控件
    qlabel1 = QLabel()
    qlabel1.setWindowTitle("qlabel1")
    qlabel1.setText("yi gei wo li giaogiao!")
    qlabel1.show()

    # qlabel是window的子控件
    qlabel = QLabel(window)
    qlabel.setWindowTitle("giao")
    qlabel.setText("yi gei wo li giaogiao!")
    qlabel.show()

    # 2-2 设置控件
    # 2-3 展示控件
    # 刚创建好一个控件之后，前提是控件没有父控件
    window.show()

    # 3、应用程序执行，进入到消息循环
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
