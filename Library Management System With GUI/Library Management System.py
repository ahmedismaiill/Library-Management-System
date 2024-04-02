from tkinter import *
import csv
class Book:

    def __init__(self,title, author, genre,publication_year):
        self._title = title
        self._author = author
        self._genre = genre
        self._publication_year = publication_year

    def _set_title(self, title):
        self._title = title

    def _display_title(self):
        return self._title

    def _set_author(self, author):
        self._author = author

    def _display_author(self):
        return self._author

    def _set_genre(self, genre):
        self._genre = genre

    def _display_genre(self):
        return self._genre

    def _set_publication_year(self, publication_year):
        self._publication_year = publication_year

    def _display_publication_year(self):
        return self._publication_year

class library(Book):



    def __init__(self):
        self.__book = []

    def add_book(self,Book):
        self.__book.append(Book)

    def remove_book_by_title(self, title):
        for book in self.__book:
            if title == book._display_title():
                self.__book.remove(book)
                text.insert(INSERT,f"Book with title '{title}' has been removed.\n")
                return
        text.insert(INSERT,f"Book with title '{title}' not found in the library.\n")

    def search_book_title(self,title):
        f = 0
        for Book in self.__book:
            if title == Book._display_title():
                f = 1
                break
        if f == 1:
            text.insert(INSERT,f"{title} Is Here \n")
        else:
            text.insert(INSERT,f"{title} Is Not Here \n")

    def search_book_author(self,author):
        f = 0
        for Book in self.__book:
            if author == Book._display_author():
                f = 1
                break
        if f == 1:
            text.insert(INSERT,f"{author} Is Here \n")
        else:
            text.insert(INSERT,f"{author} Is Not Here \n")

    def display_library(self):
        count = 1
        if len(self.__book) == 0:
            text.insert(INSERT,"Library is empty\n")
        else:
            for book in self.__book:
                book_info = f"{book._title}\t\t{book._author}\t\t{book._genre}\t\t{book._publication_year}\n"
                text.insert(INSERT, book_info)

    def save_to(self,filename):
        with open(filename,'w') as file:
            w = csv.writer(file)
            for book in self.__book:
                w.writerow([book._title,book._author,book._genre,book._publication_year])

    def load_from(self,filename):
        try:
            with open(filename,'r') as file:
                r = csv.reader(file)
                for row in r:
                    title,author,genre,publication_year = row
                    book = Book(title,author,genre,publication_year)
                    self.__book.append(book)
                text.insert(INSERT,"Library loaded Successfuly\n")
        except FileNotFoundError:
            text.insert(INSERT,"File is Not Found\n")
        except Exception as e:
            text.insert(INSERT,f"Error Is {e}\n")

l = library()

def add():
    title = enrty_add_title.get()
    enrty_add_title.delete(0,END)
    author = enrty_add_author.get()
    enrty_add_author.delete(0,END)
    genre = enrty_add_genre.get()
    enrty_add_genre.delete(0,END)
    publication_year = enrty_add_year.get()
    enrty_add_year.delete(0,END)
    book = Book(title,author,genre,publication_year)
    l.add_book(book)

def load():
    filename = entry_load.get()
    entry_load.delete(0,END)
    l.load_from(filename)

def save():
    filename = entry_save.get()
    entry_save.delete(0,END)
    l.save_to(filename)

def remove_title():
    title = enrty_remove_title.get()
    enrty_remove_title.delete(0, END)
    l.remove_book_by_title(title)

def search_title():
    title = enrty_search_title.get()
    enrty_search_title.delete(0,END)
    l.search_book_title(title)

def search_author():
    author = enrty_search_author.get()
    enrty_search_author.delete(0, END)
    l.search_book_author(author)

def display_library():
    text.delete(1.0,END)
    text.insert(INSERT,"Library Contents:\n")
    l.display_library()

def clear():
    text.delete(1.0, END)


root = Tk()
root.title("Personal Library Management System")
label_display = Label(root,text="Welcome Personal Library Management System ",font="Helvatica 20 bold")
label_display.grid(row=0)



label_title = Label(root,text="Title")
label_title.grid(row=1,column=0)

label_author = Label(root,text="Author")
label_author.grid(row=2,column=0)

label_genre = Label(root,text="Genre")
label_genre.grid(row=3,column=0)

label_year = Label(root,text="Publication Year")
label_year.grid(row=4,column=0)

enrty_add_title = Entry(root,width=40,borderwidth=5)
enrty_add_title.grid(row=1,column=1)

enrty_add_author = Entry(root,width=40,borderwidth=5)
enrty_add_author.grid(row=2,column=1)

enrty_add_genre = Entry(root,width=40,borderwidth=5)
enrty_add_genre.grid(row=3,column=1)

enrty_add_year = Entry(root,width=40,borderwidth=5)
enrty_add_year.grid(row=4,column=1)

button_add = Button(root,text="Add Book",padx=400,command=add)
button_add.grid(row=5,column=0)


button_remove_title = Button(root,text="Remove Book with title only ",padx=400,command=remove_title)
button_remove_title.grid(row=6,column=0)
enrty_remove_title = Entry(root,width=40,borderwidth=5)
enrty_remove_title.grid(row=6,column=1)

button_search_title = Button(root,text="Search Book with title only",padx=400,command=search_title)
button_search_title.grid(row=7,column=0)
enrty_search_title = Entry(root,width=40,borderwidth=5)
enrty_search_title.grid(row=7,column=1)

button_search_author = Button(root,text="Search Book with author only",padx=400,command=search_author)
button_search_author.grid(row=8,column=0)
enrty_search_author = Entry(root,width=40,borderwidth=5)
enrty_search_author.grid(row=8,column=1)

button_save = Button(root,text="Save To Write as form 'Filename.csv'",padx=400,command=save)
button_save.grid(row=9,column=0)
entry_save = Entry(root,width=40,borderwidth=5)
entry_save.grid(row=9,column=1)

button_load = Button(root,text="Load From Write as form 'Filename.csv'",padx=400,command=load)
button_load.grid(row=10,column=0)
entry_load = Entry(root,width=40,borderwidth=5)
entry_load.grid(row=10,column=1)

button_display = Button(root,text="Display Library",padx=400,command=display_library)
button_display.grid(row=11,column=0)

text = Text(root)
text.grid(row=12)

button_exit = Button(root,text="Exit",padx=140,command=exit)
button_exit.grid(row=11,column=1)

button_clear = Button(root,text="Clear The Board",padx=5,command=clear)
button_clear.grid(row=12,column=1)



root.mainloop()