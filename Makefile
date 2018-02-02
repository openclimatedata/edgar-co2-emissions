data/edgar-co2-emissions.csv: venv
	./venv/bin/python scripts/process.py

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

clean:
	rm -rf data/*.csv

clean-venv:
	rm -rf venv

.PHONY: clean clean-venv
