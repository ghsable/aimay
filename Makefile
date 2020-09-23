init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	python -m coverage run -m unittest discover
	python -m coverage html

run:
#	python -m aimay
#	uwsgi --workers=9 --http=0.0.0.0:8080 --mount /=aimay.__main__:app
	gunicorn --workers 9 aimay.__main__:app

sdist:
	python setup.py sdist
