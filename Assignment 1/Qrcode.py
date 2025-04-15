import qrcode
from IPython.display import Image, display

from pyzbar.pyzbar import decode
from PIL import Image



data = "Copy kr smje baghair"

qr = qrcode.QRCode(version= 1, box_size=5, border=2)

qr.add_data(data)

qr.add_data("Naananananan")

qr.make(fit=True)


img = qr.make_image(fill_color="red", back_color="yellow")

img = img.convert("RGB")

img.save("/content/qr_image.png")

display(img)

img = Image.open("/content/qr_image.png")
result = decode(img)
print(result)