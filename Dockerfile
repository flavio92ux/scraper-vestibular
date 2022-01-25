FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "scraper"]