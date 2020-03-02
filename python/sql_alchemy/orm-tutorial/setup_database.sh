docker run --name sqlalchemy-orm-psql \
    -e POSTGRES_PASSWORD=dbpassword \
    -e POSTGRES_USER=dbuser \
    -e POSTGRES_DB=sqlalchemy-orm-tutorial \
    -p 5432:5432 \
    -d postgres