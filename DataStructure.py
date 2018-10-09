import os
from askDir import *
from PictureFile import *

class DataStructure:
    '''datastructure of pictures, for make some relations'''

    def __init__(self):
        self.data = []
        self.dataByCamera = {}
        self.cameras = []
        self.formates = ["JPG","jpg"]

    def add(self, struct):
        '''add PictureFile into structure'''

        #add into basic structure
        self.data.append(struct)

        #add into structure sorted by camera
        if not self.cameras.__contains__(struct.camera):
            self.dataByCamera[struct.camera] = []
            self.cameras.append(struct.camera)
        self.dataByCamera[struct.camera].append([str(struct.name),str(struct.time)])

    def printValues(self):
        '''print structure'''
        for one in self.cameras:
            print(str(one))
            root = self.data[one]
            for p in  root:
                print(">>>" + p[0] + " -- " + p[1])

    def loadDataFromDirectory(self, nameOfDirectory):
        '''load all alowed files from directory'''
        os.chdir(nameOfDirectory)
        files = os.listdir(nameOfDirectory)
        for one in files:
            part = one.split(".")
            if len(part) == 2 and self.formates.__contains__(part[1]):
                picture = PictureFile(one)
                self.add(picture)

    def getData(self):
        '''retrun list of strustures PictureFile'''
        retrun(self.data)

    def renameInFolder(self, prefix = "", suffix = ""):
        '''run function for rename Picture files by using suf/prefix'''
        dir = askDir()
        self.loadDataFromDirectory(dir)
        for one in self.data:
            os.renames(old = one.name, new = (prefix + one.newName + suffix + "." + str(one.endName)))

    
