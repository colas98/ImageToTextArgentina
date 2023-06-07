# Tesseract

import cv2
import pytesseract
import fastwer
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from preprocessing_image import preprocess_image


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

# # Show the sample images that we will work on (Need to create a folder to upload sample images in Colab environment)
# sample_list = os.listdir(data_path)
# pdf_list = os.listdir(data_path)
#
# pdf = input("pdf name?") # libro_1.pdf
# sample = input("sample name?") # libro_1_sample.txt
#
# if pdf not in pdf_list or sample not in sample_list:
#     raise NameError
#
# # Inputing parameters
# first_page = int(input('first_page')) # 20
# last_page = int(input('last_page')) # 21
# sampling = str2bool(input('sampling')) # False
# cropping_image = str2bool(input('cropping_image')) # False
# thresholding_image = str2bool(input('thresholding_image')) # True
# thresholding_method = int(input('thresholding_method')) # 1-7
# resizing_image = str2bool(input('resizing_image')) # False
# resizing_method = int(input('resizing_method')) # 1-3



parameters = {'sample': 'libro_1_sample.txt', 'pdf': 'libro_1.pdf', 'first_page': 20, 'last_page': 21, 'sampling': False,
              'cropping_image': False, 'thresholding_image': True,
              'resizing_image': True,
              'resizing_method': 1, 'thresholding_method': 2}

# parameters = {'sample': sample, 'pdf': pdf, 'first_page': first_page, 'last_page': last_page, 'sampling': sampling,
#               'cropping_image': cropping_image, 'thresholding_image': thresholding_image,
#               'resizing_image': resizing_image,
#               'resizing_method': resizing_method, 'thresholding_method': thresholding_method}

# Create empty dataframe to store output
df_output = pd.DataFrame(columns = ['pdf_filename', 'sample_filename', 'txt_reference', 'ocr_output', 'cer', 'wer'])
df_output['pdf_filename'] = parameters['pdf']

first_page = parameters['first_page']
last_page = parameters['last_page']
images = pdf_to_img(data_path + parameters['pdf'], first_page, last_page)
with open(data_path + parameters['sample'],  'r', encoding='utf-8') as f :
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
df_output.loc[df_output['pdf_filename'] == parameters['pdf'], 'sample_filename'] = parameters['sample']
df_output.loc[df_output['pdf_filename'] == parameters['pdf'], 'txt_reference'] = reference_text[0:200]
df_output.loc[df_output['pdf_filename'] == parameters['pdf'], 'ocr_output'] = output_text[0:200]
df_output.loc[df_output['pdf_filename'] == parameters['pdf'], 'cer'] = cer
df_output.loc[df_output['pdf_filename'] == parameters['pdf'], 'wer'] = wer
# print(df_output)
df_output
