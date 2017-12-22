#!/usr/bin/env python

import json
from skimage.color import deltaE_ciede2000

# For reducing the colourset
# requires scikit-image

def rgb2one(r):
    return (float(r[0]/256),float(r[1]/256),float(r[2]/256))
    
with open("dmc.json") as w:
    DMC = json.load(w)


seen = []
for i in DMC:
    irgb = i["RGB"]
    icol = i["ColorName"]
    ihex = "#"+i["Hex"]

    for j in DMC:
        jrgb = j["RGB"]
        jcol = j["ColorName"]
        jhex = "#"+j["Hex"]

        if icol == jcol:
            continue

        #if "{},{}".format(jcol,icol) in seen:
        #    continue

        seen.append("{},{}".format(icol, jcol))

        io = rgb2one(irgb) 
        jo = rgb2one(jrgb)

        d = deltaE_ciede2000(io, jo)

        print("<tr><td>{}</td>".format(d), end="")
        print("<td>{}</td><td>{}</td><td style='background-color: {}'>&nbsp; &nbsp; &nbsp; &nbsp;</td>".format(icol,ihex,ihex), end="")
        print("<td style='background-color: {}'>&nbsp; &nbsp; &nbsp; &nbsp; </td><td>{}</td><td>{}</td>".format(jhex,jhex,jcol), end="")
        print("</tr>")

