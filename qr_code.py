### pip install qrcode pillow
# qrcode: This library lets us perform all of our QR code related operations
# pillow: This library helps us process and save images

import qrcode
# We just need to import qrcode, because pillow is implicitly imported.

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
#The version parameter is an integer from 1 to 40 that controls the size of the QR code.
#The box_size parameter controls how many pixels each “box” of the QR code is.
#The border parameter controls how many boxes thick the border should be.

#Then, the data (specifically, the link we specified before) is added to the QR code, using .add_data(). 
#The QR code is then generated using .make():
qr.add_data(website_link)
qr.make()

#Finally, we save this created QR code in an img pillow object using qr.make_image():
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('youtube_qr.png')