#!/usr/bin/env bash

cd ..

curl -sSL https://install.python-poetry.org | python3 -

poetry install --whitout dev