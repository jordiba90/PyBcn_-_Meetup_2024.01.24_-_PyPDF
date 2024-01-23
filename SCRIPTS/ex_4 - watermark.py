import os; import subprocess; clear = lambda: os.system('cls'); clear()
import pypdf; print("Python Library: ", pypdf.__name__, pypdf.__version__)
################################################################################

pdf = 'PDF\\2 - Camelot Project.pdf'
water = 'PDF\\z - watermark.pdf'

################################################################################

print("\n***************************************************************************")
print("WATERMARK")
print("***************************************************************************\n")

reader = pypdf.PdfReader(pdf)

num_pages = len(reader.pages)
print(f"- Número de páginas: {num_pages}\n")

for i in range(num_pages): 

    stamp = pypdf.PdfReader(pdf).pages[i]
    writer = pypdf.PdfWriter(clone_from=water)
    
    for page in writer.pages:
        
        page.merge_page(stamp, over=False) 
        writer.add_page(page)

    writer.write(pdf[:-4]+"_watermark.pdf")

print("\n***************************************************************************\n")
