import vs

def getFile():
	fileName = vs.GetFile()
	if not vs.DidCancel():
		vs.Close(fileName)
	return (fileName)

path = getFile()



with open(path,"r") as f:
	line = f.readline()
	while line:
		line = f.readline()
		vs.NameClass(line)
