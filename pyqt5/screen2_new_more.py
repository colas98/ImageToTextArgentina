self.bt_menu.clicked.connect(self.mover_menu)


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