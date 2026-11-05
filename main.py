import csv
from pathlib import Path
import psycopg2

BASE_DIR = Path(__file__).parent
data_dir = BASE_DIR / "data"

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345",
)
cur = conn.cursor()


def read_csv_as_dicts(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


employees_data = read_csv_as_dicts(data_dir / "employees_data.csv")
customers_data = read_csv_as_dicts(data_dir / "customers_data.csv")
orders_data = read_csv_as_dicts(data_dir / "orders_data.csv")

# 1. Сначала родители (на них ссылаются внешние ключи), потом заказы
for row in customers_data:
    cur.execute(
        "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s);",
        (row["customer_id"], row["company_name"], row["contact_name"]),
    )

for row in employees_data:
    cur.execute(
        "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s);",
        (row["employee_id"], row["first_name"], row["last_name"],
        row["title"], row["birth_date"], row["notes"]),
    )

for row in orders_data:
    cur.execute(
        "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s);",
        (row["order_id"], row["customer_id"], row["employee_id"],
        row["order_date"], row["ship_city"]),
    )

conn.commit()

# Проверки
cur.execute("""
    SELECT customer_id, company_name, contact_name
    FROM customers WHERE customer_id = 'WOLZA';
""")
print("Проверка customers:", cur.fetchall())

cur.execute("""
    SELECT employee_id, first_name, last_name, title, birth_date, notes
    FROM employees WHERE employee_id = 9;
""")
print("Проверка employees:", cur.fetchall())

cur.execute("""
    SELECT order_id, customer_id, employee_id, order_date, ship_city
    FROM orders WHERE order_id = 11077;
""")
print("Проверка orders:", cur.fetchall())

cur.close()
conn.close()
