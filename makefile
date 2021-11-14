default:
	@echo targets: install test

install:
	source ./vpy363/bin/activate; \
	pip3 install -r requirements.txt

test:
	@echo test target not yet set up

