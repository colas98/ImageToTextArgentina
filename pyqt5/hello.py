import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle("Hello World!")

        # Set Vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a Label
        my_label = qtw.QLabel("Pick Something From The List Below")
        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)


        # Create an entry box
        # my_entry = qtw.QLineEdit()
        # my_entry.setObjectName("name_field")
        # my_entry.setText("")
        # self.layout().addWidget(my_entry)

        # Create a Combo box
        my_combo = qtw.QComboBox(self,
                                 editable=True,
                                 insertPolicy=qtw.QComboBox.InsertAtBottom)

        # Add Items to the Combo Box
        my_combo.addItem("Pepperoni", "Something")
        my_combo.addItem("Cheese", qtw.QWidget)
        my_combo.addItem("Peppers", 2)
        my_combo.addItems(["One" "Two", "Three"])
        my_combo.insertItem(2, "Third Thing")




        # Create a button
        my_button = qtw.QPushButton("Press me!",
                                    clicked = lambda: press_it())
        self.layout().addWidget(my_button)


        self.show()

        # import main
        def press_it():
            # Set entry box
            # my_label.setText(f'Hello {my_entry.text()}!')
            # Clear entry box
            # my_entry.setText("")
            my_label.setText(f'You Picked {my_combo.currentText()}!')

            # book_path = 'C:/Users/Hp/OneDrive/Escritorio/libro_3.pdf'
            # main.print_pages(my_combo.currentText())
            # Put combobox on the screen
            self.layout().addWidget(my_combo)


app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()
