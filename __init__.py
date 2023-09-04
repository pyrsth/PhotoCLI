from PIL import image
from rembg import remove

def removebg(address,output):
    input_path=address
    output_path=output
    inp=Image.open(input_path)
    output=remove(inp)
    output.save(output_path)

def rmexif(address):
    image = Image.open(address)
    # next 3 lines strip exif
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save('image_file_without_exif.jpeg')

    # as a good practice, close the file handler after saving the image.
    image_without_exif.close()
def help():
    print("rmbg      Remove background photos and convert to PNG format.")
    print("rmexif    Remove exif(photo data).")
    print("?         Show this output.")
    print("version   Show version abd more about for this program")
ps=input("enter command:(or ? for help)")
print("Wellcome to PhotoCLI!")

if ps=="rmbg":
    adress_inp=input("Enter a photo address: ")
    oupt_inp=input("Enter output  address:(Just png. lake.png,etc) ")
    removebg(adress_inp,oupt_inp)
    print("Photo background is removed ")
elif ps=="rmexif":
    exphotoaddress=input("Enter a photo address:")
    rmeixf(exphotoaddress)
    print("Photo exif is removed")
elif ps=="?":
    help()
elif ps=="version":
    print("PhotoCLI v0.01 alpha","\n","Taha Mokhtary HashemAbad <taha490mokh@gmail.com>","\n","GPLv2")
else:
    help()
