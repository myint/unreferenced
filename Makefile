check:
	pycodestyle unreferenced unreferenced.py setup.py
	pydocstyle unreferenced unreferenced.py setup.py
	pylint \
		--reports=no \
		--rcfile=/dev/null \
		--disable=bad-continuation \
		--disable=missing-docstring \
		unreferenced.py setup.py
	python setup.py --long-description | rstcheck -
	scspell unreferenced unreferenced.py setup.py README.rst

readme:
	@restview --long-description --strict
