CREATE EXTENSION "uuid-ossp";
CREATE EXTENSION "pgcrypto";

CREATE TYPE user_sex AS ENUM ('Male', 'Female', 'Other');

CREATE TABLE users(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    email varchar NOT NULL UNIQUE,
    password varchar NOT NULL,
    first_name varchar NOT NULL,
    last_name varchar NOT NULL,
    birthday date,
    last_login date,
    registration_date date NOT NULL DEFAULT now(),
    sex user_sex NOT NULL,
    phone_number varchar NOT NULL,
    country varchar NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE stocks(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    symbol varchar(10) NOT NULL UNIQUE,
    company_name varchar(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE user_stocks(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    user_id uuid NOT NULL REFERENCES users(id),
    stock_id uuid NOT NULL REFERENCES stocks(id),
    open_price real NOT NULL CHECK (open_price > 0),
    quantity integer NOT NULL CHECK (quantity > 0),
    PRIMARY KEY(id)
);

SELECT email, stocks.symbol, AVG(open_price) AS average_open_price, SUM(user_stocks.quantity) AS total_quantity FROM users
INNER JOIN user_stocks ON user_stocks.user_id = users.id
INNER JOIN stocks ON stocks.id = user_stocks.stock_id
WHERE symbol IN ('APPL', 'TSLA') AND quantity BETWEEN 10 AND 101
GROUP BY symbol, email
HAVING SUM(user_stocks.quantity) > 10;