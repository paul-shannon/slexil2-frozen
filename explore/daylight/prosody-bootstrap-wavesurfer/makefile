PORT = 8990
default:
	@echo targets: kb, http.local view.local publish
kb:
	m4 --quiet -P kb.pre > kb.pre2
	sed  s/COMMA/,/g kb.pre2 > kb.js

http:
	python3 -m http.server $(PORT) &

view.local:
	open http://localhost:$(PORT)/index.html

publish:
	scp * paulshannnon@pshannon.net:public_html/pshannon.net/slexil2/

view:
	open   https://pshannon.net/slexil2/

