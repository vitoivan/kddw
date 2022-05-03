COVERAGE := coverage.txt
COVERAGE_BIN := .coverage
POSTGRES_PWD := 123456

define COVERAGE_MSG
+------------------------------------------------+
|                                                |
|         Check the file "$(COVERAGE)"          |
|                                                |
+------------------------------------------------+
endef
export COVERAGE_MSG


all: run

run:
	@flask run

resetpg:
	@sudo docker stop postgres
	@sudo docker rm postgres
	@sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=$(POSTGRES_PWD) -d postgres

mg: 
	@rm -rf migrations
	@flask db init
	@flask db migrate
	@flask db upgrade

test:
	@coverage run -m pytest

coverage:
	@coverage report -m > $(COVERAGE) 
	@echo "$$COVERAGE_MSG"

# Remove coverage files and .pyc/.pyo files
clean:
	@rm -f $(COVERAGE) $(COVERAGE_BIN) 
	@find . | grep -E "/__pycache__$|\.pyc$|\.pyo$\" | xargs rm -rf

.PHONY: clean coverage test mg resetpg run all