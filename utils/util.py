import json 
import csv
import pandas as pd
import PyPDF2
import tabula
import os
import fitz  # PyMuPDF
import xlwings as xw

def read_json_array(json_data):
    with open(json_data, "r") as file:
        data = json.load(file)
    df = pd.json_normalize(data)
    table_string = df.to_csv(index=False,header=True,sep=',')
    return table_string

def parse_json(json_data,field):
    with open(json_data,'r') as json_file:
        try:
            data = json.load(json_file)
            keys = field.split('.')
            current = data
            for key in keys:
                current=current[key]
            return current
        except (json.JSONDecodeError,KeyError):
            return None


# still need improvement
def get_json_fields_list(json_data):
    fields = set()
    with open(json_data,'r') as json_file:
        if isinstance(json_file, dict):
            for key, value in json_data.items():
                fields.add(key)
                fields.update(get_json_fields_list(value))
        elif isinstance(json_file, list):
            for item in json_file:
                fields.update(get_json_fields_list(item))
        print(fields)



def pdf_to_text(file_path):
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

def pdf_table_to_csv(pdf_path):
    tables = tabula.read_pdf(pdf_path,pages="all")
    for i, table in enumerate(tables):
        output_csv = f'./files/output_table_{i}.csv'
        table.to_csv(output_csv, index=False)

def extract_images_from_pdf(location_pdf,location_output):
    os.makedirs(location_output, exist_ok=True)

    # Open the PDF
    pdf_document = fitz.open(location_pdf)

    # Loop through each page
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        images = page.get_images(full=True)
        
        # Loop through each image on the page
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_data = base_image["image"]
            image_format = base_image["ext"]

            # Save the image to the output folder
            image_filename = f"{location_output}/page_{page_number + 1}_image_{img_index + 1}.{image_format}"
            with open(image_filename, "wb") as image_file:
                image_file.write(image_data)

    # Close the PDF
    pdf_document.close()

def xlwings_xlsx_to_dictionary(locationFile,sheetName):
    ws = xw.Book(locationFile).sheets[sheetName]
    table_range = ws.range('A1').expand()
    table_data = table_range.value
    header_row = table_range.rows[0].value
    table_data = []

    # Iterate through each row of the table (excluding the header row)
    for row_values in table_range.rows[1:]:
        row_dict = {}
        for col_index, col_value in enumerate(row_values.value):
            col_name = header_row[col_index]
            row_dict[col_name] = col_value
        table_data.append(row_dict)
    return table_data

def csv_to_dictionary(file_path):
    data_list = []  # Initialize an empty list to store dictionaries

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)  # Read the header row
        for row in csv_reader:
            data_dict = {}
            for i, value in enumerate(row):
                data_dict[headers[i]] = value
            data_list.append(data_dict)

    return data_list