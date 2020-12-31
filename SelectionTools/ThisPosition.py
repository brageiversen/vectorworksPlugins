import vs
 
selectedInstrumentPos = ""

def instrument(h): 
	global selectedInstrumentPos
	selectedInstrumentPos = vs.GetRField(h,"Lighting Device","Position")
	
	
	return()

selectedLightCrit = "(((SEL=TRUE) & (R IN ['Lighting Device'])))"
vs.ForEachObject(instrument,selectedLightCrit)
vs.DSelectAll()

s = "(((R IN ['Lighting Device']) & ('Lighting Device'.'Position'='" + selectedInstrumentPos + "')))"
vs.SelectObj(s)

