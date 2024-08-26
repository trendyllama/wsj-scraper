
defaut: test

.PHONY: test

test:

	python -m unittest

clean:

	find . | grep -E "__pycache__" | xargs rm -rf