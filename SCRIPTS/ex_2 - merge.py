import os; import subprocess; clear = lambda: os.system('cls'); clear()
import pypdf; print("Python Library: ", pypdf.__name__, pypdf.__version__)
################################################################################

pdf = 'PDF\\2 - Camelot Project.pdf'

################################################################################

print("\n***************************************************************************")
print("MERGE")
print("***************************************************************************\n")

reader = pypdf.PdfReader(pdf)
writer = pypdf.PdfWriter()

for page in reader.pages: writer.add_page(page)

input = 'PDF\\z - blank.pdf'
input = pypdf.PdfReader(input)

for page in input.pages: writer.add_page(page)

with open(pdf[:-4]+'_blank.pdf', "wb") as f: writer.write(f)
output = pypdf.PdfReader(pdf[:-4]+'_blank.pdf')

num_pages = len(reader.pages)
print(f"- Número de páginas (antes) : {num_pages}\n")
num_pages_new = len(output.pages)
print(f"- Número de páginas (ahora) : {num_pages_new}")

print("\n***************************************************************************\n")
