PYTHON ?= python
QUARTO ?= quarto

.PHONY: html doctest preview

html:
	$(PYTHON) render_api.py
	$(QUARTO) render .

doctest:
	$(PYTHON) -m sphinx -b doctest . _build/doctest

preview:
	$(PYTHON) render_api.py
	$(QUARTO) preview .
