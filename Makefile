install:
	poetry install

lint:
	poetry run flake8 brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	pip uninstall hexlet-code
