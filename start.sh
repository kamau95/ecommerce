#!/bin/sh
gunicorn --bind 0.0.0.0:${PORT} "web:create_app()"
