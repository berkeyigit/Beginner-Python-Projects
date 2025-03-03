import qrcode
import tkinter as tk
from PIL import Image, ImageTk

def generate():
    url = entry.get()
    if not url:
        return
    
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10,  
        border=4 
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill="black", back_color="white")
    qr_image.show()
    qr_image.save("qrcode.png")

    img = Image.open("qrcode.png")
    img = ImageTk.PhotoImage(img)
    qr_label = tk.Label(root, image=img).pack()
    qr_label.image = img

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x200")

descrioption = tk.Label(root, text="Enter URL").pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Generate QR Code", command=generate)
button.pack()

qr_label = tk.Label(root)
qr_label.pack

root.mainloop()