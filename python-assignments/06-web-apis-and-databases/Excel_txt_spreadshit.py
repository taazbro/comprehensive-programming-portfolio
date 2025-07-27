import openpyxl


text_file_path = '/Users/tanjim//Downloads/Phone_Number_and_Email_Address.txt'
excel_file_path = '/Users/tanjim//Downloads/Phone_Numbers_and_Emails.xlsx'


workbook = openpyxl.Workbook()
sheet = workbook.active


with open(text_file_path, 'r') as file:
    lines = file.readlines()


for index, line in enumerate(lines):
   
    sheet.cell(row=index + 1, column=1).value = line.strip()


workbook.save(excel_file_path)
