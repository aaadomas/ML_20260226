FROM python:3.12-slim

WORKDIR src
COPY src


ENV UV_NO_DEV=1

RUN uv sync --locked