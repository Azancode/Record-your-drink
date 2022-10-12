from tkinter import *
from datetime import datetime
root=Tk()
bg = PhotoImage(file=r"asset.png")
my_canvas=Canvas(root, width=825, height=529)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0,0, image=bg, anchor='nw')
my_canvas.create_text(155, 90, text='Welcome', font=('Helvetica', 50))
def close():
   root.quit()
def inf():
   now = datetime.now()
   current_time = now.strftime("%H:%M:%S")
   f=open('appinf', 'w')
   f.write('You Just Hydrated yourself' + current_time)
button1 = Button(root, text="Record a drink", command=inf)
button2 = Button(root, text="Exit", command=close)
button1_window=my_canvas.create_window(20,150, anchor='nw', window=button1)
button2_window=my_canvas.create_window(120,150, anchor='nw', window=button2)
root.mainloop()

