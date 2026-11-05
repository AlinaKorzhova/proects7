CREATE TABLE employees
(
  employee_id int PRIMARY KEY,
  first_name varchar(100) NOT NULL,
  last_name varchar(100) NOT NULL,
  title varchar(100) NOT NULL,
  birth_date date NOT NULL,
  notes text NOT NULL
);

INSERT INTO employees VALUES (1, 'Nancy', 'Davolio', 'Sales Representative', '1948-12-08', 'Education includes a BA in psychology from Colorado State University in 1970. She also completed The Art of the Cold Call. Nancy is a member of Toastmasters International.');

SELECT * FROM employees

CREATE TABLE customers
(
  customer_id varchar(100) PRIMARY KEY,
  company_name varchar(100),
  contact_name varchar(100)
);

INSERT INTO customers VALUES ('ALFKI', 'Alfreds Futterkiste', 'Maria Anders')

SELECT * FROM customers

CREATE TABLE orders
(
  order_id int PRIMARY KEY,
  customer_id varchar(100) REFERENCES customers(customer_id),
  employee_id int REFERENCES employees(employee_id),
  order_date date NOT NULL,
  ship_city varchar(100) NOT NULL
);

INSERT INTO orders VALUES (10248, 'VINET', 5, '1996-07-04', 'Reims')

SELECT * FROM orders