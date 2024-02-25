import fitz  # pip install PyMuPDF

pdf_path = '23-24strikerbot.pdf'

pdf_document = fitz.open(pdf_path)

all_text = []

for page_number in range(pdf_document.page_count):
    page = pdf_document[page_number]
    text = page.get_text()
    all_text.append(text)

pdf_document.close()

output_file_path = 'list.txt'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for text in all_text:
        output_file.write(text)
