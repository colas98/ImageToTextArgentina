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
import os

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
        self.df_output =  pd.DataFrame(
            columns=['pdf_filename', 'sample_filename', 'txt_reference', 'ocr_output', 'cer', 'wer'])
        self.dict_parameters = {}

    def import_dict(self):
        cwd = os.getcwd()
        with open(cwd + "/pyqt5/dict_pyqt5.json") as file:
            self.dict_parameters = json.load(file)


    def pdf_to_img(self, pdf_file, FIRST_PAGE, LAST_PAGE):
        return pdf2image.convert_from_path(pdf_file, first_page=FIRST_PAGE, last_page=LAST_PAGE)

    def ocr_core(self,file):
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        text = pytesseract.image_to_string(file, lang='spa')
        return text

    def clean_line_break(self,file):
        file = file.replace("\n", "")
        file = file.replace("-\n", "")
        return file

    def str2bool(self,v):
        return v.lower() in ("yes", "true", "t", "1")

    def run(self):
        self.import_dict()
        self.df_output = self.df_output.assign(pdf_filename = [self.dict_parameters['Paths']['BookFile']])

        images = self.pdf_to_img(self.dict_parameters['Paths']['BookFile'], self.dict_parameters['GeneralParameters']['FirstPage'],
                            self.dict_parameters['GeneralParameters']['LastPage'])
        with open(self.dict_parameters['Paths']['SampleFile'], 'r', encoding='utf-8') as f:
            reference_text = f.read()
        output_text = ''
        for pg, img in enumerate(images):
            img = preprocess_image(img, parameters=self.dict_parameters)
            output_aux_text = self.ocr_core(img)
            output_text += output_aux_text
        output_text = self.clean_line_break(output_text)
        reference_text = self.clean_line_break(reference_text)

        cer = fastwer.score_sent(output_text, reference_text, char_level=True)
        wer = fastwer.score_sent(output_text, reference_text, char_level=False)
        self.df_output.loc[self.df_output['pdf_filename'] == self.dict_parameters['Paths']['BookFile'], 'sample_filename'] = self.dict_parameters['Paths']['SampleFile']
        self.df_output.loc[self.df_output['pdf_filename'] == self.dict_parameters['Paths']['BookFile'], 'txt_reference'] = reference_text[0:200]
        self.df_output.loc[self.df_output['pdf_filename'] == self.dict_parameters['Paths']['BookFile'], 'ocr_output'] = output_text[0:200]
        self.df_output.loc[self.df_output['pdf_filename'] == self.dict_parameters['Paths']['BookFile'], 'cer'] = cer
        self.df_output.loc[self.df_output['pdf_filename'] == self.dict_parameters['Paths']['BookFile'], 'wer'] = wer
        # print(self.df_output)
        self.df_output

if __name__ == '__main__':
    ScanTest = Scan()
    ScanTest.run()
    print('end')