import vs

instrType       = ""
instrMode       = ""
wattage         = ""
position        = ""
channel         = ""
universeAdress  = ""
circuitNumber   = ""
circuitName     = ""
uid             = ""

def getFile():
	fileName = vs.GetFile()
	if not vs.DidCancel():
		vs.Close(fileName)
	return (fileName)


def eachLight(h):
	vs.SetRField(h, "Lighting Device", "Wattage", wattage)
	vs.SetRField(h, "Lighting Device", "Postion", position)
	vs.SetRField(h, "Lighting Device", "Channel", channel)
	vs.SetRField(h, "Lighting Device", "UniverseAddress", universeAdress)
	vs.SetRField(h, "Lighting Device", "Circuit Number", circuitNumber)
	vs.SetRField(h, "Lighting Device", "Circuit Name", circuitName)
	
#path = r"C:\Users\brage\Dropbox\Lys\Brages Prosjektmappe\Vectorworks Dev\ImportExport\myFile.txt"
path = getFile()

numberElements = 9 #Number of datafields in one line
headerRow = 4      #The header row. Which column is what
firstRow = 5       #First row of data

with open(path,"r") as f:
    line = f.readline()
    cnt = 1
    while line:
        line = f.readline()

        #Remove newline character at the end of each line
        newLineIndex = line.find('\n')
        if newLineIndex >= 0:
            line = line[:newLineIndex]

        #Split each line into element at each tab delimiter
        splits = line.split('\t')

        #parse data
        if cnt > firstRow:
            if len(splits) == numberElements:
                instrType       = splits[0]
                instrMode       = splits[1]
                wattage         = splits[2]
                position        = splits[3]
                channel         = splits[4]
                universeAdress  = splits[5]
                circuitNumber   = splits[6]
                circuitName     = splits[7]
                uid             = splits[8]
                
                criteria = "(N='" + uid + "')"
                
                vs.ForEachObject(eachLight,criteria)
        cnt+=1
