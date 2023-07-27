import PyPDF2

import os

import re



class ELibrary:

    def __init__(self):

        self.books_directory = "books"

        self.books = []

        self.selected_book = None

        

        self.load_books()

        

    def load_books(self):

        book_files = os.listdir(self.books_directory)

        for book_file in book_files:

            if book_file.endswith(".pdf"):

                book_path = os.path.join(self.books_directory, book_file)

                book_name = self.get_book_title(book_path)

                self.books.append({"name": book_name, "path": book_path})

                

    def get_book_title(self, book_path):

        with open(book_path, 'rb') as f:

            pdf_reader = PyPDF2.PdfFileReader(f)

            title = pdf_reader.getDocumentInfo().title

            if not title:

                title = os.path.basename(book_path).replace(".pdf", "")

            return title

            

    def select_book(self, book_index):

        self.selected_book = self.books[book_index]

            

    def search_books(self, query):

        results = []

        for book in self.books:

            book_title = book['name']

            if re.search(query, book_title, re.IGNORECASE):

                results.append(book)

        return results

            

e_library = ELibrary()

