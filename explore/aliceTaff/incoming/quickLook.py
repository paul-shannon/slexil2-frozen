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
def runTests(display=False):

    test_conversation(display)

#----------------------------------------------------------------------------------------------------
def test_conversation(display):

    print("--- test_conversation")

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

    if(display):
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".html", dir=".")
        try:
            tmp.write(bytes(htmlText, "utf-8"))
            tmp.close()
        finally:
            os.system("open %s" % tmp.name)


#----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    display = False
    if(len(sys.argv) == 2 and sys.argv[1] == "display"):
        display = True
    runTests(display)
