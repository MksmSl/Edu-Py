import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='dbMaks2401',
    port=5432,
)

with    connection.cursor() as cursor:

    cursor.execute("""SELECT * FROM public.users""")

    print(cursor.fetchall())


