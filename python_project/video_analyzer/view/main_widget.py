from PyQt5.QtWidgets import QWidget, QTableWidget, QHeaderView, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton,\
    QLabel, QSpacerItem, QSizePolicy, QFileDialog, QGroupBox, QComboBox


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(open('D:\\MAESTRIA\\TecEmergentes\\video_analyzer\\styles\\basic_style.css').read())
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(('Algorithm', 'Word', 'Percentage', 'Second', 'Time'))
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layoutLeftMain = QVBoxLayout()
        self.group_box = QGroupBox()
        self.layoutLeftMain.addWidget(self.group_box)

        self.layoutLeft = QVBoxLayout()
        self.group_box.setLayout(self.layoutLeft)

        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)
        self.browse_button = QPushButton('Browse')
        self.browse_button.clicked.connect(self.__browse_file)

        self.word = QLineEdit()
        # self.algorithm = QLineEdit()
        self.algorithm = QComboBox()
        self.algorithm.addItem("LeeNet")
        self.algorithm.addItem("ProxyLeeNet")
        self.algorithm.addItem("Custom")

        # self.percentage = QLineEdit()
        self.percentage = QComboBox()
        self.percentage.addItem("0")
        self.percentage.addItem("10")
        self.percentage.addItem("20")
        self.percentage.addItem("30")
        self.percentage.addItem("40")
        self.percentage.addItem("50")
        self.percentage.addItem("60")
        self.percentage.addItem("70")
        self.percentage.addItem("80")
        self.percentage.addItem("90")
        self.percentage.addItem("100")

        self.buttonSearch = QPushButton('Search')
        self.vertical_spacer = QSpacerItem(10, 450, QSizePolicy.Expanding)

        self.layoutLeft.setSpacing(5)

        self.layoutLeft.addWidget(QLabel('File Path'))
        self.layoutLeft.addWidget(self.file_path)
        self.layoutLeft.addWidget(self.browse_button)
        self.layoutLeft.addWidget(QLabel('word'))
        self.layoutLeft.addWidget(self.word)
        self.layoutLeft.addWidget(QLabel('algorithm'))
        self.layoutLeft.addWidget(self.algorithm)
        self.layoutLeft.addWidget(QLabel('percentage'))
        self.layoutLeft.addWidget(self.percentage)
        self.layoutLeft.addWidget(self.buttonSearch)

        self.layoutLeftMain.addSpacerItem(self.vertical_spacer)
        self.layoutLeftMain.addWidget(QLabel('AT BootCamp'))

        self.layout = QHBoxLayout()
        self.layout.addLayout(self.layoutLeftMain, 25)
        self.layout.addWidget(self.table, 75)
        self.setLayout(self.layout)

    def __browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', 'Video file (*.mp4)')
        print(file_name[0])
        self.file_path.setText(file_name[0])

    def get_button_search(self):
        print('get_button_search')
        return self.buttonSearch
