FROM python:3.12

WORKDIR /usr/workspace

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps

COPY . .

CMD ["pytest", "-v", "-s"]

