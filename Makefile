cleanlog:
	ls | grep .log | xargs -I {} rm -rf {} 

run_default: cleanlog
	python3 main.py > stdout.log

run: cleanlog
	python3 main.py --setdefault 1 > stdout.log

debug: cleanlog
	python3 -m pdb main.py

typehint:
	mypy  main.py

clean: cleanlog
	cat .gitignore | xargs -I {} rm -rf {} 