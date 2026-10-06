import os

import cloudinary
import cloudinary.uploader
import pymupdf

from config import (
    CLOUDINARY_API_KEY,
    CLOUDINARY_API_SECRET,
    CLOUDINARY_CLOUD_NAME,
)


class PdfHighlighter:
    def __init__(self, pdf_path, ner_dict):
        self.pdf_path = pdf_path
        self.ner_dict = ner_dict
        self.list = []

    def highlight(self):
        try:
            print("\nHighlighting user PDF...\n")

            self.list = list(self.ner_dict.keys())
            doc = pymupdf.open(self.pdf_path)

            for page in doc:
                for word in self.list:
                    for instance in page.search_for(word):
                        page.add_highlight_annot(instance)

            highlighted_pdf_path = os.path.join(".", "static", "highlighted.pdf")
            doc.save(highlighted_pdf_path)
            doc.close()

            cloudinary.config(
                cloud_name=CLOUDINARY_CLOUD_NAME,
                api_key=CLOUDINARY_API_KEY,
                api_secret=CLOUDINARY_API_SECRET,
            )

            result = cloudinary.uploader.upload(
                highlighted_pdf_path,
                public_id="highlighted.pdf",
                resource_type="raw",
            )

            temp_url = result.get("secure_url")
            if not temp_url:
                raise Exception("Failed to upload file to Cloudinary")

            if os.path.exists(highlighted_pdf_path):
                os.remove(highlighted_pdf_path)

            return temp_url

        except Exception as err:
            print(f"Error occurred while highlighting PDF: {err}")
            return None
