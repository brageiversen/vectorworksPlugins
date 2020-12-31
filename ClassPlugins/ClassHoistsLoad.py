import vs

hoistClassPrefix = "20 Rigging-28_Hoist_"

def changeClass(h): 
	hoistType = vs.GetRField(h,"HoistVW","Type")
	
	className = hoistClassPrefix + hoistType
	
	vs.SetClass(h,className)
	return()

activeClass = vs.ActiveClass()

hoistCrit = "(R IN ['HoistVW'])"