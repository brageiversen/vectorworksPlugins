import vs

lightingPosClassPrefix = "20 Rigging-21_Truss_"

def changeClass(h): 
	posName = vs.GetRField(h,"Light Position Obj","Position Name")
	
	className = lightingPosClassPrefix + posName
	
	vs.SetClass(h,className)
	return()

activeClass = vs.ActiveClass()

hoistCrit = "(R IN ['Light Position Obj'])"

vs.ForEachObject(changeClass,hoistCrit)

vs.NameClass(activeClass)
