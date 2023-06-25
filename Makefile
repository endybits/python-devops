install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C *.py devopslib
test:
	pytest -m pytest -vv --cov=devopslib