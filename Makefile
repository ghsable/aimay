init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	python -m coverage run -m unittest discover

run:
	python -m aimay
