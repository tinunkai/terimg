all: ti

ti:
	.venv/bin/python ti.py img/autumn.jpg

cur:
	.venv/bin/python curimg.py

init:
	python3 -m venv .venv

install:
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
