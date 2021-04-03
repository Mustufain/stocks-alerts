.virtualenv:
	virtualenv -p python3 .virtualenv
	. .virtualenv/bin/activate; \
	pip install -r requirements.txt -r requirements_test.txt

clean:
	find . -name __pycache__ -exec rm -rf {} +
	rm -rf *.egg-info
	rm -rf .virtualenv/


test: .virtualenv
	(. .virtualenv/bin/activate; \
	pycodestyle --max-line-length=79 stocks_alerting test; \
	nosetests --with-coverage --cover-tests --cover-min-percentage=80 --cover-package=stocks_alerting test)

build: test clean

.PHONY: test clean
