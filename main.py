# Tesseract

# Convert document from pdf to image https://stackoverflow.com/questions/29657237/tesseract-ocr-pdf-as-input

import pdf2image
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file, first_page= 1, last_page=2)


def ocr_core(file):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(file, lang='spa')
    return text


def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    for pg, img in enumerate(images):
        print(ocr_core(img))


book_path = 'C:/Users/Hp/OneDrive/Escritorio/libro_sabina.pdf'
print_pages(book_path)
