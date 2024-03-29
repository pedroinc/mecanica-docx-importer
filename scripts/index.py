from .csv_creator import CsvCreator
import os


if __name__ == "__main__":
    # import pdb; pdb.set_trace()

    filename = os.getenv("CSV_NAME")
    docs_folder = os.getenv("DOCS_FOLDER")

    file_name = "AJJ 1198 06.01.2014.docx"

    csv_creator = CsvCreator(filename, docs_folder)
    print("creating the csv with the data.")
    csv_creator.create()
    print("csv created!")
