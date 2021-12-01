import vs

crit = "((R IN ['Data Tag']))"

labelClassPrefix = "40 Label Lights-4"

def GetTaggedObject(h):
    result = False;
    num = vs.GetNumAssociations(h);
        
    assH = None
    assKind = None
    value = None
    i = 0;
    while(i < num and result == False):
        assH, assKind, value = vs.GetAssociation(h, i);
        if (assKind == 37):
            result = True;
        i = i + 1;
    return result, assH;

def callback(h):
	
	value, assH = GetTaggedObject(h)
	
	instrType = vs.GetRField(assH,"Lighting Device","Inst Type")
	deviceType = vs.GetRField(assH,"Lighting Device","Device Type")
	
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
	dataTagClass = labelClassPrefix + deviceTypeNumber + "_" + instrType
	
	if deviceType == "Moving Light" or deviceType == "Light" or deviceType == "SFX": 
		vs.NameClass(dataTagClass)

	vs.SetClass(h,dataTagClass)

vs.ForEachObject(callback, crit)
