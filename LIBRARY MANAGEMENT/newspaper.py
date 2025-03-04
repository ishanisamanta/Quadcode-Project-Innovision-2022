import requests
import json
from bs4 import BeautifulSoup
from PIL import Image
import os
import img2pdf
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkcalendar import Calendar, DateEntry
import datetime


file_name = ''
finaltime = ''
dt_stamp = ''
newspaper_name = ''


def get_pageno(date, month, year, name):
    global newspaper_name

    r = requests.get(
        # f"https://epaper.anandabazar.com/calcutta/{year}-{month}-{date}/71/Page-1.html")
        # f"https://epaper.telegraphindia.com/calcutta/{year}-{month}-{date}/71/Page-1.html")
        f"https://epaper.{name}.com/calcutta/{year}-{month}-{date}/71/Page-1.html")

    # If this line causes an error, run 'pip install html5lib'
    soup = BeautifulSoup(r.content, 'html5lib')
    text = soup.find('input', attrs={'id': 'totalpages'})

    page_no = int(text['value'])
    # print(page_no)

    spin_box.config(to=page_no)

    newspaper_name = name


def get_paper():

    global file_name
    global finaltime
    global dt_stamp
    # print(spin_box.get())
    name = get_word()

    # url = f"https://epaper.anandabazar.com/epaperimages////{finaltime}////{finaltime}-md-hr-"
    # url = f"https://epaper.telegraphindia.com/epaperimages////{finaltime}////{finaltime}-md-hr-"
    url = f"https://epaper.{name}.com/epaperimages////{finaltime}////{finaltime}-md-hr-"

    # print(url)

    lst = []
    for i in range(1, int(spin_box.get())+1):
        lst.append(url+f"{i}ll.png")
    # print(lst)

    with open(f"{file_name}/{dt_stamp} {name}.pdf", "wb") as f:
        f.write(img2pdf.convert([requests.get(i).content for i in lst]))

    statuslbl.configure(text='Download Completed 🔥. Thank 🙏 you for using.')


def select_date(name):

    global finaltime
    get_dat = str(cal.get_date()).split('-')
    final_date = get_dat[-1]
    final_month = get_dat[1]
    final_year = get_dat[0]

    finaltime = final_date+final_month+final_year

    global dt_stamp
    dt_stamp = datetime.datetime(
        int(final_year), int(final_month), int(final_date))
    dt_stamp = dt_stamp.strftime('%d %B, %Y')

    get_pageno(final_date, final_month, final_year, name)


def select_location():
    global file_name
    file_name = filedialog.askdirectory(
        initialdir='Desktop', title='Select Directory')
    dwnlocbtn.configure(text=f'{file_name}')


def get_word():
    return newspaper_name


# Driver Code
if __name__ == "__main__":

    # create a instance root
    root = Tk()
    # Set Title, geometry
    root.title("Bengali E-Newspaper")
    root.geometry("500x500")
    root.resizable(False, False)

    # create the style widget, configure and map
    style = ttk.Style()
    style.configure("R.TLabel", foreground="Red", font="{Courier New}")
    style.configure("N.TLabel", foreground="navy", font="{Courier New}")
    style.configure("C.TButton", font="{Courier New}")
    style.map("C.TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[
              ('pressed', '!disabled', 'yellow'), ('active', 'green')])

    # Create a heading Frame
    headingfrm = LabelFrame(root,)
    headingfrm.pack(side='top', fill='both')

    # create a heading label
    heading_lbl = ttk.Label(
        headingfrm, text="Welcome To the Bengali E-Newspaper App", style='R.TLabel')
    heading_lbl.pack(pady=10)

    # Create a body Frame
    bodyfrm = Frame(root)
    bodyfrm.pack(fill='both')

    # Create 'Choose date' label
    chslbl1 = ttk.Label(bodyfrm, text='Select Date', style="N.TLabel")
    chslbl1.pack(pady=10)

    # set min date and max date for calender widget
    mindate = datetime.date(year=2021, month=1, day=1)
    maxdate = datetime.date.today()

    # create calender widget
    cal = DateEntry(bodyfrm, width=15, background='darkblue',
                    foreground='white', borderwidth=2, mindate=mindate, maxdate=maxdate)
    cal.pack(padx=10, pady=5)

    frame = Frame(bodyfrm)
    frame.pack(fill='both')

    # Craete a telegraph button
    telegraph = ttk.Button(frame, text="Telegraph",
                           command=lambda: select_date('telegraphindia'), style="C.TButton")
    # telegraph.pack(pady=20)
    telegraph.grid(row=0, column=1, pady=20, padx=70)

    # Craete a anandabazar button
    anandabazar = ttk.Button(frame, text="Anandabazar",
                             command=lambda: select_date('anandabazar'), style="C.TButton")
    # anandabazar.pack(pady=20)
    anandabazar.grid(row=0, column=2, pady=20)

    # Create Choose page label
    chslbl2 = ttk.Label(bodyfrm, text='Select Upto Page', style="N.TLabel")
    chslbl2.pack(pady=10)

    # Craete spin box for page number selection and set its default value
    spin_box = ttk.Spinbox(bodyfrm, from_=1, to=2, wrap=True)
    spin_box.set(1)
    spin_box.pack()

    # print(spin_box.get())

    # Create Choose Downlod Location Button
    dwnlocbtn = ttk.Button(bodyfrm, text="Select Download Location",
                           command=select_location, style="C.TButton")
    dwnlocbtn.pack(pady=20)

    # Add Download Button
    dwnbtn = ttk.Button(bodyfrm, text="Download",
                        command=get_paper, style="C.TButton")
    dwnbtn.pack(pady=20)

    # Create a status bar LabelFrame
    statusfrm = LabelFrame(root, text='Status Bar', font='Arial 15')
    statusfrm.pack(side='bottom', fill='both')

    # craete a status label
    statuslbl = ttk.Label(statusfrm, text="Tips 🤫 Press 'q' for Exit.",
                          font='{Courier New} 13', style='N.TLabel')
    statuslbl.pack(ipady=5)

    # Binding 'q' key for exit
    root.bind('q', exit)

    # call the mainloop of the root instances
    root.mainloop()
