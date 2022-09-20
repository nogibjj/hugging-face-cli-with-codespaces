install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	#conda env create -f environment.yml
	#conda activate hf
	##had to do this as well
	#conda install pytorch torchvision -c pytorch

test:
	#python -m pytest -vv test_main.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py

all: install lint test