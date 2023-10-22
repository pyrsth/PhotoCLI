 try : 
    from PIL import Image
except : 
    print("ERROR : PYTHON MODULE PIL NOT INSTALLED")
    import sys
    sys.exit()
try : 
    from rembg import remove
except : 
    print("ERROR : PYTHON MODULE rembg NOT INSTALLED")
try :    
    import argparse
except : 
    print("ERROR : PYTHON MODULE argparse NOT INSTALLED")

def removebg(address,output):
    input_path=address #input address image
    output_path=output #set output addres
    inp=Image.open(input_path) #open image in python
    output=remove(inp)   #remove background
    output.save(output_path)  #save Image

def rmexif(address):
       # next 3 lines strip exif
    image = Image.open(address)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save('image_file_without_exif.jpeg')
    print("Photo exif is removed")
def setquality(quality,image_path):
    image_file = Image.open(image_path)
    image_file.save("f{image_path}_changed_quality.png", quality=quality) 
## 4 lines about Create flags for programme feature
parser=argparse.ArgumentParser(description="Welcome to PhotoCLI !  PhotoCLI 0.01 alpha  Taha Mokhtary HashemAbad <taha490mokh@gmail.com> GPLv3")
parser.add_argument('-e',help="Remove exif your photo.",action='store_true',default=None)
parser.add_argument('-b',help="Remove background for your photo.",action='store_true',default=None)
parser.add_argument('--version', action='version', version='PhotoCLI 0.01 alpha,  Taha Mokhtary HashemAbad <taha490mokh@gmail.com> GPLv3')
parser.add_argument('-sq',action='store_ture',help="Set quality for your photo.",default=None)
ns = parser.parse_args()
if ns.e :#two lines of remove exif
    exphotoaddress=input("Enter a photo address: ")
    rmexif(exphotoaddress)
 
if ns.b :#3 lines of remove background
    adress_inp=input("Enter a photo address: ")
    removebg(adress_inp,f'{adress_inp}_removed_bakground.png')
    print("Photo background is removed ")
if ns.sq :
    imagepath=input("Enter address your: ")
    quality=input("Enter quality(1-100): ")
    setquality(imagepath,quality)
