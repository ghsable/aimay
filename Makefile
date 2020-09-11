init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	python -m coverage run -m unittest discover
	python -m coverage html

run:
	python -m aimay
