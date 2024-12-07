.PHONY: clean build install run
DEFAULT: install

clean:
	rm -rf dist
build: clean
	python3 -m build
install: build
	pipx install dist/*.tar.gz --force
run:
	sportify
