run:
	rm *.log | python3 main.py
debug:
	python3 -m pdb main.py
typehint:
	mypy  main.py
clean:
	cat .gitignore | xargs -I {} rm -rf {} | rm -f *.log