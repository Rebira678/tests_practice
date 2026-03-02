FROM python=3.2-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python","-m","pytest","-v"]