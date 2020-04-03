LAB_B := bball
version_file := VERSION
VERSION := $(shell cat ${version_file})

docker-dev: Dockerfile
	docker build -t $(LAB_B):debug . --target dev 

run-dev: .env.list
	docker run --rm -it -p 3939:3939 --env-file .env.list $(LAB_B):debug sh

.PHONY: docker-dev run-dev