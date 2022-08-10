import qrcode

print("-QRCODE GENERATOR-")
print("Created By Rauf Endro Widagdo")

link = input("Masukkan link : ")
if link != None :
    img = qrcode.make(link)
    type(img)
    img.save("qr.png")
    print("QRCODE sudah jadi (qr.png)")
else :
    print("Link belum diisi")
