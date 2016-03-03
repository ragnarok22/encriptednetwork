__version__ = "1.0"
__author__ = "Ragnarok"

from PyQt5.QtWidgets import QMainWindow, QWidget, QMenuBar, QStatusBar, QMenu, QAction, qApp, QGridLayout, QLabel, \
    QLineEdit, QHBoxLayout, QPushButton, QMessageBox, QApplication
from PyQt5.QtGui import QIcon
import sys
import platform
from algorithm.codification import ShannonFano as shannon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.icon = QIcon("sources/images/logo.png")
        self.setWindowIcon(self.icon)
        self.setWindowTitle("Encoding Algorithms Network")
        self.setMinimumSize(640, 480)

        self.max_messages = 20

        self.create_menu_components()

    def create_menu_components(self):
        self.menubar = QMenuBar()
        self.statusbar = QStatusBar()

        self.menuFile = QMenu("&File")

        self.new_file_action = QAction("&New File", self)
        self.new_file_action.setStatusTip("Create a new encoding project")
        self.new_file_action.setShortcut("Ctrl+N")
        self.menuFile.addAction(self.new_file_action)

        self.open_file_action = QAction("&Open File", self)
        self.open_file_action.setStatusTip("Open a encoding network file")
        self.open_file_action.setShortcut("Ctrl+O")
        self.menuFile.addAction(self.open_file_action)

        self.save_action = QAction("&Save", self)
        self.save_action.setShortcut("Ctrl+S")
        self.menuFile.addAction(self.save_action)

        self.save_as_action = QAction("Save As", self)
        self.menuFile.addAction(self.save_as_action)

        self.quit_action = QAction("&Quit", self)
        self.quit_action.setStatusTip("Quit the program")
        self.quit_action.setShortcut("Ctrl+Q")
        self.quit_action.triggered.connect(qApp.exit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.quit_action)

        self.menuHelp = QMenu("&Help")

        self.about_shannon_action = QAction("About Shannon-Fano Algorithm", self)
        self.about_shannon_action.setStatusTip("Show information about Shannon-Fano algorithms")
        self.about_shannon_action.triggered.connect(self.about_shannonfano_function)
        self.menuHelp.addAction(self.about_shannon_action)

        self.about_action = QAction("&About Encoding Network", self)
        self.about_action.setStatusTip("Show information about Encoding Network")
        self.about_action.setShortcut("F1")
        self.about_action.triggered.connect(self.about_application_function)
        self.menuHelp.addAction(self.about_action)

        self.menubar.addMenu(self.menuFile)
        self.menubar.addMenu(self.menuHelp)

        self.setMenuBar(self.menubar)
        self.setStatusBar(self.statusbar)

        # cuerpo de la ventana principal
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        self.central_layout = QGridLayout()
        self.central_layout.setSpacing(10)

        # self.table = QTableWidget()
        # self.table.setRowCount(1)
        # self.table.setColumnCount(2)
        # self.table.setHorizontalHeaderLabels(["probablilidad", "encriptacion"])
        # self.table.resizeColumnsToContents()
        # self.table.verticalHeader().hide()
        # self.central_layout.addWidget(self.table)

        self.central_layout.addWidget(QLabel("Probabilities"), 1, 0)
        self.central_layout.addWidget(QLabel("Encoding Text"), 1, 1)

        self.probablities_array = []

        for i in range(self.max_messages):
            self.probablities_array.append(QLineEdit())
            self.central_layout.addWidget(self.probablities_array[i], i + 2, 0)

        # button layout
        button_layout = QHBoxLayout()

        calculate_btn = QPushButton("Calculate")
        calculate_btn.clicked.connect(self.calculate_probabilities_function)

        exit_btn = QPushButton("Quit")
        exit_btn.clicked.connect(qApp.exit)

        add_column_btn = QPushButton("Add Probabilities")
        add_column_btn.clicked.connect(self.add_column_function)

        button_layout.addWidget(calculate_btn)
        button_layout.addWidget(add_column_btn)
        button_layout.addWidget(exit_btn)

        self.central_layout.addLayout(button_layout, 30, 30)
        self.mainWidget.setLayout(self.central_layout)

        self.set_styles()

    def add_column_function(self):
        QMessageBox.warning(QWidget(), "Not Implemented",
                            '''
                            <p><b>Not Implemented Yet</b></p>
                            <p>You have a beta version, this function is not implemented yet. Please
                            visit <a href="http://www.encryptednetwork.com">our page</a> to download the latest version</p>
                            '''
                            )

    def calculate_probabilities_function(self):
        print("calculando shannon fano")
        if self.probablities_array[0].text() == "":
            QMessageBox.information(QWidget(), "Error in Data", "you must to give unless one number")
            return
        probabilities = []
        self.encoding_array = []
        for i in self.probablities_array:
            try:
                probabilities.append(float(i.text()))
            except ValueError:
                break

        sh = shannon(probabilities).get_message_encoded()

        for i in range(len(probabilities)):
            self.encoding_array.append(QLabel(sh[i]))
            self.central_layout.addWidget(self.encoding_array[i], i + 2, 1)

    def about_application_function(self):
        about = QMessageBox()
        about.setWindowIcon(self.icon)
        QMessageBox.about(about, "About Encripted Network",
                          '''
                          <body >
                          <p><b>Encrypted Network</b></p>
                          <p><b>Version:</b> {0}</p>
                          <p><b>Author:</b> {1}</p>
                          <p>University Informatics student.</p>
                          <p>This application using Shannon-Fano algorithm to encoding messages given the
                          probabilities for each text
                          </p>
                          <p>This version run on {2}</p>
                          <p><footer>&copy; 2015 - 2016 Encrypted Network. All rights reserved.</footer></p>
                          </body>
                          '''.format(__version__, __author__, platform.system())
                          )

    def about_shannonfano_function(self):
        about = "In the field of data compression, <b>Shannon–Fano coding</b> is a technique for constructing a prefix code" \
                " based on a set of symbols and their probabilities (estimated or measured). It is suboptimal in the " \
                "sense that it does not achieve the lowest possible expected code word length like Huffman coding;" \
                " however unlike Huffman coding, it does guarantee that all code word lengths are within one bit of " \
                "their theoretical ideal − logP(x). The technique was proposed in Claude Elwood Shannon's A " \
                "Mathematical Theory of Communication, his 1948 article introducing the field of information theory." \
                " The method was attributed to Robert Fano, who later published it as a technical report.[1]" \
                " Shannon–Fano coding should not be confused with Shannon coding, the coding method used to prove" \
                " Shannon's noiseless coding theorem, or with Shannon-Fano-Elias coding (also known as Elias coding)," \
                " the precursor to arithmetic coding."
        sh = QMessageBox()
        sh.setWindowIcon(QIcon("sources/images/shannon.png"))
        QMessageBox.about(sh, "About Shannon-Fano algorithms", about)

    def set_styles(self):
        style = open("sources/styles.css", "r")
        self.setStyleSheet(style.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
