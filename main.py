__version__ = "1.4"
__author__ = "Ragnarok"

import sys

import platform
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from algorithm.codification import ShannonFano as shannon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.icon = QIcon("sources/images/logo.png")
        self.setWindowIcon(self.icon)
        self.setWindowTitle("Encoding Algorithms Network")
        self.setMinimumSize(450, 400)
        self.setMaximumSize(450, 400)

        self.max_messages = 20

        self.create_menu_components()

        self.url_save = ''

    def create_menu_components(self):
        self.menubar = QMenuBar()
        self.statusbar = QStatusBar()

        self.menuFile = QMenu("&File")
        self.menuAction = QMenu("&Action")

        self.new_file_action = QAction("&New File", self)
        self.new_file_action.setStatusTip("Create a new encoding project")
        self.new_file_action.setShortcut("Ctrl+N")
        self.new_file_action.triggered.connect(self.new_file_function)
        self.menuFile.addAction(self.new_file_action)

        self.calculate_action = QAction("&Calculate", self)
        self.calculate_action.setStatusTip("Calculate encoding messages")
        self.calculate_action.setShortcut('Ctrl+Shift+C')
        self.calculate_action.triggered.connect(self.calculate_probabilities_function)
        self.menuAction.addAction(self.calculate_action)

        self.add_probabilities_action = QAction("&Add Probabilities", self)
        self.add_probabilities_action.setStatusTip("Add Probabilities")
        self.add_probabilities_action.setShortcut('Ctrl+Shift+A')
        self.add_probabilities_action.triggered.connect(self.add_column_function)
        self.menuAction.addAction(self.add_probabilities_action)

        self.remove_probabilities_action = QAction("&Remove Probabilities", self)
        self.remove_probabilities_action.setStatusTip("Remove Probabilities")
        self.remove_probabilities_action.setShortcut('Ctrl+Shift+R')
        self.remove_probabilities_action.triggered.connect(self.delete_column_function)
        self.menuAction.addAction(self.remove_probabilities_action)

        self.open_file_action = QAction("&Open File", self)
        self.open_file_action.setStatusTip("Open a encoding network file")
        self.open_file_action.setShortcut("Ctrl+O")
        self.open_file_action.triggered.connect(self.open_file_function)
        self.menuFile.addAction(self.open_file_action)

        self.save_action = QAction("&Save", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(self.save_function)
        self.menuFile.addAction(self.save_action)

        self.save_as_action = QAction("Save As", self)
        self.save_as_action.setShortcut("Ctrl+Shift+S")
        self.save_as_action.triggered.connect(self.save_as_function)
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
        self.about_shannon_action.triggered.connect(self.about_shannon_fano_function)
        self.menuHelp.addAction(self.about_shannon_action)

        self.about_action = QAction("&About Encoding Network", self)
        self.about_action.setStatusTip("Show information about Encoding Network")
        self.about_action.setShortcut("F1")
        self.about_action.triggered.connect(self.about_application_function)
        self.menuHelp.addAction(self.about_action)

        self.menubar.addMenu(self.menuFile)
        self.menubar.addMenu(self.menuAction)
        self.menubar.addMenu(self.menuHelp)

        self.setMenuBar(self.menubar)
        self.setStatusBar(self.statusbar)

        # cuerpo de la ventana principal
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        self.central_layout = QGridLayout()
        self.central_layout.setSpacing(2)

        self.table = QTableWidget(1, 2)
        self.table.setHorizontalHeaderLabels(["Probabilities", "Encoding message"])
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().resizeSection(0, self.width() / 2 - 15)
        # self.table.verticalHeader().hide()

        # button layout
        button_layout = QHBoxLayout()

        calculate_btn = QPushButton("Calculate")
        calculate_btn.clicked.connect(self.calculate_probabilities_function)

        exit_btn = QPushButton("Quit")
        exit_btn.clicked.connect(qApp.exit)

        add_column_btn = QPushButton("Add Probabilities")
        add_column_btn.clicked.connect(self.add_column_function)

        remove_column_btn = QPushButton("Remove Probabilities")
        remove_column_btn.clicked.connect(self.delete_column_function)

        button_layout.addWidget(calculate_btn)
        button_layout.addWidget(add_column_btn)
        button_layout.addWidget(remove_column_btn)
        button_layout.addWidget(exit_btn)

        self.central_layout.addWidget(self.table, 0, 0)
        self.central_layout.addLayout(button_layout, 1, 0)
        self.mainWidget.setLayout(self.central_layout)

        self.statusBar().showMessage('Ready')

        self.set_styles()

    def add_column_function(self):
        self.table.insertRow(self.table.rowCount())

    def delete_column_function(self):
        if self.table.rowCount() == 1:
            return

        if len(self.table.selectedIndexes()) == 0:
            self.table.removeRow(self.table.rowCount() - 1)
            return

        # self.table.clearContents()  # resetea todo el contenido de la tabla
        for i in self.table.selectedIndexes():
            self.table.removeRow(i.row())

    def calculate_probabilities_function(self):
        if self.table.itemAt(0, 0) is None:
            QMessageBox.warning(None, "Error in data", "you must give unless one number")
            return

        probabilities = []
        self.table.sortByColumn(0, Qt.DescendingOrder)

        for i in range(self.table.rowCount()):
            if self.table.item(i, 0) is None:
                QMessageBox.warning(None, "Error in data", "you must complete de information")
                return
            probabilities.append(float(self.table.item(i, 0).text()))

        encoding = shannon(probabilities).get_message_encoded()

        for i in range(self.table.rowCount()):
            self.table.setItem(i, 1, QTableWidgetItem(encoding[i]))

    def about_application_function(self):
        about = QMessageBox()
        about.setWindowIcon(self.icon)
        QMessageBox.about(about, "About Encripted Network",
                          '''
                          <p><b>Encrypted Network</b></p>
                          <p><b>Version:</b> {0}</p>
                          <p><b>Author:</b> {1}</p>
                          <p>University Informatics student.</p>
                          <p>This application using Shannon-Fano algorithm to encoding messages given the
                          probabilities for each text.
                          </p>
                          <p>This version run on {2}</p>
                          <p><footer>&copy; 2015 - 2016 Encrypted Network. All rights reserved.</footer></p>
                          '''.format(__version__, __author__, platform.system())
                          )

    def about_shannon_fano_function(self):
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

    def save_function(self):
        if not self.url_save == '':
            array = []
            array.append([])
            array.append([])
            for i in range(self.table.rowCount()):
                if self.table.item(i, 0) is None:
                    QMessageBox.warning(None, "Error in data", "you must complete de information")
                    return
                array[0].append(self.table.item(i, 0).text())
                array[1].append(self.table.item(i, 1).text())
            file = open(self.url_save, 'w')
            iterator = 0
            for row in array:
                iterator += 1
                for item in row:
                    file.write('{} '.format(item))
                if iterator != 2:
                    file.write('\n')
        else:
            self.save_as_function()

    def save_as_function(self):
        array = []
        array.append([])
        array.append([])
        for i in range(self.table.rowCount()):
            if self.table.item(i, 0) is None:
                QMessageBox.warning(None, "Error in data", "you must complete de information")
                return
            array[0].append(self.table.item(i, 0).text())
            array[1].append(self.table.item(i, 1).text())

        objFile = QFileDialog.getSaveFileName(self, "Save File", self.url_save,
                                                'Encripted File (*.enf);; All files (*.*)'
                                              )
        if objFile[0] == '':
            return
        filename = objFile[0]
        if not filename.endswith('.enf'):
            filename += '.enf'
        self.url_save = filename
        file = open(filename, 'w')
        iterator = 0
        for row in array:
            iterator += 1
            for item in row:
                file.write('{} '.format(item))
            if iterator != 2:
                file.write('\n')

    def new_file_function(self):
        if self.url_save == '':
            reply = QMessageBox.question(self, 'Estas seguro?', '¿Desea guardar los datos?', QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # comprobar si esta bien la informacion de la tabla
                self.save_function()
        for i in range(self.table.rowCount()):
            self.table.removeRow(0)
        self.table.insertRow(0)

    def open_file_function(self):
        self.new_file_function()
        objFile = QFileDialog.getOpenFileName(self, 'Open File', '/home/ceramica',
                                                'Encripted File (*.enf)'
                                              )
        if objFile[0] == '':
            return
        file = open(objFile[0], 'r')
        file_content = file.read()
        file_content = file_content.split('\n')
        file_probabilities = file_content[0].split()
        file_encoding = file_content[1].split()

        for i in range(len(file_probabilities)):
            self.table.insertRow(self.table.rowCount())
            self.table.setItem(i, 0, QTableWidgetItem(file_probabilities[i]))
            self.table.setItem(i, 1, QTableWidgetItem(file_encoding[i]))
        self.delete_column_function()

    def is_correct_table(self):
        for i in range(self.table.rowCount()):
            if self.table.item(i, 0) is None:
                return False
        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
