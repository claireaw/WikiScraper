from tkinter import *
from tkinter import ttk
import tkinter as tk

import logic

searchOptions = ['Page name', 'Category name']

if __name__ == '__main__':
    # create main ui
    mainCompartment = tk.Tk()

    # set ui default values
    mainCompartment.geometry('300x300')
    mainCompartment.title("WikiScraper")

    urlString = tk.StringVar(mainCompartment)
    pageString = tk.StringVar(mainCompartment)

    # set up ui input contents
    tk.Label(mainCompartment, text='Wiki URL:').place(x=80, y=10)
    urlEnter = tk.Entry(mainCompartment, textvariable=urlString).place(x=136, y=10)

    entryBox = ttk.Combobox(state='readonly', values=searchOptions)
    entryBox.set(searchOptions[0])
    tk.Label(mainCompartment, text='Search Type:').place(x=65, y=35)
    entryBox.place(x=138, y=35)

    tk.Label(mainCompartment, text='Page Name:').place(x=65, y=60)
    pageEnter = tk.Entry(mainCompartment, textvariable=pageString).place(x=136, y=60)

    # be sure to take input for page/category name
    submitBtn = Button(mainCompartment, text='Run Page Scraping', command=lambda: logic.search(wikiname=urlString.get(), searchtype=entryBox.get(), pagename=pageString.get()))
    submitBtn.place(x=105, y=200)

    # begin ui
    mainCompartment.mainloop()
