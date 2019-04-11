import matplotlib.pyplot as plt
import math
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import sys
from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d
from PyQt4.uic import loadUiType
import serial
import math

#recebendo a janela grafica
Ui_MainWindow, QMainWindow = loadUiType('interface.ui')

#classe da janela grafica
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Atlas")
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.x = []
        self.y = []
        self.z = []
        self.ser = serial.Serial("COM3", 9600)

        self.graphLayout.addWidget(self.toolbar)
        self.graphLayout.addWidget(self.canvas)
        self.plot()

        self.iniciarButton.clicked.connect(self.iniciarbutton)
        self.pausarButton.clicked.connect(self.pausarbutton)
        self.pararButton.clicked.connect(self.pararbutton)

    def iniciarbutton(self):
        print("INCIAR")

    def pausarbutton(self):
        print("PAUSAR")

    def pararbutton(self):
        print("PARAR")

    def plot(self):
        self.ax = self.figure.add_subplot(111, projection = '3d')
        for i in range(20):
            self.ler_serial()
        self.canvas.draw()


    def ler_serial(self):
        rho = 57.2958 * (float(self.ser.readline()))  # Recebe a String enviada pelo Arduino
        theta = 57.2958 * (float(self.ser.readline()))
        phi = 57.2958 * (float(self.ser.readline()))

        self.x.append(rho * (math.sin(phi) * math.cos(theta)))
        self.y.append(rho * (math.sin(phi) * math.sin(theta)))
        self.z.append(rho * (math.cos(phi)))

        self.ax.scatter(self.x, self.y, self.z, zdir='z', s=5, c=None, depthshade=True)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())



