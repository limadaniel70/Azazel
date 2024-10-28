#!/usr/bin/env bash

poetry run isort azazel/
poetry run black azazel/
poetry run pylint azazel/ >> pylint.log
echo "-----------------------------" >> mypy.log
poetry run mypy azazel/ >> mypy.log
