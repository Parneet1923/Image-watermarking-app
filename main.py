import tkinter
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import ttk, filedialog


def open_img_file():
    global f
    filetypes = (
        ('jpg', '*.jpg'),
        ('png', '*.png'),
        ('All files', '*.*')
    )
    f = filedialog.askopenfilename(filetypes=filetypes)
    image_display()


def image_display():
    image = ImageTk.PhotoImage(Image.open(f).resize((600, 600)))
    img_label.config(image=image)
    img_label.image = image


def draw_watermark():
    watermark_image = Image.open(f)
    img_height = watermark_image.height
    img_width = watermark_image.width
    size = int(img_width/8)
    font = ImageFont.truetype("arial.ttf", size)
    draw = ImageDraw.Draw(watermark_image)
    draw.text(xy=(460, 450), text=text_input.get(), fill=(255,255,255), font=font, anchor='mm')
    image = ImageTk.PhotoImage(watermark_image.resize((600, 600)))
    img_label.config(image=image)
    img_label.image = image


window = Tk()
style = ttk.Style()
window.title("Image Watermarking")
window.config(width=1200, height=600)
default_image = ImageTk.PhotoImage(Image.open('image/download.png').resize((600, 600)))
img_label = ttk.Label(image=default_image)
img_label.image = default_image
img_label.grid(row=0, column=0, rowspan=20)
open_img = ttk.Button(window, text="Open Image", command=open_img_file)
open_img.grid(row=18, column=1)
text_label = ttk.Label(window, text="Watermark Text", font=('Arial', 14, 'normal'), padding=5)
text_label.focus_set()
text_label.grid(row=0, column=1)
text_input = ttk.Entry(window)
text_input.grid(row=1, column=1)
draw_button = ttk.Button(window, text="Draw Watermark", command=draw_watermark)
draw_button.grid(row=2, column=1)


tkinter.mainloop()

