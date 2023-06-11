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

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	pip uninstall hexlet-code
