import os; import subprocess; clear = lambda: os.system('cls'); clear()
import pypdf; print("Python Library: ", pypdf.__name__, pypdf.__version__)
################################################################################

pdf = 'PDF\\3 - CEC Membership Form.pdf'

################################################################################

print("\n***************************************************************************")
print("FORMS")
print("***************************************************************************\n")

reader = pypdf.PdfReader(pdf)
writer = pypdf.PdfWriter()

num_pages = len(reader.pages)
print(f"Número de páginas: {num_pages}\n")

fields = list(reader.get_fields().keys())
print(f"Número de campos: {len(fields)}\n")

print(sorted(fields, key=str.capitalize))

for i in range(num_pages): 

    writer.append(reader)
    writer.update_page_form_field_values(writer.pages[i],{'Nom': 'Jordi', 'Cognoms': 'Bosch'})

    with open(pdf[:-4]+"_filled.pdf", "wb") as f: writer.write(f)

print("\n***************************************************************************\n")
