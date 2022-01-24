from tkinter import *
import pandas as pd
import numpy as np
import datetime as dt

individual_file = open(
    'Z:\\1. QA\\99. Personal Folders\\Dylan Vantine\\General\\Individual Hold Data.txt', 'r')
range_file = open(
    'Z:\\1. QA\\99. Personal Folders\\Dylan Vantine\\General\\Range Hold Data.txt', 'r')
individual_df = pd.read_csv(individual_file, sep='\t', index_col=False)
range_df = pd.read_csv(range_file, sep='\t', index_col=False)
# df = df.drop_duplicates(subset=['Barcode', 'DT'], keep='first')

root = Tk()
# root.geometry('500x250')
root.resizable(0, 0)

barcode = 0


def get_dat(col, barcode):

    range_info = range_df.loc[(range_df['Barcode Start'] <= barcode) & (
        range_df['Barcode End'] >= barcode)]
    if range_info.shape[0] != 0:
        global hold_type
        hold_type = 'Range'
        if pd.isna(range_info[col].item()):
            return 'N/A'
        else:
            return range_info[col].item()
    else:
        tire_info = individual_df.loc[individual_df['Barcode'] == barcode]
        if tire_info.shape[0] != 0:
            hold_type = 'Individual'
            if pd.isna(tire_info[col].item()):
                return '-'
            else:
                return tire_info[col].item()
        else:
            hold_type = 'No Holds Barred'
            return 'N/A'


def check(barcode):
    barcode = int(input_box.get())
    input_box.delete(0, END)
    bc_value.config(text=barcode)
    # cure_date_value.config(text='Cure Date: ' +
    #    str(get_dat('Curing Date&Time', barcode)))
    spec_value.config(text='Spec: ' + str(get_dat('Spec', barcode)))
    hold_type_value.config(
        text='Hold Type: ' + hold_type)
    hold_app_value.config(
        text='Hold Apply?: ' + str(get_dat('Hold Apply', barcode)))
    hold_reason_value.config(text='Hold Reason: ' +
                             str(get_dat('Hold Reason', barcode)))
    registrant_value.config(text='Registrant: ' +
                            str(get_dat('Registrant', barcode)))
    registered_date_value.config(
        text='Hold Register Date: ' + str(get_dat('Registered Date&Time', barcode)))
    if hold_type == 'Individual':
        NCF_value.config(text='NCF Code: ' +
                         str(get_dat('NCF Code', barcode)))
        NCF_reg_date_value.config(text='NCF Date: ' +
                                  str(get_dat('NCF Date&Time', barcode)))
    # extra_2.config(text='extra_2: ' + str(get_dat('extra_2', barcode)))
    # extra_3.config(text='extra_3: ' + str(get_dat('extra_3', barcode)))
    # extra_4.config(text='extra_4: ' + str(get_dat('extra_4', barcode)))


input_frame = Frame(root, width=330, height=50, bd=0,
                    highlightbackground='black', highlightthickness=1)
input_frame.pack(side=TOP, pady=5, padx=5)

input_box = Entry(input_frame, font=18,
                  textvariable=barcode, width=35, bg="#eee",
                  bd=0, justify=CENTER)
input_box.pack(pady=5)

bc_frame = Frame(root, highlightbackground='black', highlightthickness=1)
bc_frame.pack(pady=5, padx=5)
frame1 = Frame(root, highlightbackground='black', highlightthickness=1)
frame1.pack(pady=5, padx=5)
frame2 = Frame(root, bd=0, highlightbackground='black', highlightthickness=1)
frame2.pack(pady=5, padx=5)
frame3 = Frame(root, bd=0, highlightbackground='black', highlightthickness=1)
frame3.pack(pady=5, padx=5)
extraframe = Frame(root, bd=0, highlightbackground='black',
                   highlightthickness=1)
extraframe.pack(pady=5, padx=5)

bc_value = Label(bc_frame, text='-', font=('ariel', 30, 'bold'))
spec_value = Label(
    frame1, text='Spec:                            -                             ')
# cure_date_value = Label(frame1, text='Cure Date:           -           ')
hold_app_value = Label(frame3, text='Hold Apply?:   -   ')
registrant_value = Label(frame2, text='Registrant:  -  ')
registered_date_value = Label(
    frame2, text='Hold Register Date:          -          ')
hold_reason_value = Label(
    frame3, text='Hold Reason:                                 -                                  ')
NCF_value = Label(extraframe, text='NCF:  -  ')
NCF_reg_date_value = Label(extraframe, text='NCF Date:          -          ')
hold_type_value = Label(frame3, text='Hold Type:   -   ')
# extra2_value = Label(extraframe, text='extra2:  -  ')
# extra3_value = Label(extraframe, text='extra3:  -  ')
# extra4_value = Label(extraframe, text='extra4:  -  ')

bc_value.grid(row=1, column=2, pady=3)
# cure_date_value.grid(row=1, column=2, pady=3)
hold_app_value.grid(row=1, column=2, pady=3, padx=5)
hold_reason_value.grid(row=1, column=3, pady=3, padx=5)
registrant_value.grid(row=1, column=3, pady=3, padx=5)
registered_date_value.grid(row=1, column=1, pady=3, padx=5)
NCF_value.grid(row=1, column=2, pady=3, padx=5)
NCF_reg_date_value.grid(row=1, column=3, pady=3, padx=5)
spec_value.grid(row=1, column=1, pady=3)
hold_type_value.grid(row=1, column=1, pady=3, padx=5)
# extra2_value.grid(row=1, column=2, pady=3, padx=5)
# extra3_value.grid(row=1, column=3, pady=3, padx=5)
# extra4_value.grid(row=1, column=4, pady=3, padx=5)


input_box.focus()

root.bind('<Return>', check)

root.mainloop()
