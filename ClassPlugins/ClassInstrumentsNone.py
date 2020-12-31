import vs


def changeClass(h): 
	instrType = vs.GetRField(h,"Lighting Device","Inst Type")
	vs.SetClass(h,"None")
	return()


lightingInstrumentCriteria = "(NOTINDLVP & NOTINREFDLVP & (R IN ['Lighting Device']))"

vs.ForEachObject(changeClass,lightingInstrumentCriteria)