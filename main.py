# Tesseract

import cv2
import pytesseract
import fastwer
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Image, display
from preprocessing_image import preprocess_image


# TESSERACT MAIN

# Tesseract

# Convert document from pdf to image https://stackoverflow.com/questions/29657237/tesseract-ocr-pdf-as-input
import cv2
import pdf2image
import numpy as np
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract



# parser = argparse.ArgumentParser(description="This program extracts provision numbers from a set of documents.")
# parser.add_argument("-i", "--input_dir", help="Input directory for the files to be modified")
# parser.add_argument("-o", "--output_dir", help="Output directory for the files to be modified")
# args = parser.parse_args()
#
# input_dir = args.input_dir
# output_dir = args.output_dir
#
# if os.path.exists(output_dir):
#     shutil.rmtree(output_dir)
# os.makedirs(output_dir)
#
# im_names = glob.glob(os.path.join(input_dir, '*.png')) + \
#            glob.glob(os.path.join(input_dir, '*.jpg')) + \
#            glob.glob(os.path.join(input_dir, '*.jpeg'))


def pdf_to_img(pdf_file, FIRST_PAGE, LAST_PAGE):
    return pdf2image.convert_from_path(pdf_file, first_page= FIRST_PAGE, last_page=LAST_PAGE)

def ocr_core(file):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(file, lang='spa')
    return text

# Show the sample images that we will work on (Need to create a folder to upload sample images in Colab environment)
txt_testing = os.listdir('C:/Users/Hp/PycharmProjects/ImageToTextArgentina/data')
# txt_testing = sorted(txt_testing)
# txt_testing = [doc for doc in txt_testing if '.txt' in doc]
# sample = txt_testing[0]

pdf_list = os.listdir('C:/Users/Hp/PycharmProjects/ImageToTextArgentina/data')
# pdf_list = sorted(pdf_list)
# pdf_list = [doc for doc in pdf_list if '.pdf' in doc]
# pdf_list = pdf_list[0]

pdf_dict = {
'libro_1.pdf': {'first_page': 20, 'last_page': 21, 'sample': 'libro_1_sample.txt', 'sampling': True, 'sampling_type': 1,
                'cropping_image': False, 'thresholding_image': False, 'resizing_image': False},
} # pedir first_page y last_page como argumento

# Create empty dataframe to store output
df_output = pd.DataFrame(columns = ['pdf_filename', 'sample_filename', 'txt_reference', 'ocr_output', 'cer', 'wer'])

# df_output['pdf_filename'] = pdf_list
df_output['pdf_filename'] = 'libro_1.pdf'

for num, pdf in enumerate(pdf_list):
    first_page = pdf_dict[pdf]['first_page']
    last_page = pdf_dict[pdf]['last_page']
    images = pdf_to_img('C:/Users/Hp/PycharmProjects/ImageToTextArgentina/data/' + pdf, first_page, last_page)
    with open('C:/Users/Hp/PycharmProjects/ImageToTextArgentina/data/' + pdf_dict[pdf]['sample'],  'r', encoding='utf-8') as f :
        reference_text = f.read()
    output_text = ''
    pnr_area = [150, 450, 1600, 1150]
    dict_preprocessing = {}
    for pg, img in enumerate(images):
        img = preprocess_image(img, dict_preprocessing = pdf_dict[pdf])
        output_aux_text = ocr_core(img)
        output_text += output_aux_text
        #print(pdf)
        #print(img)
        #print(output_aux_text)
    output_text = output_text.replace("\n", "")
    output_text = output_text.replace("-\n", "")
    reference_text = reference_text.replace("\n", "")
    reference_text = reference_text.replace("-\n", "")
    cer = fastwer.score_sent(output_text, reference_text, char_level=True)
    wer = fastwer.score_sent(output_text, reference_text, char_level=False)
    df_output.loc[df_output['pdf_filename'] == pdf, 'sample_filename'] = pdf_dict[pdf]['sample']
    df_output.loc[df_output['pdf_filename'] == pdf, 'txt_reference'] = reference_text[0:200]
    df_output.loc[df_output['pdf_filename'] == pdf, 'ocr_output'] = output_text[0:200]
    df_output.loc[df_output['pdf_filename'] == pdf, 'cer'] = cer
    df_output.loc[df_output['pdf_filename'] == pdf, 'wer'] = wer

df_output

