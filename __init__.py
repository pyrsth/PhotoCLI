from PIL import Image
from rembg import remove
def removebg(address,output):
    input_path=address
    output_path=output
    inp=Image.open(input_path)
    output=remove(inp)
    output.save(output_path)
print("Wellcome to PhotoCLI!")
adress_inp=input("Enter a address image: ")
oupt_inp=input("Enter output  address:(Just png. lake.png,etc) ")
removebg(adress_inp,oupt_inp)
print("Background image is removed in", oupt_inp)