import psycopg2

conn_params = {
  "host": "localhost",
  "database": "test",
  "user": "postgres",
  "password": "12345"
}

with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO my_table VALUES (%s, %s)", (2, "Test"))
        conn.commit()
        cur.execute("SELECT * FROM my_table")

        rows = cur.fetchall()
        for row in rows:
            print(row)