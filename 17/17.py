import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='dbMaks2401',
    port=5432,
)


