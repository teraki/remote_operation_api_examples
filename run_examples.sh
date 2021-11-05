#! /bin/bash
set -e

poetry install
poetry run teraki_examples all "$@"
