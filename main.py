from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests
from bs4 import BeautifulSoup

searchOptions = ['Page name', 'Category name']


def clean(uncleanUrl):
    nameString = "https://" + str(uncleanUrl)
    return nameString


def ping(url, pagename):
    try:
        if "https://" in url:
            page = requests.get(str(url) + "/wiki/" + str(pagename), timeout=1)
            return page
        else:
            newUrl = clean(url)
            page = requests.get(str(newUrl + "/wiki/" + str(pagename)), timeout=1)
            return page
    except Exception as e:
        ConnectionNotFound_errorWindow = tk.Toplevel(mainCompartment)
        ConnectionNotFound_errorWindow.geometry('450x150')
        ConnectionNotFound_errorWindow.title('Connection Error')
        Label(ConnectionNotFound_errorWindow, text='Connection Error. Please double check URL and try again.').place(
            x=50, y=70)
        Button(ConnectionNotFound_errorWindow, text="Close", command=ConnectionNotFound_errorWindow.destroy).place(
            x=205, y=110)
        print(e)


def search(wikiname, searchtype, pagename):
    newpage = ping(wikiname, pagename)
    newSoup = BeautifulSoup(newpage.content, 'html.parser')


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
    submitBtn = Button(mainCompartment, text='Run Page Scraping',
                       command=lambda: search(wikiname=urlString.get(), searchtype=entryBox.get(),
                                              pagename=pageString.get()))
    submitBtn.place(x=105, y=200)

    # begin ui
    mainCompartment.mainloop()
