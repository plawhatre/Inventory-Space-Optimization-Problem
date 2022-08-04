run:
	python3 main.py
debug:
	python3 -m pdb main.py
typehint:
	mypy  main.py
remove:
	cat .gitignore | xargs -I {} rm -rf {}