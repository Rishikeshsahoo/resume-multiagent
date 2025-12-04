import pymupdf
from langchain.tools import tool

@tool
def open_file(file_path: str):
    """Open a PDF file and return the document object"""
    doc = pymupdf.open(file_path)
    return doc

@tool
def read_file(file_path: str) -> str:
    """Read a PDF file and return its text content"""
    doc = pymupdf.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

@tool
def read_file_write_output(file_path: str, output_path: str):
    """Read a PDF file and write its content to an output file"""
    doc = pymupdf.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(text)
    return True