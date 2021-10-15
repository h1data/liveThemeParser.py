# Live 10 Theme File Parser by h1data
# outputs tsv file with color tag and color codes
# confirmed functional with Python 3.7.1

# usage
# python liveThemeParser.py [livethemefile]

import sys
import os
import xml.etree.ElementTree as ET

if len(sys.argv) != 2:
    print("usage: python " + sys.argv[0] + " [liveThemeFile]")
    sys.exit()

try:
    outfile = os.path.splitext(os.path.basename(sys.argv[1]))[0] + "_result.txt"
    root = ET.parse(sys.argv[1])
    with open(outfile, "w") as f:
        for element in root.findall("./SkinManager//R/.."):
            R = int(element.find("./R").get("Value"))
            G = int(element.find("./G").get("Value"))
            B = int(element.find("./B").get("Value"))
            f.write(element.tag + "\t" + ("%x" % R).zfill(2) + ("%x" % G).zfill(2) + ("%x" % B).zfill(2) + "\n")
    f.closed
    print("output to " + outfile)
except FileNotFoundError:
    print("!!ERROR!! unable to read " + sys.argv[1])
