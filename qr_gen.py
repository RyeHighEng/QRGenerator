import qrcode
from PIL import Image
import myconfig

def generateQR(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('qr.png')
    img = Image.open('qr.png')
    img.show()

createWIFI_string = "WIFI:S:" + myconfig.mySSID + ";T:" + myconfig.encryption + ";P:" + myconfig.password + ";;"
generateQR(createWIFI_string)
