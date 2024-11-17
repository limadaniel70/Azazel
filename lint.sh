#!/usr/bin/env bash

# FLAGS
MYPY_FLAGS="--strict --show-error-codes --warn-unused-ignores --pretty"
ISORT_FLAGS="--profile black"

TARGET_DIR="azazel/"

poetry run isort $ISORT_FLAGS $TARGET_DIR
poetry run black $TARGET_DIR
poetry run codespell $TARGET_DIR
poetry run pylint $TARGET_DIR >> pylint.log
echo "-----------------------------" >> mypy.log
poetry run mypy $MYPY_FLAGS $TARGET_DIR >> mypy.log
