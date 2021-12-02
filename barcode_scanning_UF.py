from tkinter import *
import pandas as pd
import numpy as np
import datetime as dt

file = open(
    'Z:\\1. QA\\99. Personal Folders\\Dylan Vantine\\General\\UF Barcode Info.txt', 'r')
df = pd.read_csv(file, sep='\t', index_col=False,
                 parse_dates={'DT': ['Date', 'Time']})
df = df.drop_duplicates(subset=['Barcode', 'DT'], keep='first')

root = Tk()
root.geometry('500x250')
root.resizable(0, 0)


barcode = 0


def get_dat(col, barcode):
    tire_info = df.loc[df['Barcode'] == barcode]
    if tire_info.shape[0] != 0:
        if tire_info.shape[0] > 1:
            tire_info = tire_info.loc[tire_info['DT'] == tire_info['DT'].max()]
        return tire_info[col].item()
    else:
        return 'N/A'


def ins_cnt(barcode):
    tire_info = df.loc[df['Barcode'] == barcode]
    return tire_info.shape[0]


def check(barcode):
    barcode = int(input_box.get())
    input_box.delete(0, END)
    bc_value.config(text=barcode)
    ins_date_value.config(text='Ins Date: ' +
                          str(get_dat('DT', barcode)))
    MC_value.config(text='M/C: ' + str(get_dat('M/C', barcode)))
    sort_value.config(text='Ins. Sort: ' +
                      str(get_dat('Ins. Sort', barcode)))
    cnt_value.config(text='Ins. Count: ' +
                     str(get_dat('Inspection Cnt.', barcode)))
    CON_value.config(text='CON: ' + str(get_dat('CON', barcode)))
    RFVa_value.config(text='RFV Angle: ' +
                      str(get_dat('RFV ANG', barcode)))
    HARa_value.config(text='HAR Angle: ' +
                      str(get_dat('R1H ANG', barcode)))
    grade_value.config(text='UF Grade: ' +
                       str(get_dat('Grade', barcode)))
    spec_value.config(text='Spec: ' + str(get_dat('SPEC', barcode)))


input_frame = Frame(root, width=330, height=50, bd=0,
                    highlightbackground='black', highlightthickness=1)
input_frame.pack(side=TOP, pady=5, padx=5)

input_box = Entry(input_frame, font=18,
                  textvariable=barcode, width=340, bg="#eee",
                  bd=0, justify=CENTER)
input_box.pack(pady=5)

bc_frame = Frame(root, highlightbackground='black', highlightthickness=1)
bc_frame.pack(pady=5, padx=5)
frame3 = Frame(root, bd=0, highlightbackground='black', highlightthickness=1)
frame3.pack(pady=5, padx=5)
frame1 = Frame(root, highlightbackground='black', highlightthickness=1)
frame1.pack(pady=5, padx=5)
frame2 = Frame(root, bd=0, highlightbackground='black', highlightthickness=1)
frame2.pack(pady=5, padx=5)


bc_value = Label(bc_frame, text='-', font=('ariel', 30, 'bold'))
ins_date_value = Label(frame1, text='Ins Date:     -     ')
MC_value = Label(frame1, text='M/C:   -   ')
sort_value = Label(frame1, text='Ins. Sort:      -    ')
cnt_value = Label(frame1, text='Ins. Count:  -  ')
CON_value = Label(frame2, text='CON:  -  ')
RFVa_value = Label(frame2, text='RFV Angle:  -  ')
HARa_value = Label(frame2, text='HAR Angle:  -  ')
grade_value = Label(frame2, text='Grade: - ')
spec_value = Label(
    frame3, text='Spec:                            -                             ')

bc_value.grid(row=1, column=1, pady=3)
ins_date_value.grid(row=1, column=1, pady=3)
MC_value.grid(row=1, column=2, pady=3, padx=5)
sort_value.grid(row=1, column=3, pady=3, padx=5)
cnt_value.grid(row=1, column=4, pady=3, padx=5)
CON_value.grid(row=1, column=1, pady=3, padx=5)
RFVa_value.grid(row=1, column=2, pady=3, padx=5)
HARa_value.grid(row=1, column=3, pady=3, padx=5)
grade_value.grid(row=1, column=4, pady=3, padx=5)
spec_value.pack(pady=3)


input_box.focus()

root.bind('<Return>', check)

root.mainloop()
