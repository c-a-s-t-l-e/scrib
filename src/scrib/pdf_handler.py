import fitz  # PyMuPDF

class PDFHandler:
    def __init__(self):
        self.doc = None

    def open_pdf(self, filepath):
        """Open and load a PDF file."""
        try:
            self.doc = fitz.open(filepath)
            # Here you might want to initialize some state or prepare for rendering
        except Exception as e:
            print(f"Failed to open PDF: {e}")

    def get_page(self, page_num):
        """Retrieve a specific page from the PDF."""
        if self.doc and 0 <= page_num < self.doc.page_count:
            return self.doc[page_num]
        return None

    def close_pdf(self):
        """Close the current PDF document."""
        if self.doc:
            self.doc.close()
            self.doc = None
