from PyQt5.QtWidgets import QApplication
from gui import PDFReaderGUI
import sys

def main():
    app = QApplication(sys.argv)
    ex = PDFReaderGUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
