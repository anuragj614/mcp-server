FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

COPY . .

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT []

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005", "--log-level", "info"]
