from pypdf import PdfReader
import pandas as pd

pdf_path = r"C:\Users\arghya.guha\Downloads\test_doc_pdf.pdf"
reader = PdfReader(pdf_path)

data = []

for page_num, page in enumerate(reader.pages, start=1):
    if "/Annots" in page:
        annotations = page["/Annots"]
        for annot_ref in annotations:
            print(annot_ref)
            annot = annot_ref.get_object()
            content = annot.get("/Contents")
            # print(content)
            if content:
                author = annot.get("/T", "")
                # print(f"Page {page_num} | Author: {author} | Comment: {content}")
                data.append({
                    "PageNo": page_num,
                    "Author": author,
                    "Comment": content
                })

# Save to Excel/CSV
df = pd.DataFrame(data, columns=["PageNo", "Author", "Comment"])
df.to_csv("extracted_sticky_notes.csv", index=False, encoding='utf-8')
print("✅ Sticky note extraction complete. Saved to 'extracted_sticky_notes.csv'")
