install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	#conda env create -f environment.yml
	#conda activate hf
	##had to do this as well
	#conda install pytorch torchvision -c pytorch
	#conda install -c conda-forge pyarrow
install-m1:
	pip install --upgrade pip &&\
		pip install -r m1-requirements.txt

install-only-conda-hf:
	#conda create --name fineTune
	#conda activate fineTune
	#conda install -c huggingface transformers
	#conda install -c conda-forge datasets
	#conda install jupyterlab
	#conda install pytorch torchvision -c pytorch

test:
	#python -m pytest -vv test_main.py

format:
	black *.py

refactor: format lint

lint:
	pylint --disable=R,C *.py

all: install lint test