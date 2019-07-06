# Simple makefile for tiptabs

# Create the environment directory and install all requirements
env:
	virtualenv env
	./env/bin/pip install -r requirements.txt

# Build the docker image
docker:
	docker build .

# Install the project
install:
	pip install .

# Install the project on the command line
devel:
	pip install -e .

test:
	make -C tests test

clean:
	find ./tests/__pycache__ -type f -name '*.pyc' -exec /bin/rm {} \;

.PHONY: env docker install devel test
