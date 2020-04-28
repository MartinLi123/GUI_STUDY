import sys
from PyQt5.Qt import *


class MainWindowExample(QMainWindow):

    def __init__(self):
        super().__init__()
        # self.InitUI()
        # self.setui_显示简单的菜单()
        self.set_菜单添加分支()
        # self.show_inputBox()

    def InitUI(self):
        self.statusBar().showMessage('准备就绪')
        self.setGeometry(700, 400, 400, 300)
        self.setWindowTitle('example---状态栏')
        self.show()

    def setui_显示简单的菜单(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--简单的菜单')

        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        # “&”这个符号，当我们按住“Alt+F”的时候就能快速打开文件这个菜单
        fileMenu = menubar.addMenu('文件(&F)')
        editmenu = menubar.addMenu("编辑(&E)")
        viewmenu = menubar.addMenu("视图(&V)")
        fileMenu.addAction(exitAct)

        self.show()

    def set_菜单添加分支(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--子菜单')

        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        saveMenu = QMenu('保存方式(&S)', self)
        saveAct = QAction(QIcon('save.png'), '保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        saveasAct = QAction(QIcon('saveas.png'), '另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        newAct = QAction(QIcon('new.png'), '新建(&N)', self)
        newAct.setShortcut('Ctrl+N')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()  # ???
        fileMenu.addAction(exitAct)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindowExample()
    sys.exit(app.exec_())

