test: FORCE
	mypy sleepingqueens
	python3 -m unittest
	
FORCE: ;
