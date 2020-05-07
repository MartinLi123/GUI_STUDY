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
    def __init__(self, tittle="信号与槽示例", size=(500, 500)):
        super().__init__()
        self.setWindowTitle(tittle)
        assert len(size) == 2
        self.resize(size[0], size[1])
        self.setup_ui()

    def setup_ui(self):
        # self.show_object_signal_operation()
        # self.show_sigal_block()
        # self.show_HowManySlotsOneSignalConnected()
        # self.show_Qobject_type_determination()
        # self.show_set_labels_by_inherit()
        self.show_object_delete()


    def show_object_signal_operation(self):
        def destroy_slot(obj):
            print("销毁了对象---", obj)
        def obj_name_changed(new_name):
            print("对象的名称变化了,新的名称为---", new_name)

        # obj1.destroyed 示例
        obj1 = QObject()
        # 局部变量 obj1 在函数执行之后就会被销毁，则触发信号
        obj1.destroyed.connect(destroy_slot) # 只要写函数名无需传参， 会自动把对象的引用传入

        # obj1.objectNameChanged 示例
        self.obj1 = QObject()
        self.obj1.setObjectName("对象1")
        # 对象名变化之后会触发， 会将新的变量名传入
        self.obj1.objectNameChanged.connect(obj_name_changed)
        print("*"*100)
        self.obj1.setObjectName("对象111")

    def show_sigal_block(self):
        def obj_name_changed(new_name):
            print("对象的名称变化了,新的名称为---", new_name)

        self.obj1 = QObject()
        self.obj1.setObjectName("对象1")
        # 对象名变化之后会触发， 会将新的变量名传入
        self.obj1.objectNameChanged.connect(obj_name_changed)

        # 设置阻断槽连接
        self.obj1.blockSignals(True)
        self.obj1.setObjectName("对象2")
        print("是否阻隔了信号---", self.obj1.signalsBlocked())
        self.obj1.blockSignals(False)
        print("是否阻隔了信号---", self.obj1.signalsBlocked())
        self.obj1.setObjectName("对象3")

    def show_HowManySlotsOneSignalConnected(self):
        def obj_name_changed1(new_name):
            print("对象的名称变化了,新的名称为---", new_name)

        def obj_name_changed2(new_name):
            print("对象的名称变化了,新的名称为---", new_name)

        self.obj1 = QObject()
        self.obj1.setObjectName("对象1")
        self.obj1.objectNameChanged.connect(obj_name_changed1)
        self.obj1.objectNameChanged.connect(obj_name_changed2)

        slot_num = self.obj1.receivers(self.obj1.objectNameChanged)
        print( slot_num , "个 slot" "PYQT signal" "self.obj1.receivers "  "connected")

    def show_Qobject_type_determination(self):
        pass
        obj1 = QObject()

        obj2 = QPushButton()
        obj3 = QLabel()
        obj_list = [obj1, obj2, obj3]
        for obj in obj_list:
            print(obj.inherits("QWidget"))  # 直接或者间接继承

    def show_set_labels_by_inherit(self):
        label1 = QLabel(self)
        label1.setText("label1")
        label1.move(100, 100)

        label2 = QLabel(self)
        label2.setText("label2")
        label2.move(200, 200)

        label3 = QLabel(self)
        label3.setText("label3")
        label3.move(300,300)

        btn = QPushButton(self)
        btn.setText("BUTTON")

        # btn.isWidgetType()

        for obj in self.children():
            # print(obj)
            # if obj.isWidgetType()
            if obj.inherits("QLabel"):  # 传入一个字符串
                print(obj, "   yes")
                obj.setStyleSheet("color:red")

    def show_object_delete(self):
        def delete_print(obj):
            print(obj.objectName(), "被删除了!")

        obj1 = QObject(self)
        obj1.setObjectName("obj1")
        obj2 = QObject()
        obj2.setObjectName("obj2")
        obj3 = QObject()
        obj3.setObjectName("obj3")

        obj2.setParent(obj1)
        obj3.setParent(obj2)

        obj1.destroyed.connect(delete_print)
        obj2.destroyed.connect(delete_print)
        obj3.destroyed.connect(delete_print)

        obj2.deleteLater()
        print(obj1.children())




if __name__ == '__main__':
    main()
