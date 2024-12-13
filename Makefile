install:
	pip install --upgrade pip setuptools wheel &&\
		pip install -r requirements.txt

algorithms:
	pytest --nbmake --nbmake-timeout=1000 -n=auto algorithms

tools:
	pytest --nbmake --nbmake-timeout=1500 -n=auto tools

use-cases:
	pytest --nbmake --nbmake-timeout=1000 -n=auto use-cases

test: algorithms tools use-cases

all: install test