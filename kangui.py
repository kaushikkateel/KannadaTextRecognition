
#  Created by Kaushik Kateel on 4/05/19.
#  Copyright © 2019 Kaushik Kateel. All rights reserved.

import os
import tkinter as tk
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 1000

data =str()
root = tk.Tk(className=' KANNADA TEXT ANALYSER')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,)
canvas.pack()

frame = tk.Frame(root, bg='#339cff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1) 



def xd():
    e = entry.get()
    play(e)

button1 = tk.Button(frame, text="Upload", font=40, command=xd)
button1.place(relx=0.7, relheight=1, relwidth=0.1)

def yd():
	printt()

button2 = tk.Button(frame, text="Get data", font=40, command=yd)
button2.place(relx=0.81, relheight=1, relwidth=0.15)

lower_frame = tk.Frame(root, bg='#339cff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.7, anchor='n')
def play(e):
	
	cmdIn = "tesseract "+str(e)+" output -l kan --oem 1 --psm 3"
	print(cmdIn)
	os.popen(cmdIn)


	
def printt():
	data=str()
	f=open("C:\\Users\\bhatk\\output.txt", encoding = "utf8")
	data = f.read()
	f.close()
	label = tk.Label(lower_frame, bd=3, text=data, bg='#cce6ff', fg='#000000')
	label.place(relx=0.0,rely=0.0, relheight=1, relwidth=1)
	label.config(font = ("Courier",12))
root.mainloop()

