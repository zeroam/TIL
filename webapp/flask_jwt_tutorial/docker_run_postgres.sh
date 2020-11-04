#!/bin/sh
docker run --rm \
    -e POSTGRES_USER=root \
    -e POSTGRES_PASSWORD=root \
    -e POSTGRES_DB=jwt_auth \
    -p 5432:5432 \
    -d postgres