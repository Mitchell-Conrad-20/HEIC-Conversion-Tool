from PIL import Image
from pillow_heif import register_heif_opener
import os

register_heif_opener()

folder = input("Paste absolute source path: ")

try:
    os.mkdir(os.path.join(folder, "Converted"))
except:
    pass

documents = os.listdir(folder)

for doc in documents:
    if doc.endswith(".heic"):
        print("Converting " + doc)
        path = folder + "\\" + doc
        image = Image.open(path)
        image.convert('RGB').save(folder + "\\Converted\\" + doc[:-4] + "jpg")