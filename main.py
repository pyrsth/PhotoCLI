from PIL import Image
from rembg import remove
import argparse
def removebg(address,output,quality):
    input_path=address #input address image
    output_path=output #set output addres
    inp=Image.open(input_path) #open image in python
    output=remove(inp)   #remove background
    output.save(output_path,quality=quality)  #save Image

def rmexif(address,quality):
       # next 3 lines strip exif
    image = Image.open(address)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save('f{address}_without_exif.jpeg',quality=quality)
    print("Photo exif is removed")
## 4 lines about Create flags for programme feature
parser=argparse.ArgumentParser(description="Welcome to PhotoCLI !  PhotoCLI 0.01 alpha  Taha Mokhtary HashemAbad <taha490mokh@gmail.com> GPLv3")
parser.add_argument('-e',help="Remove exif your photo.",action='store_true',default=None)
parser.add_argument('-b',help="Remove background for your photo.",action='store_true',default=None)
parser.add_argument('--version', action='version', version='PhotoCLI 0.01 alpha,  Taha Mokhtary HashemAbad <taha490mokh@gmail.com> GPLv3')
ns = parser.parse_args()
if ns.e :#two lines of remove exif
    exphotoaddress=input("Enter a photo address: ")
    quality2=input("Enter quality(1-100): ")
    rmexif(exphotoaddress)
    print("EXIF is removed")
if ns.b :#3 lines of remove background
    adress_inp=input("Enter a photo address: ")
    quality=input("Enter quality(1-100): ")
    removebg(adress_inp,f'{adress_inp}_removed_bakground.png')
    print("Photo background is removed ")
