POETRY = poetry run
.PHONY: install shell run format test sec docs img


install:
	@poetry install
shell:
	@poetry shell
format:
	@${POETRY} isort .
	@${POETRY} blue .
test:
	@${POETRY} pytest
cover:
	@${POETRY} pytest --cov=.
sec:
	@${POETRY} pip-audit
docs:
	@${POETRY} mkdocs serve
img:
	docker-compose --env-file .env up -d mongo
imgd:
	docker-compose --env-file .env down
#dckr:
#	sudo docker run --name ${DB_NAME} -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=${MONGO_USERNAME} -e MONGO_INITDB_ROOT_PASSWORD=${MONGO_PASSWORD} mongo