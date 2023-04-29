# Tesseract

# Convert document from pdf to image https://stackoverflow.com/questions/29657237/tesseract-ocr-pdf-as-input
import cv2
import pdf2image
import numpy as np
from preprocessing_image import preprocess_image
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file, first_page= 20, last_page=21)

def ocr_core(file):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(file, lang='spa')
    return text


def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    for pg, img in enumerate(images):
        img = preprocess_image(img)
        print(ocr_core(img))
        text = ocr_core(img)
        print('next')

#book_path = 'C:/Users/Hp/OneDrive/Escritorio/libro_3.pdf'
#print_pages(book_path)
