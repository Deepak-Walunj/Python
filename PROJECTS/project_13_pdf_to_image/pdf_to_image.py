from pdf2image import convert_from_path
import os

# Path to the uploaded PDF file
pdf_folder = r"C:/Users/deepa/Desktop/python/Python/PROJECTS/project_13_pdf_to_image/pdf"
image_folder = r"C:/Users/deepa/Desktop/python/Python/PROJECTS/project_13_pdf_to_image/image"
os.makedirs(image_folder, exist_ok=True)
pdf_files=[f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
for pdf_file in pdf_files:
    pdf_path=os.path.join(pdf_folder,pdf_file)
    try:
        pages = convert_from_path(pdf_path, 300)  # Convert at 300 DPI
        print(pages)
        for i, page in enumerate(pages):
            image_path = os.path.join(image_folder,f"{os.path.splitext(pdf_file)[0]}_page_{i+1}.png")
            page.save(image_path, 'PNG')
            print(f'Saved: {image_path}')
        os.remove(pdf_path)
        print(f"Deleted: {pdf_path}")
    except Exception as e:
        print(f'Error: {e}')

