#-------------------------------------------------------------------------------
# Author:      sumit.khandelwal
# Created:     14/10/2019
# Copyright:   (c) sumit.khandelwal 2019
#-------------------------------------------------------------------------------
from googletrans import Translator # Import Translator modules from googletrans
translator = Translator() # Craete an object og translator modules
# TKinter GUI structure for User Interaction
import tkinter as tk
# Function for Hindi
def show_entry_hindi():
    translated = translator.translate(str(e1.get()), src='en', dest='hi')
    labelResult.config(text="After Translation the result is :  %s " % translated.text)
# Function for Marathi
def show_entry_marathi():
    translated = translator.translate(str(e1.get()), src='en', dest='mr')
    labelResult.config(text="After Translation the result is :  %s " % translated.text)
# Function for Gujrati
def show_entry_gujrati():
    translated = translator.translate(str(e1.get()), src='en', dest='gu')
    labelResult.config(text="After Translation the result is :  %s " % translated.text)
# You can add many function as per requirments (Just change the destination language code)
master = tk.Tk()
#acc = accuracy
master.title('Language Translator')
master.geometry('900x400+100+200')
tk.Label(master, text="Enter Your Sentense : ").grid(row=0)
e1 = tk.Entry(master)
e1.grid(row=0, column=1)
labelResult = tk.Label(master)
labelResult.grid(row=10, column=2)
tk.Button(master,text='Quit',command=master.quit, bg="red").grid(row=6, column=0, sticky=tk.W,pady=4)
tk.Button(master,text='Hindi', command=show_entry_hindi).grid(row=6,column=1,sticky=tk.W,pady=4)
tk.Button(master,text='Marathi', command=show_entry_marathi).grid(row=6,column=2,sticky=tk.W,pady=4)
tk.Button(master,text='gujrati', command=show_entry_gujrati).grid(row=7,column=0,sticky=tk.W,pady=4)
tk.mainloop()


