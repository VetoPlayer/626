#!/usr/bin/env python

import json
from skimage.color import deltaE_ciede2000

# For reducing the colourset
# requires scikit-image

def rgb2one(r):
    return (float(r[0]/256),float(r[1]/256),float(r[2]/256))
    
##with open("dmc.json") as w:
#with open("limited.json") as w:
with open("raw/color.json") as w:
    DMC = json.load(w)


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


seen = []
for i in DMC:
    icol = i["Description"]
    ihex = "#"+i["Hex"]
    irgb = hex_to_rgb(ihex)

    for j in DMC:
        jcol = j["Description"]
        jhex = "#"+j["Hex"]
        jrgb = hex_to_rgb(jhex)

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

