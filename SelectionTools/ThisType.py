import vs
 
selectedInstrumentType = ""

def instrument(h): 
	global selectedInstrumentType
	selectedInstrumentType = vs.GetRField(h,"Lighting Device","Inst Type")
	
	
	return()

selectedLightCrit = "(((SEL=TRUE) & (R IN ['Lighting Device'])))"
vs.ForEachObject(instrument,selectedLightCrit)
vs.DSelectAll()

s = "(((R IN ['Lighting Device']) & ('Lighting Device'.'Inst Type'='" + selectedInstrumentType + "')))"
vs.SelectObj(s)
