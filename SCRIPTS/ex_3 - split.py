import os; import subprocess; clear = lambda: os.system('cls'); clear()
import pypdf; print("Python Library: ", pypdf.__name__, pypdf.__version__)
################################################################################

pdf = 'PDF\\2 - Camelot Project.pdf'

################################################################################

print("\n***************************************************************************")
print("SPLIT")
print("***************************************************************************\n")

reader = pypdf.PdfReader(pdf)
num_pages = len(reader.pages)

for page in range(num_pages):

    writer = pypdf.PdfWriter()
    writer.add_page(reader.pages[page])
    with open(pdf[:-4]+'_'+str(page)+'.pdf', "wb") as f: writer.write(f)

files = os.listdir('PDF')
files = [file for file in files if pdf[4:-4] in file][1:]

print(f"Archivos creados:\n")
for i in range(len(files)):print(files[i])

print("\n***************************************************************************\n")
