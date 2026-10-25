.PHONY: html gettext clean

html:
	python -m sphinx -b html . _build/html

gettext:
	python -m sphinx -b gettext . _build/gettext

clean:
	python -c "import shutil; shutil.rmtree('_build', ignore_errors=True)"
