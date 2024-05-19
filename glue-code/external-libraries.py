from pdf_generator.generate_pdf import create_pdf

def process_data():
    data = {'name': 'Bob', 'age': 35, 'city': 'Chicago'}
    create_pdf(data, 'output.pdf')

process_data()
