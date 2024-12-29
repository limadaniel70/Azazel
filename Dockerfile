FROM python:3.12-slim-bookworm

WORKDIR /Azazel

COPY dist/*.whl /Azazel/

RUN pip install --no-cache-dir /Azazel/*.whl && rm -f /Azazel/*.whl

COPY . /Azazel/

ENTRYPOINT [ "python3", "-B", "-m", "azazel" ]
