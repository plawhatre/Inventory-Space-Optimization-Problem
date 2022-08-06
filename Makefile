run_default:
	rm *.log | python3 main.py > stdout.log

run:
	rm *.log | python3 main.py --setdefault 1 > stdout.log

debug:
	python3 -m pdb main.py

typehint:
	mypy  main.py

clean:
	cat .gitignore | xargs -I {} rm -rf {} | rm -f *.log