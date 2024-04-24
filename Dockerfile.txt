FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY text_counter.py .
COPY paragraphs.txt /app/
CMD ["python", "text_counter.py"]
