FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "scraper.py"]