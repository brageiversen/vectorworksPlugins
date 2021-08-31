import vs
import json

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
	
path = getFile()
        
with open(path) as json_file:
	data = json.load(json_file)
	for p in data['lightingDevices']:
		instrType = p['instrumentType']
		instrMode = p['fixtureMode']
		wattage = p['wattage']
		position = p['position']
		channel = p['channel']
		universeAdress = p['patch']
		circuitNumber = p['circuitNumber']
		circuitName = p['circuitName']
		uid = p['__UID']
		
		criteria = "(N='" + uid + "')"
		
		vs.ForEachObject(eachLight,criteria)
		

#	device = {
#		"instrumentType": vs.GetRField(h,"Lighting Device","Inst Type"),
#		"fixtureMode": vs.GetRField(h,"Lighting Device","Fixture Mode"),
#		"wattage": vs.GetRField(h,"Lighting Device","Wattage"),
#		"position": vs.GetRField(h,"Lighting Device","Position"),
#		"channel": vs.GetRField(h,"Lighting Device","Channel"),
#		"patch": vs.GetRField(h,"Lighting Device","UniverseAddress"),
#		"circuitNumber": vs.GetRField(h,"Lighting Device","Circuit Number"),
#		"circuitName": vs.GetRField(h,"Lighting Device","Circuit Name"),
#		"__UID": vs.GetName(h)
#	}
