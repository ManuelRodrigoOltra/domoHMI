from enum import Enum

from PySide2.QtCore import Qt


class TouchStatus(Enum):
    NONE = -1,
    PRESSED = 0,
    TAPING = 1,


class TouchBase:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.status = None
        self.last_click = None

        self.setAttribute(Qt.WA_AcceptTouchEvents, True)
        self.installEventFilter(self)
        self.grabGesture(Qt.PinchGesture)


    def eventFilter(self):

        return False

    def touch_press(self):
        self.status = TouchStatus.PRESSED

class TouchGraph()