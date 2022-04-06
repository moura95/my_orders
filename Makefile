DEBUG?=0
VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python
PORT?=8000

ifdef DEBUG
DEPS_DEV=-r requirements.txt
endif

$(VENV_NAME)/bin/activate: requirements.txt
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -r requirements.txt ${DEPS_DEV}
	touch $(VENV_NAME)/bin/activate

.PHONY: prepare_venv
prepare_venv: $(VENV_NAME)/bin/activate

PHONY: runserver
run: prepare_venv
	${PYTHON} manage.py runserver 0.0.0.0:${PORT}

PHONY: migrate
migrate: prepare_venv
	${PYTHON} manage.py makemigrations
	${PYTHON} manage.py migrate

PHONY: test
test: prepare_venv
	${PYTHON} ./manage.py test

PHONY: check
check:
	# TODO: Code quality
	# TODO: Security settings
	${PYTHON} ./manage.py check
