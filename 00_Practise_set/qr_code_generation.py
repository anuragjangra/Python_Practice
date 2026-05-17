import qrcode
# Create a QR code object
url = input("Enter the URL to generate QR code: ")
filename = input("Enter the filename to save the QR code (without extension): ")
if not (filename.endswith(".png")):
    filename += ".png"
    
img = qrcode.make(url)
img.save(filename)