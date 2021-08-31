import vs

uniqueInstruments = []
uniqueInstrumentsCount = []

def MyGetPlugInString(ndx):
#{Static Text}
	GetPlugInString = ''
	if   ndx == 1001:
		GetPlugInString = 'OK'
	elif ndx == 1002:		
		GetPlugInString = 'Cancel'
	elif ndx == 1003:
		GetPlugInString = 'Instrument Count'
	elif ndx == 1004:
		GetPlugInString = 'List Box'
	elif ndx == 1005: 
		GetPlugInString = ''
	elif ndx == 1006:
		GetPlugInString = 'List Browser'
	elif ndx == 1007:
		GetPlugInString = ''
	elif ndx == 1008:
		GetPlugInString = ''
	#{Help Text}
	if   ndx == 2001:
		GetPlugInString = 'Accepts the dialog data.'
	elif ndx == 2002: 
		GetPlugInString = 'Cancels the dialog data.'
	elif ndx == 2004: 
		GetPlugInString = ''
	elif ndx == 2005:
		GetPlugInString = 'This is list box control.'
	elif ndx == 2006: 
		GetPlugInString = ''
	elif ndx == 2007:
		GetPlugInString = 'This is list browser control.'
	elif ndx == 2008:
		GetPlugInString = 'Tabbed content list box. This list box contains rows with two strings with tab delimiter. This causes the list to have two columns.'
	return GetPlugInString
	
def GetStr(ndx):
    return MyGetPlugInString( ndx + 1000 )


def GetHelpStr(ndx):
    return MyGetPlugInString( ndx + 2000 )

def SampleDlg2():

	#{ default and cancel button IDs}
	kOK                   = 1;
	kCancel               = 2;

	#{ control IDs}
	kListBoxText          = 4;

	dialog = vs.CreateResizableLayout(GetStr(3), True, GetStr(kOK), GetStr(kCancel), True, True );

	#{create controls}
	vs.CreateStaticText( dialog, kListBoxText, "Instrument Count", -1 );
	vs.SetFirstLayoutItem( dialog, kListBoxText );
	
	for i in range(len(uniqueInstruments)):
		if i < 100: 
			name = uniqueInstruments[i]
			cnt = uniqueInstrumentsCount[i]
		
			#name field
			vs.CreateStaticText( dialog, kListBoxText+i+1, name, -1 );
			vs.SetBelowItem( dialog, kListBoxText+i, kListBoxText+i+1, 0, 0 );
		
			#count field
			vs.CreateStaticText( dialog, kListBoxText+i+100, str(cnt), -1 );
			vs.SetRightItem( dialog, kListBoxText+i+1, kListBoxText+i+100, 0, 0 );

	

	#{set help strings}
	for cnt in range(1,8):
		vs.SetHelpText(dialog, cnt, GetHelpStr(cnt))



	if vs.RunLayoutDialog( dialog, None ) == 1:
		pass
		
# ----------------------------------------------------------

def checkType(h): 
	type = vs.GetRField(h,"Lighting Device","Inst Type")
	
	global uniqueInstruments
	if not (type in uniqueInstruments):
		uniqueInstruments.append(type)
	
	return()
	
parameterType = 'Lighting Device'
parameterName = 'Inst Type'
	
# Criteria for iteration of all lighting devices
lightCriteria = "((R IN ['" + parameterType + "']))"
vs.ForEachObject(checkType,lightCriteria)

# Which 

for i in range(len(uniqueInstruments)):
	name = uniqueInstruments[i]
	#global uniqueInstrumentsCount
	uniqueInstrumentsCount.append(int(vs.Count("((R IN ['" + parameterType + "'])) & ('" + parameterType + "'.'" + parameterName + "'='" + name + "')")))

SampleDlg2()