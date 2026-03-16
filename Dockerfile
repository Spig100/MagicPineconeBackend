FROM python:3.14.3-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_NO_CACHE=1\
    UV_COMPILE_BYTECODE=1

WORKDIR /app

COPY pyproject.toml ./

RUN uv pip install --system -r pyproject.toml

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
