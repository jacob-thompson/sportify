.PHONY: clean build install run test
DEFAULT: install

clean:
	rm -rf dist .tox
build: clean
	python3 -m build
install: build
	pipx install dist/*.tar.gz --force
run:
	sportify
