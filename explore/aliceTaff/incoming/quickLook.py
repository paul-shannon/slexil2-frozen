import re
import sys
sys.path.append("../../../slexil")
from text import *
import importlib
import os
import pdb
import tempfile
#----------------------------------------------------------------------------------------------------
pd.set_option('display.width', 1000)
#----------------------------------------------------------------------------------------------------
audioFilename = "1RuthNora2Wide.wav"
elanXmlFilename ="01RuthNora230126forPS.eaf"
targetDirectory = "audio"
projectDirectory = "./"
tierGuideFile= "tierGuide.yaml"
grammaticalTermsFile="grammaticalTerms.txt"

text = Text(elanXmlFilename, audioFilename, grammaticalTermsFile, tierGuideFile,
            projectDirectory, quiet=True)
text.getTierSummary()

htmlText = indent(text.toHTML())
# jsText = text.getJavascript()

tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".html", dir=".")
try:
   tmp.write(bytes(htmlText, "utf-8"))
   tmp.close()
   print("wrote %s" % tmp.name)
finally:
   os.system("open %s" % tmp.name)
