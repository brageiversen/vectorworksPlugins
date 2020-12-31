import vs

def changeClass(h): 

	vs.SetClass(h,"None")
	return()

activeClass = vs.ActiveClass()

hoistCrit = "(R IN ['HoistVW'])"

vs.ForEachObject(changeClass,hoistCrit)

vs.NameClass(activeClass)