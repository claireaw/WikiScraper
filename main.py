import tkinter as tk

if __name__ == '__main__':
    # create main ui
    mainCompartment = tk.Tk()

    # set ui default values
    mainCompartment.geometry('500x500')
    mainCompartment.title("WikiScraper")

    # set up ui input contents
    tk.Label(mainCompartment, text='Wiki URL').grid(row=0)
    urlenter = tk.Entry(mainCompartment).grid(row=0, column=1)

    #begin ui
    mainCompartment.mainloop()
