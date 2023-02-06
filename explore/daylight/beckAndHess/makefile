STORY = beckAndHess
YAML2EAF = ~/github/slexil2/yamlToEAF/toEAF.py

default:
	@echo targets: venv  eaf extractAudio html open

venv:
	@echo be sure to run: source /Users/paul/github/slexil2/py3105/bin/activate



eaf:
	python ~/github/slexil2/yamlToEAF/toEAF.py $(STORY).yaml


html:
	python daylight-eaf2html.py 

open:
	open $(STORY)0.html

extractAudio:
	python ~/github/slexil2/yamlToEAF/extractAudioPhrases.py \
                               daylight.wav \
                               $(STORY).eaf \
                               audio
customize:
	sed -f ../insertCustomCode.sed $(STORY)0.html  > $(STORY).html



