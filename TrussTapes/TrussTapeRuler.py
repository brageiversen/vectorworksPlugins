import vs

endmarkClassPrefix = "Lightning Tapes-"
endmarkLayer = vs.GetObject("Endmarks")
rulerLayer = vs.GetObject("Ruler")


def createSymbolAndName(name,p,lx_name,end_field,end_name,className):
	vs.Symbol(name,p,0)
	h = vs.LNewObj()
	vs.SetRField(h, "End Marks Record Format", "TrussName",lx_name )
	vs.SetRField(h, "End Marks Record Format", end_field,end_name,end_name )
	vs.SetClass(h,className)
	vs.SetParent(h,endmarkLayer)
	

trussLength = vs.IntDialog("Length of Truss? (mm)", 10000)
trussName = vs.StrDialog("Name of Truss?", "LX0")

posY = 0

leftX = -trussLength/2
rightX = trussLength/2

rightName = "Endmark SL"
centerName = "Endmark Center"
leftName = "Endmark SR"

createSymbolAndName(rightName,(rightX,posY),trussName,"Right Name","SL End",endmarkClassPrefix + trussName)
createSymbolAndName(centerName,(0,posY),trussName,"Right Name","Center",endmarkClassPrefix + trussName)
createSymbolAndName(leftName,(leftX,posY),trussName,"Left Name","SR End",endmarkClassPrefix + trussName)

h = vs.GetObject("rulerTemplate")

hh = vs.CreateDuplicateObject(h,None)
vs.SetClass(hh,endmarkClassPrefix + trussName)
vs.SetParent(hh,rulerLayer)
vs.SetRField(hh, "Dimension Tape", "TapeLength", trussLength)

x,y = vs.Get2DPt(hh,0)
dx = -x - trussLength/2
dy = -y + posY
vs.HMove(hh,dx,dy) 

