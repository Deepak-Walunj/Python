from PyPDF2 import PdfWriter,PdfReader
import os
def mergePdfs(dir):
    merger=PdfWriter()
    files=[file for file in os.listdir(dir) if file.endswith(".pdf") ]
    os.chdir(dir)
    for pdf in files:
        with open (pdf,"rb") as file:
            reader=PdfReader(file)
            merger.append(reader)
            
    out_path=os.path.join(dir,"Merged_pdf.pdf")
    with open (out_path,"wb") as file:    
        merger.write(file)

    
if __name__=="__main__":
    dir="C:\\Users\\Deepak\\OneDrive\\Desktop\\Python\\PROJECTS\\project_7"
    mergePdfs(dir)