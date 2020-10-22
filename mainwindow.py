from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas import Particulas
from particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.particulas = Particulas()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))

    @Slot()
    def click_agregar(self):
        identificacion = int(self.ui.id_lineEdit.text())
        origenx = int(self.ui.origenx_lineEdit.text())
        origeny = int(self.ui.origeny_lineEdit.text())
        destinox = int(self.ui.destinoy_lineEdit.text())
        destinoy = int(self.ui.destinoy_lineEdit.text())
        velocidad = int(self.ui.velocidad_lineEdit.text())
        red = int(self.ui.red_lineEdit.text())
        green = int(self.ui.green_lineEdit.text())
        blue = int(self.ui.blue_lineEdit.text())

        particula = Particula(identificacion, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        self.particulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        identificacion = int(self.ui.id_lineEdit.text())
        origenx = int(self.ui.origenx_lineEdit.text())
        origeny = int(self.ui.origeny_lineEdit.text())
        destinox = int(self.ui.destinoy_lineEdit.text())
        destinoy = int(self.ui.destinoy_lineEdit.text())
        velocidad = int(self.ui.velocidad_lineEdit.text())
        red = int(self.ui.red_lineEdit.text())
        green = int(self.ui.green_lineEdit.text())
        blue = int(self.ui.blue_lineEdit.text())

        particula = Particula(identificacion, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        self.particulas.agregar_inicio(particula)
