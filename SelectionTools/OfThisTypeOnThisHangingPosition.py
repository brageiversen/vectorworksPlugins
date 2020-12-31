import vs
 
selectedInstrumentType = ""
selectedInstrumentPos = ""

def instrument(h): 
	global selectedInstrumentType
	global selectedInstrumentPos
	selectedInstrumentType = vs.GetRField(h,"Lighting Device","Inst Type")
	selectedInstrumentPos = vs.GetRField(h, "Lighting Device", "Position")
	
	return()

selectedLightCrit = "(((SEL=TRUE) & (R IN ['Lighting Device'])))"
vs.ForEachObject(instrument,selectedLightCrit)
vs.DSelectAll()

s = "((R IN ['Lighting Device']) & ('Lighting Device'.'Inst Type'='" + selectedInstrumentType + "') & ('Lighting Device'.'Position'='" + selectedInstrumentPos + "'))"
vs.SelectObj(s)
#vs.Message(s)
	
#(((R IN ['Lighting Device']) & (('Lighting Device'.'Inst Type'='viper') & ('Lighting Device'.'Position'='LX8'))))