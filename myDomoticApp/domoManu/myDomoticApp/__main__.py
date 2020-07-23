import sys

from PySide2.QtWidgets import QApplication
from ui_general import MainHMIWindow
from ui_windows import Widget


def hmi_dom_init():
    print ("configuramos el interfaz")
    pass

def hmi_dom_launch():

    app = QApplication(sys.argv)

    widget = Widget()
    w = MainHMIWindow(widget)
    w.setWindowTitle("Domótica")

    w.showMaximized()
    hmi_dom_exec(app)


def hmi_dom_exec(app):
    try:
        app.exec_()
    except Exception as err:
        print(err)



if __name__ == '__main__' :
    hmi_dom_init()
    hmi_dom_launch()

