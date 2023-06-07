# Tesseract

import cv2
import pytesseract
import fastwer
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from preprocessing_image import preprocess_image
import json

# TESSERACT MAIN

# Tesseract

# Convert document from pdf to image https://stackoverflow.com/questions/29657237/tesseract-ocr-pdf-as-input
import cv2
import pdf2image
import numpy as np
# try:
#     from PIL import Image
# except ImportError:
#     import Image
import pytesseract


class Scan:
    def __init__(self):
        data_path = 'C:/Users/Hp/PycharmProjects/ImageToTextArgentina/data/'
        df_output = pd.DataFrame()
        dict_parameters = {}

    def import_dict(self):
        cwd = os.getcwd()
        with open(cwd + "/pyqt5/dict_pyqt5.json") as file:
            dict_parameters = json.load(file)

    def pdf_to_img(pdf_file, FIRST_PAGE, LAST_PAGE):
        return pdf2image.convert_from_path(pdf_file, first_page=FIRST_PAGE, last_page=LAST_PAGE)

    def ocr_core(file):
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        text = pytesseract.image_to_string(file, lang='spa')
        return text

    def clean_line_break(file):
        file = file.replace("\n", "")
        file = file.replace("-\n", "")
        return file

    def str2bool(v):
        return v.lower() in ("yes", "true", "t", "1")

    def run(self):
        pass
data_path = 'C:/Users/Hp/PycharmProjects/ImageToTextArgentina/data/'

def pdf_to_img(pdf_file, FIRST_PAGE, LAST_PAGE):
    return pdf2image.convert_from_path(pdf_file, first_page= FIRST_PAGE, last_page=LAST_PAGE)

def ocr_core(file):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(file, lang='spa')
    return text

def clean_line_break(file):
    file = file.replace("\n", "")
    file = file.replace("-\n", "")
    return file

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

import os
cwd = os.getcwd()


with open(cwd + "/pyqt5/dict_pyqt5.json") as file:
    parameters_dict = json.load(file)



parameters = {'SampleFile': 'libro_1_sample.txt', 'BookFile': 'libro_1.pdf', 'FirstPage': 20, 'LastPage': 21, 'Sampling': False,
              'CroppingImage': False, 'ThresholdingImage': True,
              'ResizingImage': True,
              'ResizingMethod': 1, 'ThresholdingMethod': 1}

# parameters = {'SampleFile': sample, 'BookFile': pdf, 'FirstPage': first_page, 'LastPage': last_page, 'Sampling': sampling,
#               'CroppingImage': cropping_image, 'ThresholdingImage': thresholding_image,
#               'ResizingIma': resizing_image,
#               'ResizingMethod': resizing_method, 'ThresholdingMethod': thresholding_method}

# Create empty dataframe to store output
df_output = pd.DataFrame(columns = ['pdf_filename', 'sample_filename', 'txt_reference', 'ocr_output', 'cer', 'wer'])
df_output['pdf_filename'] = parameters['BookFile']

first_page = parameters['FirstPage']
last_page = parameters['LastPage']
images = pdf_to_img(data_path + parameters['BookFile'], first_page, last_page)
with open(data_path + parameters['SampleFile'],  'r', encoding='utf-8') as f :
    reference_text = f.read()
output_text = ''
# pnr_area = [150, 450, 1600, 1150] #TODO: In progress
for pg, img in enumerate(images):
    img = preprocess_image(img, parameters = parameters)
    output_aux_text = ocr_core(img)
    output_text += output_aux_text
    #print(pdf)
    #print(img)
    #print(output_aux_text)
output_text = clean_line_break(output_text)
reference_text = clean_line_break(reference_text)

cer = fastwer.score_sent(output_text, reference_text, char_level=True)
wer = fastwer.score_sent(output_text, reference_text, char_level=False)
df_output.loc[df_output['pdf_filename'] == parameters['BookFile'], 'sample_filename'] = parameters['SampleFile']
df_output.loc[df_output['pdf_filename'] == parameters['BookFile'], 'txt_reference'] = reference_text[0:200]
df_output.loc[df_output['pdf_filename'] == parameters['BookFile'], 'ocr_output'] = output_text[0:200]
df_output.loc[df_output['pdf_filename'] == parameters['BookFile'], 'cer'] = cer
df_output.loc[df_output['pdf_filename'] == parameters['BookFile'], 'wer'] = wer
# print(df_output)
df_output
