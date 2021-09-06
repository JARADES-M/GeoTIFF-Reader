install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=services --cov=main tests/test_image_processor.py tests/test_main.py

format:
	black *.py services/*.py models/*.py

lint:
	pylint --disable=R,C,W,E *.py services/*.py models/*.py

all: install lint test