uniqueTruss = []
uniqueTrussCount = []

def MyGetPlugInString(ndx):
#{Static Text}
	GetPlugInString = ''
	if   ndx == 1001:
		GetPlugInString = 'OK'
	elif ndx == 1002:		
		GetPlugInString = 'Cancel'
	elif ndx == 1003:
		GetPlugInString = 'Truss Count'
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
	vs.CreateStaticText( dialog, kListBoxText, "Truss Count", -1 );
	vs.SetFirstLayoutItem( dialog, kListBoxText );
	
	for i in range(len(uniqueTruss)):
		if i < 100: 
			name = uniqueTruss[i]
			cnt = uniqueTrussCount[i]
		
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
	type = vs.GetRField(h,"Truss Record","Model Name")
	
	global uniqueTruss
	if not (type in uniqueTruss):
		uniqueTruss.append(type)
	
	return()
	
	
# Criteria for iteration of all lighting devices
searchCrit = "((INOBJECT & (R IN ['Truss Record']) & (PON='TrussItem')))"
vs.ForEachObject(checkType,searchCrit)

for i in range(len(uniqueTruss)):
	name = uniqueTruss[i]
	#global uniqueInstrumentsCount
	uniqueTrussCount.append(int(vs.Count("((INOBJECT & (R IN ['Truss Record']) & (PON='TrussItem') & ('Truss Record'.'Model Name'='" + name + "')))")))

SampleDlg2()