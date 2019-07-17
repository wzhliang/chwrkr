.PHONY: test clean default

default:
	pyinstaller -c -F main.py
	cp dist/main ${HOME}/bin/chwrk && chmod a+x ${HOME}/bin/chwrk

clean:
	@rm -rf __pycache__ build dist
