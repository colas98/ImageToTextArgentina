
from PyQt5.QtCore import QPropertyAnimation

self.bt_menu.clicked.connect(self.mover_menu)


# debajo de self.exit
self.bt_path.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
self.bt_general.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
self.bt_advanced.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))

def mover_menu(self):
    if True:
        width = self.frame_lateral.width()
        normal = 0
        if width == 0:
            extender = 200
        else:
            extender = normal
        self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()


self.exit.clicked.connect(lambda:self.closescr(Form))


def closescr(self, Form):
    Form.hide()

### sreen_1

from screen2_new import Ui_Form



def secondscr(self):
    # Code the 2nd screen here
    self.Form = QtWidgets.QWidget()
    self.ui = Ui_Form()
    self.ui.setupUi(self.Form)
    self.Form.show()

self.secondbtn.clicked.connect(self.secondscr)

MainWindow.resize(320, 140)
