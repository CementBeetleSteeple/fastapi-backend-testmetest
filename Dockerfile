FROM python:3.11-slim as builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target /packages

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /packages /usr/lib/python3.11/site-packages
COPY app/ ./app/
ENV PYTHONPATH=/app PORT=8000
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
