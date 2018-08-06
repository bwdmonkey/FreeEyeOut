all: install

# List all commands
.PHONY: ls
ls:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs

.PHONY: install
install:
	pip install virtualenv
	virtualenv venv
	( \
		source venv/bin/activate; \
		pip install -r FreeEyeOut/requirements.txt \
    )
