from PySide2.QtWidgets import  QVBoxLayout, QPushButton, \
    QLabel, QMainWindow


class MainHMIWindow(QMainWindow):

    def __init__(self):
        super().__init__()


        self.label_bot_luz_1 = QLabel()
        self.buttonComedor = QPushButton()

        print("ejecuta init")
        self.init_ui()


    def init_ui(self):
        self.label_bot_luz_1.setText("Luz comedor")
        self.buttonComedor.setText("On")
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        print("pasa")
        self.layout().addWidget(self.label_bot_luz_1)

        # luz_comedor = QWidget(objetcName = "Luz comedor")
        # luz_comedor.setLayout(QVBoxLayout)
        # luz_comedor.layout().setContentsMargins(0,0,0,0)
        # luz_comedor.layout().setSpacing(0)
        # luz_comedor.layout().addWidget(self.label_bot_luz_1)
        # luz_comedor.layout().addWidget(self.buttonComedor)
        #
        #
        # self.label_bot_luz_2 = QLabel()
        # self.label_bot_luz_2.setText("Luz cocina")
        # self.buttonCocina = QPushButton()
        # self.buttonCocina.setText(self, "On")
        # luz_cocina = QWidget(objetcName="Luz cocina")
        # luz_cocina.setLayout(QVBoxLayout)
        # luz_cocina.layout().setContentsMargins(0, 0, 0, 0)
        # luz_cocina.layout().setSpacing(0)
        # luz_cocina.layout().addWidget(self.label_bot_luz_2)
        # luz_cocina.layout().addWidget(self.buttonCocina)
        #
        #
        #
        # luz_group = QWidget(objectName = "grupo de luces")
        # luz_group.setLayout(QHBoxLayout)
        # luz_group.layout().addWidget(luz_comedor)
        # luz_group.layout().addWidget(luz_cocina)
        #
        # self.layout().addWidget(luz_group)

        self.setCentralWidget(self.layout())

        #self.layout().addWidget(self.buttonTest)



