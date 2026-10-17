

from pypdf import PdfReader

with open(r"C:\Users\tsiri\OneDrive\Documents\Kathleen Kail Parent Notification - Teaching Certification Letter.pdf", "rb") as file:
    reader = PdfReader(file)

    for page in reader.pages:
        print(page.extract_text())