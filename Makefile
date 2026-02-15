help:
	@echo 
	@echo "install    					-- install backend dependencies"
	@echo "lint 						-- lint backend"
	@echo "format 						-- format backend"
	@echo "mypy 						-- type check backend"
	@echo "dev 							-- start mcp development server"
	@echo "inspect 						-- start mcp inspector"
	@echo "clean 						-- clean up docker containers"


.PHONY: install
install:
	uv sync --frozen

.PHONY: lint
lint:
	uv run ruff check .

.PHONY: format
format:
	uv run ruff check --fix .
	uv run ruff format .

.PHONY: mypy
mypy:
	uv run mypy .

.PHONY: dev
dev:
	@COMPOSE_MENU=false docker compose up --build --no-log-prefix
	@echo "⌛ Waiting 5 seconds for docker services to be healthy..."
	@sleep 5
# 	uv run uvicorn main:app --reload --host localhost --port 8005 --log-level info

.PHONY: clean
clean:
	docker compose down -v

.PHONY: inspect
inspect:
	npx @modelcontextprotocol/inspector --transport http --url http://localhost:8005/mcp