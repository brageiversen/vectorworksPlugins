import vs
pluginLng= vs.PLineLength

vs.MoveTo(0,0)
#vs.LineTo(pluginLng,0)

yOffset = vs.PY_Offset

vs.Smooth(2)
vs.Poly(0, yOffset, pluginLng/2, 0.2*pluginLng+yOffset, pluginLng, yOffset)
h = vs.LNewObj()
vs.SetLW(h,20)

cableClassPrefix = "40 Lights-49_Cable Type "

if vs.PType == "DMX":
	vs.SetPenFore(h,(65535,0,0))
	vs.SetClass(h,cableClassPrefix + "DMX")	
elif vs.PType == "Power":
	vs.SetPenFore(h,(0,65535,0))
	vs.SetClass(h,cableClassPrefix + "Power")	
elif vs.PType == "Hybrid":
	vs.SetPenFore(h,(0,0,65535))
	vs.SetClass(h,cableClassPrefix + "Hybrid")




