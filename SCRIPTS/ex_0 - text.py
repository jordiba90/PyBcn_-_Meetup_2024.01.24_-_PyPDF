import os; import subprocess; clear = lambda: os.system('cls'); clear()
import pypdf; print("Python Library: ", pypdf.__name__, pypdf.__version__)
################################################################################

pdf = 'PDF\\1 - The Zen of Python.pdf'

################################################################################

print("\n***************************************************************************")
print("TEXT")
print("***************************************************************************\n")

reader = pypdf.PdfReader(pdf)

text = ""
for i in range(len(reader.pages)): text += reader.pages[i].extract_text()

print(f"- Número de páginas: {len(reader.pages)}\n")
print(f"- Número de carácteres: {len(text)}\n")

text = text[307:1205]
text = [line.strip() for line in text.splitlines()]
print(f"- Ejemplo de texto: {text[:1]}")

print("\n***************************************************************************\n")
