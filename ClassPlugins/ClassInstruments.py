import vs

lightingClassPrefix = "40 Lights-4"

def changeClass(h): 
	instrType = vs.GetRField(h,"Lighting Device","Inst Type")
	deviceType = vs.GetRField(h,"Lighting Device","Device Type")
	
	deviceTypeNumber = "0"
	if deviceType == "Moving Light":
		deviceTypeNumber = "2"
	elif deviceType == "Light": 
		deviceTypeNumber = "1"
	elif deviceType == "SFX":
		deviceTypeNumber = "8"
	else:
		deviceTypeNumber = "3"
		
	#Get rid of "-" and the rest of the instrument name. Removes things like "- Hung" from class name. 
	indexOfBar = instrType.find("-")
	if indexOfBar != -1: 
		instrType = instrType[:indexOfBar]
	instrTypeClass = lightingClassPrefix + deviceTypeNumber + "_" + instrType
	
	vs.SetClass(h,instrTypeClass)
	return()

activeClass = vs.ActiveClass()

lightingInstrumentCriteria = "(NOTINDLVP & NOTINREFDLVP & (R IN ['Lighting Device']))"

vs.ForEachObject(changeClass,lightingInstrumentCriteria)

vs.NameClass(activeClass)
