import PyPDF2

# Buka file PDF (ganti 'nama_file.pdf' ke nama file lo kalo beda)
with open("berita.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        print(page.extract_text())