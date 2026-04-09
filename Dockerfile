FROM python:3.14.3-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_NO_CACHE=1\
    UV_COMPILE_BYTECODE=1

WORKDIR /app

# 準備 psycopg2 需要的編譯環境
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./
# 透過 uv sync 建立環境
RUN uv sync --frozen

COPY . .

# 透過 uv run 啟動 uvicorn，確保讀取到虛擬環境
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
