all: ti

ti:
	@ .venv/bin/python ti.py --width=64 --height=64 --scale=16 img/autumn.jpg

cur:
	.venv/bin/python curexample.py

testcolor:
	./testcolor.sh

init:
	python3 -m venv .venv

install:
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
