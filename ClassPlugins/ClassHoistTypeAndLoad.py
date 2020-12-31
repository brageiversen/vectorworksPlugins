import vs

hoistClassPrefix = "20 Rigging-28_Hoist_"

def changeClass(h): 
	hoistType = vs.GetRField(h,"HoistVW","Type")
	hoistFunc = vs.GetRField(h,"HoistVW","Function")
	
	className = hoistClassPrefix + hoistFunc + " " + hoistType
	
	vs.SetClass(h,className)
	return()

activeClass = vs.ActiveClass()

hoistCrit = "(R IN ['HoistVW'])"

vs.ForEachObject(changeClass,hoistCrit)

vs.NameClass(activeClass)
