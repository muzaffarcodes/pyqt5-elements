import sys
import random
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QPushButton,QWidget,QApplication,QLabel,QTextEdit,QLineEdit
class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Dice Roller")
		self.setGeometry(100,100)
		self.ui_start()
	def ui_start(self):
		self.start = QPushButton("Start")
		self.restart = QPushButton("Restart")
		self.clear = QPushButton("Clear All")

		self.textBody = QLineEdit()

		h_box = QHBoxLayout()
		h_box.addWidget(self.textBody)
		h_box.addWidget(self.start)
		h_box.addWidget(self.restart)
		h_box.addWidget(self.clear)
		v_box = QVBoxLayout()
		v_box.addLayout(h_box)

		self.setLayout(v_box)
		self.setFixedSize(500,100)

		self.start.clicked.connect()
		self.start.clicked.connect()
		self.clear.clicked.connect()

		self.show()
	def start_b(self):
		if self.sender().text() == "Start":
					
			

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())