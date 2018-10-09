from DataStructure import *
from askText import *

if __name__ == '__main__':
    d = DataStructure()
    value = askText()
    d.renameInFolder(prefix = value.ret[0], suffix = value.ret[0])
