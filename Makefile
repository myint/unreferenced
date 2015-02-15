check:
	pep8 unreferenced unreferenced.py setup.py
	pep257 unreferenced unreferenced.py setup.py
	pylint \
		--report=no \
		--rcfile=/dev/null \
		--disable=bad-continuation \
		--disable=missing-docstring \
		unreferenced.py setup.py
	python setup.py --long-description | rstcheck -
	scspell unreferenced unreferenced.py setup.py README.rst

readme:
	@restview --long-description --strict
