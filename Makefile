
SERVICE_NAME=fastapi-api-jwt

SERVICVE_TEMPLATE=60-service.cf.yaml

PORT = 8000

# -----------------------------------------------------------------------------

define check_json_file 
	@if [ ! -f $(1) ]; than \
		echo "Cannot find $(1)"; \
		exit 1 ]
	fi
	@echo -n -c "\t$(1) : " 
	@cat $(!) | jq
	@echo OK
endef

# -----------------------------------------------------------------------------

test:
	@echo "Checking intents JSON file..."
	$(call check_json_file ./dataset/intents.json)

run:
	uvicorn --host 0.0.0.0 --app-dir src app.main:app

develop:
	uvicorn --host 0.0.0.0 --app-dir src app.main:app --reload

setup:
	@ignore -- Ignore setup

compile:
	@ignore -- Ignore compile

unit-tests:
	@ignore -- Ignore unit-tests

chk-data:
	src/scripts/chk_intemts.py

pylint:
	-(cd src; pylint app)

# ----- Local Docker Methods  -------------------------------------------------

local-build:
	docker build -t fastapi-app .


local-run:
	docker run -it --rm -p 127.0.0.1:$(PORT):$(PORT) fastapi-app

local-run-bg:
	docker run -it --rm -d -p 127.0.0.1:$(PORT):$(PORT) fastapi-app &


local-ngrok:
	ngrok http http://localhost:$(PORT)

local-test:
	-(cd tests; echo OK)

# -----------------------------------------------------------------------------

