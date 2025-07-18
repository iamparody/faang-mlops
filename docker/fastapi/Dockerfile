FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY fastapi_app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY fastapi_app /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
