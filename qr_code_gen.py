#!C:\Python35\
#####################################################
# QR code generator for HBO IMEI
# by HORSE at 2016/6/25
# QR (Quick Response) code Generator for HBO's IMEI
# bugfix checklist:
# more complicated qrcode generated methonds
# qrcode image in dot/or cycle shape
# make an GUI for easy operation
# insert into table in *.doc file
# .....................................
# preconfigured env for qrcode to works on windows
# pip install Pillow /older PIL Python Image Library
# pip install qrcode
# pip qrcode command test: qrcode "just a test" > test.png
# pip install colorama
#####################################################


import qrcode


def make_qr():
    qr = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
        )
    """2016-06-25-17-06-55, IMEI:362523432423914"""
    f = open(r'./IMEI.txt')
    while True:
        line = f.readline()

        if line:
            imei = line.split()[1].split(":")[1]
            qr.add_data(imei)
            qr.make(fit=True)
            image = qr.make_image()
            image.save("./img2/%s.png" %imei)
            qr.clear()
        else:
            break

if __name__ == '__main__':
    make_qr()
