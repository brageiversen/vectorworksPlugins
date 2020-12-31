import vs
import datetime

def saveNewFile():
	path = vs.PutFile("Export data..", "importexport.txt")
	if not vs.DidCancel():
		vs.Close(path)

	#indexOfLastBackSlash = path.rfind("\\")
	#filename = path[(indexOfLastBackSlash+1):]
	return (path)

def getFileName():
	path = vs.GetFPathName()
	indexOfLastSlash = path.rfind("\\")
	return(path[(indexOfLastSlash+1):])

timestamp = datetime.datetime.now()
date = timestamp.strftime("%x")
time = timestamp.strftime("%X")

header = "Instrument Type	Fixture Mode	Wattage	Position	Channel	Universe/Address	Circuit Number	Circuit Name	__UID \r"
#fileName = r"C:\Users\brage\Dropbox\Lys\Brages Prosjektmappe\Vectorworks Dev\ImportExport\myFile.txt"
fileName = saveNewFile()
lightingInstrumentCriteria = "(NOTINDLVP & NOTINREFDLVP & (R IN ['Lighting Device']))"

numberOfFixtures = vs.Count(lightingInstrumentCriteria)
preheader = "Filename:\t" + getFileName() + "\rFirst row:\t7\rLast row\t" + str(int(numberOfFixtures+6)) + "\rDate:\t" + date + "\rTime:\t" + time + "\r"
f = open(fileName,'w')
f.write(preheader)
f.write(header)

def iterate(h): 
	instrType = vs.GetRField(h,"Lighting Device","Inst Type")
	mode = vs.GetRField(h,"Lighting Device","Fixture Mode")
	wattage = vs.GetRField(h,"Lighting Device","Wattage")
	pos = vs.GetRField(h,"Lighting Device","Position")
	channel = vs.GetRField(h,"Lighting Device","Channel")
	patch = vs.GetRField(h,"Lighting Device","UniverseAddress")
	circuitNumber = vs.GetRField(h,"Lighting Device","Circuit Number")
	circuitName = vs.GetRField(h,"Lighting Device","Circuit Name")
	uid = vs.GetName(h)
	
	data = instrType + "\t" + mode + "\t" + wattage + "\t" + pos + "\t" + channel + "\t" + patch + "\t" + circuitNumber + "\t" + circuitName + "\t" + uid + "\r"
	f.write(data)
		
	return()


vs.ForEachObject(iterate,lightingInstrumentCriteria)
f.close()