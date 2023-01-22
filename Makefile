test: FORCE
	mypy sleepingqueens
	mypy test
	python3 -m unittest
	
FORCE: ;
