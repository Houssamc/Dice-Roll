import random
from tkinter import *
from PIL import ImageTk, Image

# create window
window = Tk()
window.geometry("650x500")
window.title('Dice Roll')

# picture label and grid
img = Image.open('dicee.jpg')
img = img.resize((350, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)
img_label = Label(window, image=photo)
img_label.grid(row=0, column=0, padx=150, pady=10, sticky='w')
img_label.image = photo

# label for dice roll
label = Label(window, font=("times", 200))

# dice roll function
def dice_roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.config(text=f'{random.choice(number)}{random.choice(number)}')
    label.grid(row=2, column=0)

# button and grid location
button = Button(window,text="Roll Dice", font=('comic sans', 20, 'bold'),command=dice_roll)
button.grid(row=1, column=0, padx=250, sticky='w')

# run main loop
window.mainloop()