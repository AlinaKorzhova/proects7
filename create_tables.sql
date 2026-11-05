CREATE TABLE employees
(
  first_name varchar(100) PRIMARY KEY,
  last_name varchar(100) NOT NULL,
  title varchar(100) NOT NULL,
  birth_date date NOT NULL,
  notes text NOT NULL
);

SELECT * FROM employees

CREATE TABLE customers
(
  customer_id varchar(100) PRIMARY KEY,
  company_name varchar(100),
  contact_name varchar(100)
);

SELECT * FROM customers

CREATE TABLE orders
(
  order_id int PRIMARY KEY,
  customer_id varchar(100) REFERENCES customers(customer_id),
  employee_id int REFERENCES employees(employee_id),
  order_date date NOT NULL,
  ship_city varchar(100) NOT NULL
);

SELECT * FROM orders