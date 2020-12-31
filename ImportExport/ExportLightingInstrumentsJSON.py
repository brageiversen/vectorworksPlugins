import vs
import datetime
import json

def saveNewFile():
	path = vs.PutFile("Export data..", "importexportLights.json")
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

fileName = saveNewFile()
lightingInstrumentCriteria = "(NOTINDLVP & NOTINREFDLVP & (R IN ['Lighting Device']))"

numberOfFixtures = vs.Count(lightingInstrumentCriteria)
	
dataToExport = {}

dataToExport['info'] = []
dataToExport['info'].append({
	'fileName': getFileName(),
	'fixtureCount': str(int(numberOfFixtures)),
	'exportDate': date,
	'exportTime': time
})

dataToExport['lightingDevices'] = []

def iterate(h): 
	#Python oject containing lighting type data
	device = {
		"instrumentType": vs.GetRField(h,"Lighting Device","Inst Type"),
		"fixtureMode": vs.GetRField(h,"Lighting Device","Fixture Mode"),
		"wattage": vs.GetRField(h,"Lighting Device","Wattage"),
		"position": vs.GetRField(h,"Lighting Device","Position"),
		"channel": vs.GetRField(h,"Lighting Device","Channel"),
		"patch": vs.GetRField(h,"Lighting Device","UniverseAddress"),
		"circuitNumber": vs.GetRField(h,"Lighting Device","Circuit Number"),
		"circuitName": vs.GetRField(h,"Lighting Device","Circuit Name"),
		"dmxLine": vs.GetRField(h,"Lighting Device", "DMX Line"), 
		"dmxFootprint": vs.GetRField(h,"Lighting Device","num channels"),
		"deviceType": vs.GetRField(h,"Lighting Device","Device Type"),
		"color": vs.GetRField(h,"Lighting Device","Color"),
		"userField1": vs.GetRField(h,"Lighting Device", "User Field 1"),
		"userField2": vs.GetRField(h,"Lighting Device", "User Field 2"),
		"userField3": vs.GetRField(h,"Lighting Device", "User Field 3"),
		"userField4": vs.GetRField(h,"Lighting Device", "User Field 4"),
		"userField5": vs.GetRField(h,"Lighting Device", "User Field 5"),
		"userField6": vs.GetRField(h,"Lighting Device", "User Field 6"),
		"__UID": vs.GetName(h),
		"class": vs.GetClass(h),
		"layer": vs.GetLName(vs.GetLayer(h)),
		
	}
	
	
	
	dataToExport['lightingDevices'].append(device)
		
vs.ForEachObject(iterate,lightingInstrumentCriteria)

with open(fileName,'w') as outfile:
	json.dump(dataToExport,outfile,indent=4)