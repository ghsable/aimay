init:
	python -m pip install -r requirements.txt
  python -m pip install codecov

test:
	python -m coverage run -m unittest discover

run:
  python -m aimay
