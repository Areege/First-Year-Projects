#Code developed by Areege Chaudhary (10197607): October 26, 2015

#prompt user to input their name and the size of their USB drive
name=input('Please enter your name:')
print('Hello', name + ',', 'please enter your USB drive size in GB:')
drive_size=int(input())
#calculate the size of different image file types with a 800x600 pixels resolution
GIF_size=int(800*600/5)
JPEG_size=int(800*600*2/25)
PNG_size=int(800*600*3/8)
TIFF_size=int(800*600*4)
#calcuate how many image files can fit on the USB depending on their file type
GIF_fit=1000000000*drive_size//GIF_size
JPEG_fit=1000000000*drive_size//JPEG_size
PNG_fit=1000000000*drive_size//PNG_size
TIFF_fit=1000000000*drive_size//TIFF_size
#output the data to the user
print('Your', drive_size, 'GB USB drive can store:')
print(format(GIF_fit, '>40'), 'images in GIF format')
print(format(JPEG_fit, '>40'), 'images in JPEG format')
print(format(PNG_fit, '>40'), 'images in PNG format')
print(format(TIFF_fit, '>40'),'images in TIFF format')


