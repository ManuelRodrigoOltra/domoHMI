
from time import time

import psutil
from PySide2.QtCore import Qt, QTimer, QThreadPool, Slot
from PySide2.QtWidgets import QVBoxLayout, QPushButton, \
    QWidget, QLabel, QHBoxLayout, QTabWidget, QGridLayout
from pyqtgraph import GraphicsLayoutWidget, PlotWidget, setConfigOptions, mkPen


class UiLightWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.label_btn_l1 = QLabel("Salon")
        self.btn_salon = QPushButton("ON")

        self.label_btn_l2 = QLabel("Cocina")
        self.btn_cocina = QPushButton("ON")

        self.init_ui()
        self.init_logic()

    def init_ui(self):

        btn_group_grid = QGridLayout()
        btn_group_grid.addWidget(self.label_btn_l1, 0, 0)
        btn_group_grid.addWidget(self.btn_salon, 1, 0)

        btn_group_grid.addWidget(self.label_btn_l2, 0, 1)
        btn_group_grid.addWidget(self.btn_cocina, 1, 1)

        self.setLayout(btn_group_grid)
        self.layout().setAlignment(Qt.AlignCenter)

    def init_logic(self):
        self.btn_cocina.clicked.connect(self.fun_luces_cocina)
        self.btn_salon.clicked.connect(self.fun_luces_salon)

    def fun_luces_cocina(self):

        print("luz cocina on/off")
        if self.btn_cocina.text() == "ON":
            self.btn_cocina.setText("OFF")
        else:
            self.btn_cocina.setText("ON")

    def fun_luces_salon(self):
        print("luz salón on/off")
        if self.btn_salon.text() == "ON":
            self.btn_salon.setText("OFF")
        else:
            self.btn_salon.setText("ON")


class UiVisualConsumos(GraphicsLayoutWidget):

    def __init__(self):

        super().__init__()

        self.threadpool = QThreadPool()

        self.cpuUsage = []
        self.countTime =[]

        self.start_time = time()

        self.timer = QTimer()

        # ---------------------------------------------------------------------------
        self.plot_view = PlotWidget()
        self.plot_view.plotItem.setTitle("Processor percent usage")
        setConfigOptions(antialias=False)
        # ---------------------------------------------------------------------------

        self.hour = []
        self.temperature = []

        # ---------------------------------------------------------------------------
        self.plot_view.plot(self.hour, self.temperature, pen=mkPen(cosmetic=True, width=40.0, color='r'))
        self.plot_view.setLabel('left', "Processor usage", units='%')
        # ---------------------------------------------------------------------------

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.plot_view)
        self.setLayout(self.main_layout)

    @Slot()
    def refresh(self, n):
        self.hour.append(n[0])
        self.temperature.append(n[1])
        self.plot_view.plot(self.hour, self.temperature, pen='r')

    @Slot()
    def init_logica(self, cpu_usage_callback):
        cpu_usage_callback.emit([float(time() - self.start_time),float(psutil.cpu_percent())])


class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.tab_light = UiLightWindow()
        self.tab_consum = UiVisualConsumos()
        self.main_layout = QHBoxLayout()
        # size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.tabs = QTabWidget()


        self.tabs.addTab(self.tab_light, 'Luces')
        self.tabs.addTab(self.tab_consum, 'Consumo')

        self.main_layout.addWidget(self.tabs)
        self.setLayout(self.main_layout)
        
        self.main_layout.setContentsMargins(10,10,10,10)






