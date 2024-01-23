import os; import subprocess; clear = lambda: os.system('cls'); clear()
import pypdf; print("Python Library: ", pypdf.__name__, pypdf.__version__)
################################################################################

pdf = 'PDF\\1 - The Zen of Python.pdf'
#pdf = 'PDF\\2 - Camelot Project.pdf'
#pdf = 'PDF\\3 - CEC Membership Form.pdf'

################################################################################

print("\n***************************************************************************")
print("METADATA")
print("***************************************************************************\n")

reader = pypdf.PdfReader(pdf)
writer = pypdf.PdfWriter()
for page in reader.pages: writer.add_page(page)
writer.add_metadata(reader.metadata)
#writer.add_metadata({"/Title":pdf,"/Author": "X"})
with open(pdf, "wb") as f: writer.write(f)

metadata = reader.metadata
print(f"- Title: {metadata.title}")
print(f"- Subject: {metadata.subject}")
print(f"- Author: {metadata.author}")
print(f"- Creation_Date: {metadata.creation_date}")
print(f"- Modification_Date: {metadata.modification_date}")
print(f'- Tamaño del archivo {round(os.stat(pdf).st_size / (1024 * 1024), 2)} MB')
print(f"- Número de páginas: {len(reader.pages)}")

print("\n***************************************************************************\n")
