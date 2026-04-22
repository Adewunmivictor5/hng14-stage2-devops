# ---- Builder Stage ----
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# ---- Final Stage ----
FROM python:3.11-slim

WORKDIR /app

# install curl
# hadolint ignore=DL3008,DL3015
RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

# create user
RUN useradd -m appuser

# copy installed packages correctly
COPY --from=builder /usr/local /usr/local

# copy app
COPY . .

# fix permissions
RUN chown -R appuser:appuser /app

USER appuser

ENV PATH=/usr/local/bin:$PATH

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
