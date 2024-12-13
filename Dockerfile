FROM python:3.12-slim-bookworm

WORKDIR /Azazel

COPY requirements.txt /Azazel/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /Azazel/

ENTRYPOINT [ "python3", "-B", "-m", "azazel" ]
