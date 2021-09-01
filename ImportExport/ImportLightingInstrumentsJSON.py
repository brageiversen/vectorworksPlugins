import vs
import json

instrType = ""
instrMode = ""
wattage = ""
position = ""
channel = ""
universeAdress = ""
circuitNumber = ""
circuitName = ""
uid = ""
fixtureMode = ""
dmxLine = ""
dmxFootprint = ""
deviceType = ""
color = ""
user1 = ""
user2 = ""
user3 = ""
user4 = ""
user5 = ""
user6 = ""
className = ""


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
    vs.SetRField(h, "Lighting Device", "Inst Type", instrType)
    vs.SetRField(h, "Lighting Device", "Fixture Mode", instrMode)
    vs.SetRField(h, "Lighting Device", "DMX Line", dmxLine)
    vs.SetRField(h, "Lighting Device", "num channels", dmxFootprint)
    vs.SetRField(h, "Lighting Device", "Device Type", deviceType)
    vs.SetRField(h, "Lighting Device", "Color", color)
    vs.SetRField(h, "Lighting Device", "User Field 1", user1)
    vs.SetRField(h, "Lighting Device", "User Field 2", user2)
    vs.SetRField(h, "Lighting Device", "User Field 3", user3)
    vs.SetRField(h, "Lighting Device", "User Field 4", user4)
    vs.SetRField(h, "Lighting Device", "User Field 5", user5)
    vs.SetRField(h, "Lighting Device", "User Field 6", user6)

    vs.SetClass(h, className)


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

        dmxLine = p['dmxLine']
        dmxFootprint = p['dmxFootprint']
        deviceType = p['deviceType']
        color = p['color']
        user1 = p['userField1']
        user2 = p['userField2']
        user3 = p['userField3']
        user4 = p['userField4']
        user5 = p['userField5']
        user6 = p['userField6']

        className = p["class"]

        uid = p['__UID']

        criteria = "(N='" + uid + "')"

        vs.ForEachObject(eachLight, criteria)

        # "__UID": vs.GetName(h),
        # "class": vs.GetClass(h),
        # "layer": vs.GetLName(vs.GetLayer(h)),
