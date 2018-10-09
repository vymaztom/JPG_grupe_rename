import exifread

class PictureFile:
    '''class for decode exif data from one file'''
    def __init__(self, nameoffile):
        self.name = nameoffile
        self.newName = ""
        self.time = ""
        self.camera = ""
        self.endName = ""
        self.readexif()
        self.generateNewName()

    def readexif(self):
        '''read EXIF data from Picture file and save it into values'''
        with open(self.name, "rb") as f:
            #read prefix of file
            self.endName = self.name.split(".")[-1]

            #read exif data from file and save into dictionary
            self.EXIFdata = exifread.process_file(f)

            #read exif data from dictionary
            if "EXIF DateTimeOriginal" in self.EXIFdata.keys():
                self.time = self.EXIFdata["EXIF DateTimeOriginal"]
            else:
                self.time = "None"

            if "Image Model" in self.EXIFdata.keys():
                self.camera = self.EXIFdata["Image Model"]
            else:
                self.camera = "None"

    def generateNewName(self):
        '''generate new name from Picture file by using date and time'''
        help_value = str(self.time).split(" ")
        help_date = str(help_value[0]).split(":")
        self.newName = ""
        for part in help_date:
            self.newName += part

        help_time = str(help_value[1]).split(":")
        for part in help_time:
            self.newName += part
