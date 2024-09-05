from PyQt5.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt
from .pdf_handler import PDFHandler

class PDFReaderGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pdf_handler = PDFHandler()

    def initUI(self):
        self.setWindowTitle('Scrib - PDF Reader')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.label = QLabel('No PDF loaded', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        btn = QPushButton('Open PDF', self)
        btn.clicked.connect(self.open_file)
        layout.addWidget(btn)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        if file_name:
            self.pdf_handler.open_pdf(file_name)
            self.label.setText(f"Current PDF: {file_name}")
            # Here you would typically update the GUI to show PDF content or pages
