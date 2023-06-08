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
import copy

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

NUM_THRESHOLDING_METHOD_OPTIONS = 7
NUM_RESIZING_METHOD_OPTIONS = 3


class Scan:
    def __init__(self, dict_parameters):
        self.df_output = pd.DataFrame(
            columns=['pdf_filename', 'sample_filename', 'txt_reference', 'ocr_output', 'cer', 'wer', 'resizing_method',
                     'thresholding_method'])
        self.dict_parameters = dict_parameters
        self.num_thresholding_method_options = 7
        self.num_resizing_method_options = 3
    def pdf_to_img(self, pdf_file, FIRST_PAGE, LAST_PAGE):
        return pdf2image.convert_from_path(pdf_file, first_page=FIRST_PAGE, last_page=LAST_PAGE)

    def ocr_core(self, file):
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        text = pytesseract.image_to_string(file, lang='spa')
        return text

    def clean_line_break(self, file):
        file = file.replace("\n", "")
        file = file.replace("-\n", "")
        return file

    def str2bool(self, v):
        return v.lower() in ("yes", "true", "t", "1")

    def run(self):
        self.df_output = self.df_output.assign(pdf_filename=[self.dict_parameters['Paths']['BookFile']])

        images = self.pdf_to_img(self.dict_parameters['Paths']['BookFile'],
                                 self.dict_parameters['GeneralParameters']['FirstPage'],
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
        self.df_output.loc[
            self.df_output['pdf_filename'] == self.dict_parameters['Paths']['BookFile'], 'sample_filename'] = \
            self.dict_parameters['Paths']['SampleFile']
        self.df_output.loc[self.df_output['pdf_filename'] == self.dict_parameters['Paths'][
            'BookFile'], 'txt_reference'] = reference_text[0:200]
        self.df_output.loc[
            self.df_output['pdf_filename'] == self.dict_parameters['Paths']['BookFile'], 'ocr_output'] = output_text[
                                                                                                         0:200]
        self.df_output.loc[self.df_output['pdf_filename'] == self.dict_parameters['Paths']['BookFile'], 'cer'] = cer
        self.df_output.loc[self.df_output['pdf_filename'] == self.dict_parameters['Paths']['BookFile'], 'wer'] = wer
        self.df_output.loc[
            self.df_output['pdf_filename'] == self.dict_parameters['Paths']['BookFile'], 'thresholding_method'] = \
        self.dict_parameters['AdvancedParameters']['ThresholdingMethod']
        self.df_output.loc[
            self.df_output['pdf_filename'] == self.dict_parameters['Paths']['BookFile'], 'resizing_method'] = \
        self.dict_parameters['AdvancedParameters']['ResizingMethod']

        # print(self.df_output)
        return self.df_output


if __name__ == '__main__':
    cwd = os.getcwd()
    with open(cwd + "/pyqt5/dict_pyqt5.json") as file:
        dict_parameters = json.load(file)
    dict_parameters_list = []

    if dict_parameters['AdvancedParameters']['ThresholdingMethod'] == 'All' and not \
            dict_parameters['AdvancedParameters']['ResizingMethod'] == 'All':
        for num in range(1, NUM_THRESHOLDING_METHOD_OPTIONS + 1):
            dict_parameters_list.append(copy.deepcopy(dict_parameters))
            dict_parameters_list[num - 1]['AdvancedParameters']['ThresholdingMethod'] = num

    if dict_parameters['AdvancedParameters']['ResizingMethod'] == 'All' and not dict_parameters['AdvancedParameters'][
                                                                                    'ThresholdingMethod'] == 'All':
        for num in range(1, NUM_RESIZING_METHOD_OPTIONS + 1):
            dict_parameters_list.append(copy.deepcopy(dict_parameters))
            dict_parameters_list[num - 1]['AdvancedParameters']['ThresholdingMethod'] = num

    if dict_parameters['AdvancedParameters']['ThresholdingMethod'] == 'All' and dict_parameters['AdvancedParameters'][
        'ResizingMethod'] == 'All':
        for num in range(1, NUM_THRESHOLDING_METHOD_OPTIONS + 1):
            for num_2 in range(1, NUM_RESIZING_METHOD_OPTIONS + 1):
                dict_parameters_list.append(copy.deepcopy(dict_parameters))
                dict_parameters_list[num * NUM_THRESHOLDING_METHOD_OPTIONS + num_2 - 1]['AdvancedParameters'][
                    'ThresholdingMethod'] = num
                dict_parameters_list[num * NUM_RESIZING_METHOD_OPTIONS + num_2 - 1]['AdvancedParameters'][
                    'ResizingMethod'] = num_2
    df_output_total =  pd.DataFrame(
            columns=['pdf_filename', 'sample_filename', 'txt_reference', 'ocr_output', 'cer', 'wer', 'resizing_method',
                     'thresholding_method'])
    for dict_parameters in dict_parameters_list:
        print(dict_parameters)
        ScanBook = Scan(dict_parameters)
        df_output = ScanBook.run()
        df_output_total = pd.concat([df_output_total, df_output])
    df_output_total
    print('end')
