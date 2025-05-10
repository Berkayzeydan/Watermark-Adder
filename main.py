from tkinter import *
from PIL import Image, ImageTk
import os



def get_watermark():
    for logo in os.listdir("logo/"):
        if logo.lower().endswith((".png", ".jpg", ".jpeg")):
            logo_path = os.path.join("logo", logo)
            logo_to = Image.open(logo_path)
            sym = logo_to.convert("RGBA")
            datas = sym.getdata()
            new_data = []
            for item in datas:
                r, g, b, a = item
                if r < 30 and g < 30 and b < 30:
                    new_data.append((r, g, b, 100))
                else:
                    new_data.append(item)

            sym.putdata(new_data)
            return sym.resize((75,75))
    return None

def get_image():
    image_files = os.listdir("image/")
    for file in image_files:
        if file.lower().endswith((".png", ".jpg", ".jpeg")):

            img_path = os.path.join("image", file)
            img_to = Image.open(img_path)
            return img_to
    return None


def open_img_logo():

    img_to = get_image()
    logo_to = get_watermark()

    if logo_to is None or img_to is None:
        start_button.configure(text="Add Logo and Image First")
        return

    def add_logo(a):
        wm = ImageTk.PhotoImage(logo_to)
        canvas.create_image(a.x, a.y, image=wm)
        if not hasattr(canvas, "logos"):
            canvas.logos = []
        canvas.logos.append(wm)

    instructions = Label(text="Press wherever you want the watermarks and when you are done take a screenshot of the canvas to save the picture!")
    instructions.pack()
    img = ImageTk.PhotoImage(img_to)
    canvas = Canvas(window, height=img.height(), width=img.width())
    canvas.pack()
    canvas_image = canvas.create_image(img.width()/2, img.height()/2, image=img)
    canvas.image = img

    start_button.configure(command=quit, text="End")
    canvas.bind("<Button-1>", add_logo)



window = Tk()
start_button = Button(window, command=open_img_logo, width=50, height=2, text="Push button to use the image")
start_button.pack()


window.mainloop()
