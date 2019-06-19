all: main

main:
	.venv/bin/python ti.py --width=50 img/logo.png

init:
	python3 -m venv .venv

install:
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
