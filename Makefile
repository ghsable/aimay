init:
	python -m pip install --upgrade pip
	pip uninstall -r requirements.txt
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

docker_build:
	docker build -t aimay .

docker_run:
#	docker run --name aimay_bash -d -i -t aimay
	docker run --name aimay_bash --rm -i -t aimay bash

docker_exec:
	docker exec -it aimay_bash bash

docker_stop:
	docker stop `docker ps -q`

docker_rm:
	docker rm `docker ps -a -q`
	docker ps -a

docker_rmi:
	docker rmi -f `docker images -q`
	docker images
