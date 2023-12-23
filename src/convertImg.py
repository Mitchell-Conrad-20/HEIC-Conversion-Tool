import PIL.Image
from pillow_heif import register_heif_opener
import os
from tkinter import *
from tkinter.filedialog import askdirectory

########## Globals ##########
source = ""
destination = ""

########## API ##########

# Allows Pillow to open HEIC files
register_heif_opener()

def setSource():
    global source
    source = askdirectory(title="Select Source Folder")
    global sourceText
    sourceText.set("Source: " + source)
    
def setDestination():
    global destination
    destination = askdirectory(title="Select Destination Folder")
    global destinationText
    destinationText.set("Destination: " + destination)
    
def checkSourceDestination():
    global messageText

    if(source == "" and destination == "" ):
        messageText.set("Please select source and destination folders.")
        return False
    if(source == ""):
        messageText.set("Please select a source folder.")
        return False
    if(destination == ""):
        messageText.set("Please select a destination folder.")
        return False
        
    return True
    
def convert(fileExtension):
    global messageText

    # Ensure the user selected a source and destination first  
    if(not checkSourceDestination()):
        return

    # Create a list of all documents in the source folder
    documents = os.listdir(source)
    
    converted = 0
    
    # Convert all HEIC files in the folder to the selected filetype
    for doc in documents:
        if(doc.endswith(".HEIC") or doc.endswith(".heic")):
            messageText.set("Converting " + doc)
            window.update()
            
            path = source + "\\" + doc
            
            try:
                image = PIL.Image.open(path)
            except:
                messageText.set("Error: Failed to open " + doc)
                return
            
            try:
                image.convert('RGB').save(destination + "\\" + doc[:-4] + fileExtension)
            except:
                messageText.set("Error: Failed to save " + doc[:-4] + fileExtension)
                return
            
            converted += 1
            
    messageText.set("Conversion Complete! Converted " + str(converted) + " images!")

########## VIEW ##########

# Create window
window = Tk()
window.title("HEIC Conversion Tool")
window.geometry("640x360")
window.resizable(0,0)

# Create title label
label = Label(text="HEIC Conversion Tool", font="Helvetica 12 bold")
label.pack(pady=10)

sourceSelect = Button(text="Select Source Folder", font="Helvetica 10", command=setSource)
sourceSelect.pack(pady=10)

sourceText = StringVar()
sourceText.set("Source: None")
currentSource = Label(textvariable=sourceText, font="Helvetica 10")
currentSource.pack(pady=10)

destinationSelect = Button(text="Select Destination Folder", font="Helvetica 10", command=setDestination)
destinationSelect.pack(pady=10)

destinationText = StringVar()
destinationText.set("Destination: None")
currentDestination = Label(textvariable=destinationText, font=("Helvetica 10"))
currentDestination.pack(pady=10)

runConvertToJPG = Button(text="Convert to JPG", font="Helvetica 10", command=lambda: convert("jpg"))
runConvertToJPG.pack(pady=10)

runConvertToJPG = Button(text="Convert to PNG", font="Helvetica 10", command=lambda: convert("png"))
runConvertToJPG.pack(pady=10)

messageText = StringVar()
messageText.set("")
currentMessage = Label(textvariable=messageText, font=("Helvetica 10"))
currentMessage.pack(pady=10)

# Open the Tkinter window
window.mainloop()