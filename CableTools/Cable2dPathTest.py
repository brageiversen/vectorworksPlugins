import vs

def parseCables(cables):
    numberOfDelim = cables.count("/")
    cableLengthList = cables.split("/",numberOfDelim)
    availableLengths = [0] * (numberOfDelim+1)
    for i in range(numberOfDelim+1):
        availableLengths[i] = float(cableLengthList[i]) * 1000
    return availableLengths

def chooseCable(length,availableLengths):
    if(length > 0):
        result = 0
        for i in range(0,len(availableLengths)):
            l = availableLengths[i]
            if length - l <= 0:
                result = l
                break
            return result
    else:
        return -1
	
def calculateTopPoint(x1,y1,x2,y2,offset):
	angle = vs.ArcTan((y2-y1)/(x2-x1))
	x3 = x1 + (x2-x1)/2 - offset * vs.Sin(angle)
	y3 = y1 + (y2-y1)/2 + offset * vs.Cos(angle)
	
	return (x3,y3)
	
def calculateAngle(x1,y1,x2,y2):
	return vs.Rad2Deg(vs.ArcTan((y2-y1)/(x2-x1)))


#Get info about "this" object
(ok, objectName, h, recordHand, wall) = vs.GetCustomObjectInfo()

if ok: 
	path = vs.GetCustomObjectPath(h)		#The vertices
	numberOfVertices = vs.GetVertNum(path)	#Number of vertices
	
	#cableClassPrefix = "40 Lights-49_Cable Type "
	cableClassPrefix = vs.PClass_Prefix
	yOffset = vs.PArc_Height
	cableOffset = 1000
	textOffset = vs.PText_Offset
	name = vs.PName
	cables = vs.PAvailable_Lengths
	availableLengths = parseCables(cables)
	
	t = " Test: "
	for l in availableLengths:
		t = t + str(l) + " "
	
	vs.Message(t)
	
	for i in range(2,numberOfVertices+1):
		#Get the start and end point for the cable
		(x2,y2) = vs.GetPolyPt(path,i)
		(x1,y1) = vs.GetPolyPt(path,i-1)
		
		#Calculate the top coordinate for the cable arc. 
		(x3,y3) = calculateTopPoint(x1,y1,x2,y2,yOffset)
		
		#Draw a cubic poly line
		vs.Smooth(2)
		vs.Poly(x1, y1,x3,y3,x2,y2)
		
		#Get the latest created object (poly) and set line weight
		h = vs.LNewObj()
		vs.SetLW(h,20)
		
		#Set Color and Class
		if vs.PType == "DMX":
			vs.SetPenFore(h,(65535,0,0))
			vs.SetClass(h,cableClassPrefix + "DMX")	
		elif vs.PType == "Power":
			vs.SetPenFore(h,(0,65535,0))
			vs.SetClass(h,cableClassPrefix + "Power")	
		elif vs.PType == "Hybrid":
			vs.SetPenFore(h,(0,0,65535))
			vs.SetClass(h,cableClassPrefix + "Hybrid")
			
		#Calculate which cable length is required
		rawCableLength = vs.Sqrt((x2-x1)**2 + (y2-y1)**2)
		actualCableLength = rawCableLength + cableOffset
		choosenCable = chooseCable(actualCableLength,availableLengths)
		vs.Message(str(availableLengths))
		
		(x4,y4) = calculateTopPoint(x1,y1,x2,y2,yOffset+textOffset)
		vs.MoveTo(x4,y4)
		vs.TextJust(2)
		vs.TextRotate(calculateAngle(x1,y1,x2,y2))
		#vs.CreateText(name + "\r" + vs.PType + " " + str(choosenCable/1000) + "m")
		#vs.CreateText(str(choosenCable/1000))
	
	numberOfCables = numberOfVertices-1
	