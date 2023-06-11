#Makefile

install:
	poetry install

brain-games: # run brain-games
	poetry run brain-games

build: # build project
	poetry build

publish: # publish without PyPI
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
