from time import time

from PySide2.QtCore import QThreadPool
from PySide2.QtWidgets import QMainWindow
from thread_custom import Worker


class MainHMIWindow(QMainWindow):

    def __init__(self, widget):

        super().__init__()

        self.threadpool = QThreadPool()
        self.init_ui()
        self.setCentralWidget(widget)
        self.start_time = time()

        self.cpuUsage = []
        self.countTime =[]

        self.widget=widget

        worker = Worker(self.widget.tab_consum.init_logica)  # Any other args, kwargs are passed to the run function
        worker.signals.cpu_usage.connect(self.refresh)

        # Execute
        self.threadpool.start(worker)

    def refresh(self, n):
        self.widget.tab_consum.refresh(n)



        # # Pass the function to execute
        # worker = Worker(self.init_logica)  # Any other args, kwargs are passed to the run function
        # # Execute
        # self.threadpool.start(worker)


    def init_ui(self):
        self.flag = True
        pass

    def init_logica(self):
        pass
        # while self.flag:
        #     self.qseries = QtCharts.QLineSeries()
        #     self.qseries.name()
        #     sleep(2)
        #     time_process = self.countTime.append(time() - self.start_time)
        #     procesor_usage = self.cpuUsage.append(psutil.cpu_percent())
        #
        #     self.qseries.append(time_process, procesor_usage)


        pass

    def create_layout_luces_btn(self):
        pass


