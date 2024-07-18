SHELL:=/usr/bin/env bash -O globstar

DOCKER_IMAGE ?= develogame
DOCKER_IMAGE_TAG ?= latest
DOCKER_TARGET ?= build

build/docker:
	docker build \
		--progress=plain \
		--tag ${DOCKER_IMAGE}:${DOCKER_IMAGE_TAG} \
		--target ${DOCKER_TARGET} \
		--pull \
		.

install:
	poetry install

lint: flake8 mypy black

flake8:
	poetry run flake8 **/*.py

mypy:
	poetry run mypy **/*.py

black/check:
	poetry run black --check --diff ./

black:
	poetry run black ./

isort:
	poetry run isort **/*.py

fix: isort black
