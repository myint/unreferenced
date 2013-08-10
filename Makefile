check:
	pep8 unreferenced unreferenced.py setup.py
	pep257 unreferenced unreferenced.py setup.py
	pylint \
		--report=no \
		--msg-template='{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}' \
		--rcfile=/dev/null \
		unreferenced.py setup.py
	python setup.py --long-description | rst2html --strict > /dev/null
	scspell unreferenced unreferenced.py setup.py README.rst

readme:
	@restview --long-description --strict
