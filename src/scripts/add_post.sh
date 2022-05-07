#!/bin/sh

set -x

PORT=8000

curl -X POST http://localhost:${PORT}/posts \
    -d  '{ "id": 2, "title": "Lorem Ipsum tres", "content": "content goes here"}' \
    -H 'Content-Type: application/json'

