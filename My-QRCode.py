import tkinter as tk
import pyqrcode
import os

from pyqrcode import QRCode

#SAVE PNG FILE FUNCTION
def savepng():
    pathfile = os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/'), 'myqrcode.png')

    s = urlname.get()

    url = pyqrcode.create(s);

    url.png(pathfile, scale = 6)
#END SAVE PNG FILE FUNCTION

#SAVE SVG FILE FUNCTION
def savesvg():
    pathfile = os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/'), 'myqrcode.svg')

    s = urlname.get()

    url = pyqrcode.create(s);

    url.svg(pathfile, scale = 6)
#END SAVE SVG FILE FUNCTION

#GRAPHICAL SETTINGS
app = tk.Tk()
app.title("My-QRCode")
app.geometry('305x150')

tk.Label(app, text="Enter URL:").grid(column=0, row=0)

urlname = tk.StringVar()
tk.Entry(app, textvariable=urlname, width=50).grid(column=0, row=1)

tk.Label(text="").grid(column=0, row=2)

tk.Button(app, text="Download PNG", width=30, command=savepng).grid(column=0, row=3)

tk.Label(text="").grid(column=0, row=4)

tk.Button(app, text="Download SVG", width=30, command=savesvg).grid(column=0, row=5)

app.mainloop()
#END GRAPHICAL SETTINGS