#!/bin/sh

. venv/bin/activate
export FLASK_APP=app/__init__.py
export FLASK_ENV=development
flask run
