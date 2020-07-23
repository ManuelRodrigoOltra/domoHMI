from PySide2.QtWidgets import QApplication


def hmi_dom_init():
    print ("configuramos el interfaz")

def hmi_dom_launch():
    app = QApplication.instance()
    return app

def hmi_dom_exec(app):
    try:
        app.exec_()
    except Exception as err:
        print(err)



if __name__ == '__main__' :
    hmi_dom_init()
    hmi_dom_launch()
