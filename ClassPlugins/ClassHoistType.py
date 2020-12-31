import vs

hoistClassPrefix = "20 Rigging-28_Hoist_"

def changeClass(h): 
	hoistFunc = vs.GetRField(h,"HoistVW","Function")
	
	className = hoistClassPrefix + hoistFunc
	
	vs.SetClass(h,className)
	return()

activeClass = vs.ActiveClass()

hoistCrit = "(R IN ['HoistVW'])"