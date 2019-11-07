# python script to resize all images inside the current folder to 1/2 of the original size and export it to ./resized as .jpg in 80% quality.
# author: CountablyInfinite

from PIL import Image
import os

path=os.path.dirname(os.path.abspath(__file__))
resize_ratio = 0.5  # 0.5 for half the size, 2 to double the size

def resize_images():
    dirs = os.listdir(path)
    for item in dirs:
        file_path = path+"\\"+item
        # check if it is a file
        if os.path.isfile(file_path):
            # extract extension and convert it to lowercase
            ext = os.path.splitext(file_path)[-1].lower()
            if ext == ".jpg":
                try:
                    image = Image.open(file_path)
                    new_image_height = int(image.size[0] / (1/resize_ratio))
                    new_image_length = int(image.size[1] / (1/resize_ratio))
                    image = image.resize((new_image_height, new_image_length), Image.ANTIALIAS)
                    # try to create directory "resized"
                    if not os.path.isdir(path+"\\"+"resized"):
                        try:
                            os.mkdir(path+"\\"+"resized")
                        except OSError:
                            print ("Creation of the directory %s failed" % (path+"\\"+"resized"))
                    # save file to new directory "resized" with 80% quality
                    image.save(path +"\\resized\\"+ item, 'JPEG', quality=80)
                except Exception as e:
                    print ("Failed opening image. Error:" +str(e))     
resize_images()