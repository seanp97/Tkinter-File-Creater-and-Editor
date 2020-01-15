from tkinter import *
import sys
import tkinter
import os

fOpen = ""

def getFileName():
    try:
        global fileName
        fileNameEntry = Entry.get(labelNameEnt)
        fileName = fileNameEntry + ".txt"
        #print(fileName)
        global fOpen
        fOpen = open(fileName)
        fOpenR = fOpen.read()
        fileText.configure(text=fOpenR)
        
        if fOpenR == "":
            fileText.configure(text="Text File is Empty", font=("bold", 10))
        
    except:
        labelNameEnt.delete(first=0, last=1000)
        Entry.insert(labelNameEnt, 0, "File can't be found")
        
        
def writeToFile():
    try:
        global fOpen
        global fileName
        fOpen = open(fileName, "a")
        fileWriteText = Entry.get(fileWriteEnt)
        fOpen.write(fileWriteText + " ")
        fOpen.close()
    except:
        fileWriteEnt.delete(first=0, last=1000)
        Entry.insert(fileWriteEnt, 0, "Error occured")
    
    
def createFile():
    try:
        fileCreateText = Entry.get(createFileEnt)
        fileCreateText = fileCreateText + ".txt"
        NewFOpen = fileCreateText
        NewFOpen = open(NewFOpen, "x")
        NewFOpen.close()
    except:
        errorLabel.configure(text="An error occured")
        
        
def deleteFile():
    deleteFileText = Entry.get(deleteFileEnt)
    deleteFileText = deleteFileText + ".txt"
    
    if os.path.exists(deleteFileText):
        os.remove(deleteFileText)
    else:
        deleteFileEnt.delete(first=0, last=1000)
        Entry.insert(deleteFileEnt, 0, "File could not be found")

        
app = Tk()
app.title("Text File Writer and Reader")
app.geometry("800x400")

oneLabel = Label(app, text="Read and Write to text files", pady=20, padx=20)
oneLabel.grid(column=0, row=0)

labelName = Label(app, text="Type the text file. Note, must be in same directory", pady=20, padx=20)
labelName.grid(column=0, row=1)
labelNameEnt = Entry(app, bd=3)
labelNameEnt.grid(column=1, row=1)
labelNameBtn = Button(app, text="Submit", command=getFileName, bd=3)
labelNameBtn.grid(column=2, row=1)

fileText = Label(app, text="")
fileText.grid(column=0, row=2)

fileWrite = Label(app, text="Write to file", padx=20, pady=20)
fileWrite.grid(column=0, row=3)
fileWriteEnt = Entry(app, bd=3)
fileWriteEnt.grid(column=1, row=3)
fileWriteBtn = Button(app, bd=3, text="Submit", command=writeToFile)
fileWriteBtn.grid(column=2, row=3)

createFileLabel = Label(app, text="Creat a text File")
createFileLabel.grid(column=0, row=4, pady=20, padx=20)
createFileEnt = Entry(app, bd=3)
createFileEnt.grid(column=1, row=4)
createFileBtn = Button(app, text="Submit", bd=3, command=createFile)
createFileBtn.grid(column=2, row=4)

deleteFileLabel = Label(app, text="Delete a file")
deleteFileLabel.grid(column=0, row=5, padx=20, pady=20)
deleteFileEnt = Entry(app, bd=3)
deleteFileEnt.grid(column=1, row=5)
deleteFileBtn = Button(app, text="Submit", bd=3, command=deleteFile)
deleteFileBtn.grid(column=2, row=5)

errorLabel = Label(app, text=" ")
errorLabel.grid(column=0, row=6)

app.mainloop()
